import sys, cv2, time
from PIL import Image
import numpy as np
U='/root/.claude/uploads/8101c591-dd55-5971-91e8-f9b3f727dc4d/'
n, f, faktor, crop = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
im = Image.open(U+f)
alpha = im.convert('RGBA').getchannel('A') if im.mode in ('RGBA','P','LA') else None
rgb = im.convert('RGB')
if crop != '-':
    box = tuple(int(v) for v in crop.split(',')); rgb = rgb.crop(box); alpha = alpha.crop(box) if alpha else None
t = time.time()
if faktor > 1:
    sr = cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel(f'frei2/sr/EDSR_x{faktor}.pb'); sr.setModel('edsr', faktor)
    out = sr.upsample(cv2.cvtColor(np.asarray(rgb), cv2.COLOR_RGB2BGR)); rgb = Image.fromarray(cv2.cvtColor(out, cv2.COLOR_BGR2RGB))
    if alpha: alpha = alpha.resize(rgb.size, Image.LANCZOS)
rgb.save(f'frei2/gross/{n}.png')
if alpha: alpha.save(f'frei2/gross/{n}-alpha.png')
print(n, rgb.size, round(time.time()-t,1), 's')
