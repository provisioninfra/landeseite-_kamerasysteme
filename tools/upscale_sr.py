import sys, time, torch, torch.nn as nn, torch.nn.functional as F, numpy as np
from PIL import Image

class SRVGGNetCompact(nn.Module):
    def __init__(self, num_feat=64, num_conv=16, upscale=4):
        super().__init__()
        self.upscale = upscale
        self.body = nn.ModuleList([nn.Conv2d(3, num_feat, 3, 1, 1), nn.PReLU(num_parameters=num_feat)])
        for _ in range(num_conv):
            self.body.append(nn.Conv2d(num_feat, num_feat, 3, 1, 1)); self.body.append(nn.PReLU(num_parameters=num_feat))
        self.body.append(nn.Conv2d(num_feat, 3 * upscale * upscale, 3, 1, 1))
        self.upsampler = nn.PixelShuffle(upscale)
    def forward(self, x):
        out = x
        for m in self.body: out = m(out)
        out = self.upsampler(out)
        return out + F.interpolate(x, scale_factor=self.upscale, mode='nearest')

def load(name):
    cfg = {'anime': ('realesr-animevideov3.pth', 16), 'general': ('realesr-general-x4v3.pth', 32)}[name]
    net = SRVGGNetCompact(num_conv=cfg[1])
    sd = torch.load(cfg[0], map_location='cpu', weights_only=True)
    sd = sd.get('params_ema', sd.get('params', sd))
    net.load_state_dict(sd, strict=True); net.eval()
    return net

@torch.no_grad()
def upscale(net, img):
    x = torch.from_numpy(np.asarray(img.convert('RGB'), dtype=np.float32) / 255.).permute(2, 0, 1).unsqueeze(0)
    y = net(x).clamp_(0, 1)[0].permute(1, 2, 0).numpy()
    return Image.fromarray((y * 255.0 + 0.5).astype(np.uint8))

if __name__ == '__main__':
    model, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    torch.set_num_threads(4)
    net = load(model)
    t = time.time(); out = upscale(net, Image.open(src)); dt = time.time() - t
    out.save(dst); print(model, out.size, f'{dt:.1f}s')
