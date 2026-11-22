import sys
from PIL import Image, ImageDraw
U='/root/.claude/uploads/8101c591-dd55-5971-91e8-f9b3f727dc4d/'
W,H=1200,900
def frei(im, tol=18):
    """Weißen, vom Rand erreichbaren Hintergrund transparent machen."""
    im=im.convert('RGBA'); w,h=im.size
    mask=Image.new('L',(w,h),0); px=im.load()
    seed=Image.new('RGB',(w,h)); seed.paste(im.convert('RGB'))
    # Flutfüllung von allen Randpunkten auf einer Kopie, Markierfarbe Magenta
    for x,y in [(0,0),(w-1,0),(0,h-1),(w-1,h-1),(w//2,0),(w//2,h-1),(0,h//2),(w-1,h//2)]:
        if sum(seed.getpixel((x,y)))>3*(255-tol)-1: ImageDraw.floodfill(seed,(x,y),(255,0,255),thresh=tol*3)
    sp=seed.load()
    for y in range(h):
        for x in range(w):
            if sp[x,y]==(255,0,255): px[x,y]=(255,255,255,0)
    return im
def einpassen(im, rand=0.08):
    im=im.convert('RGBA'); bb=im.getchannel('A').getbbox(); im=im.crop(bb)
    s=min(W*(1-2*rand)/im.width, H*(1-2*rand)/im.height); s=min(s, 2.2)
    im=im.resize((max(1,int(im.width*s)),max(1,int(im.height*s))), Image.LANCZOS)
    c=Image.new('RGBA',(W,H),(0,0,0,0)); c.paste(im,((W-im.width)//2,(H-im.height)//2),im); return c
def fuellen(im, fx=0.5, fy=0.5):
    im=im.convert('RGB'); s=max(W/im.width,H/im.height); im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    x=int((im.width-W)*fx); y=int((im.height-H)*fy); return im.crop((x,y,x+W,y+H))
B=[('evva-4ks-mechanischer-zylinder', lambda: einpassen(Image.open(U+'7b59759d-image.png'))),
   ('evva-akura-44-mechanischer-zylinder', lambda: einpassen(Image.open(U+'a6169c67-image.png'))),
   ('simonsvoss-digitalzylinder-ax', lambda: fuellen(Image.open(U+'87e79b7d-image.png'),0.5,0.5)),
   ('evva-wandleser-steuereinheit', lambda: einpassen(frei(Image.open(U+'f2d74b06-image.png')))),
   ('evva-certified-partner', lambda: einpassen(frei(Image.open(U+'9b39c5a4-image.png')),0.05)),
   ('evva-elektronischer-knaufzylinder', lambda: einpassen(Image.open(U+'19254087-image.png'))),
   ('simonsvoss-smarthandle-ax-langschild', lambda: einpassen(frei(Image.open(U+'2eb98874-image.jpg')))),
   ('simonsvoss-smarthandle-ax-tuer', lambda: fuellen(Image.open(U+'46f0f6d3-image.jpg'),0.35,0.5)),
   ('evva-xesar-komponenten', lambda: einpassen(Image.open(U+'031a0a8b-image.webp'))),
   ('keyota-knaufzylinder', lambda: fuellen(Image.open(U+'a39a09ba-image.webp'),0.5,0.62))]
for n,f in B:
    im=f(); im.save(n+'.webp','WEBP',quality=82,method=6)
    import os; print(n, im.mode, os.path.getsize(n+'.webp')//1024,'KB')
