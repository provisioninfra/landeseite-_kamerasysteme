import sys, time, onnxruntime as ort
from rembg import new_session, remove
from PIL import Image
modell, quelle, ziel = sys.argv[1:4]
so = ort.SessionOptions(); so.intra_op_num_threads = 2; so.inter_op_num_threads = 1
s = new_session(modell, sess_opts=so)
t = time.time(); im = Image.open(quelle).convert('RGB')
remove(im, session=s, only_mask=True).save(ziel); print(ziel.split('/')[-1], im.size, round(time.time()-t, 1), 's')
