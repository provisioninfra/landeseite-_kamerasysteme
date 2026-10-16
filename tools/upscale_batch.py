import sys, os, time, glob, torch
from PIL import Image
from sr import load, upscale
model = sys.argv[1]
torch.set_num_threads(4)
net = load(model)
files = sorted(glob.glob('frames/f*.png'))
t0 = time.time()
for i, f in enumerate(files, 1):
    dst = 'out/' + os.path.basename(f)
    if os.path.exists(dst): continue
    out = upscale(net, Image.open(f))
    out = out.resize((3840, 2160), Image.LANCZOS)     # 4x-Ausgabe auf 4K herunterrechnen (Supersampling)
    out.save(dst, compress_level=1)
    if i % 10 == 0 or i == len(files):
        el = time.time() - t0; print(f'{i}/{len(files)} frames, {el/60:.1f} min, ETA {el/i*(len(files)-i)/60:.1f} min', flush=True)
print('DONE', flush=True)
