import sys, numpy as np, cv2
from PIL import Image
from pymatting import estimate_foreground_ml
U='/root/.claude/uploads/8101c591-dd55-5971-91e8-f9b3f727dc4d/'; G='frei2/gross/'; OUT='technik2/'
W,H=1200,900
JOBS={
 'evva-4ks-mechanischer-zylinder':(U+'7b59759d-image.png','vendor',0.07),
 'evva-akura-44-mechanischer-zylinder':(U+'a6169c67-image.png','vendor',0.06),
 'evva-elektronischer-knaufzylinder':(U+'19254087-image.png','vendor',0.08),
 'evva-xesar-komponenten':(G+'xesar.png',G+'xesar-alpha.png',0.07),
 'evva-wandleser-steuereinheit':(G+'wandleser.png',G+'wandleser-maske.png',0.08),
 'evva-certified-partner':(G+'partner.png',G+'partner-maske.png',0.05),
 'simonsvoss-smarthandle-ax-langschild':(G+'langschild.png',G+'langschild-maske.png',0.07),
 'simonsvoss-smarthandle-ax-tuer':(G+'smarthandle-tuer.png',G+'smarthandle-tuer-maske.png',0.07),
 'simonsvoss-digitalzylinder-ax':(U+'87e79b7d-image.png','frei2/dcax-maske-ohne-spiegelung.png',0.05),
 'keyota-knaufzylinder':(G+'keyota.png',G+'keyota-maske.png',0.07)}
def pm_resize(rgb,a,size):
    """vormultipliziert skalieren"""
    pre=np.dstack([rgb*a[...,None],a]).astype(np.float32)
    r=cv2.resize(pre,size,interpolation=cv2.INTER_AREA if size[0]<rgb.shape[1] else cv2.INTER_LANCZOS4)
    al=np.clip(r[...,3],0,1); col=np.where(al[...,None]>1e-4, r[...,:3]/np.maximum(al[...,None],1e-4), 0)
    return np.clip(col,0,1), al
def verfeinern(rgb,m):
    """Closed-Form-Matting nur im Kantenband, kachelweise; danach Inseln und kleine Löcher entfernen."""
    from pymatting import estimate_alpha_cf
    hard=(m>0.5).astype(np.uint8); k=np.ones((3,3),np.uint8)
    w=max(3,int(round(min(rgb.shape[:2])/350)))   # Bandbreite passend zur Bildgröße
    fg=cv2.erode(hard,k,iterations=w); bgm=cv2.erode(1-hard,k,iterations=w)
    tri=np.full(m.shape,0.5); tri[fg==1]=1; tri[bgm==1]=0
    a=tri.copy(); H,W=m.shape; T,O=320,24
    for y in range(0,H,T):
        for x in range(0,W,T):
            y0,x0=max(0,y-O),max(0,x-O); y1,x1=min(H,y+T+O),min(W,x+T+O)
            tt=tri[y0:y1,x0:x1]
            if not ((tt>0)&(tt<1)).any(): continue
            if not (tt==1).any() or not (tt==0).any():
                sub=m[y0:y1,x0:x1]
            else:
                sub=estimate_alpha_cf(rgb[y0:y1,x0:x1],tt)
            yy0,xx0=y-y0,x-x0; yy1,xx1=yy0+min(T,H-y),xx0+min(T,W-x)
            unk=(tri[y:y+T,x:x+T]>0)&(tri[y:y+T,x:x+T]<1)
            blk=a[y:y+T,x:x+T]; blk[unk]=sub[yy0:yy1,xx0:xx1][unk]
    a=np.clip(a,0,1); a[a<0.02]=0; a[a>0.98]=1
    # Inseln außerhalb und kleine Löcher innerhalb entfernen
    n,lab,st,_=cv2.connectedComponentsWithStats((a>0.02).astype(np.uint8),8)
    if n>1:
        groesst=np.argmax(st[1:,cv2.CC_STAT_AREA])+1; minf=st[groesst,cv2.CC_STAT_AREA]*0.002
        for i in range(1,n):
            if st[i,cv2.CC_STAT_AREA]<minf: a[lab==i]=0
    n,lab,st,_=cv2.connectedComponentsWithStats((a<0.5).astype(np.uint8),4)
    for i in range(1,n):
        x,y,ww,hh,ar=st[i]
        if ar<a.size*0.00015 and x>0 and y>0 and x+ww<a.shape[1] and y+hh<a.shape[0]: a[lab==i]=1
    # Kontur glätten: Fransen und Zacken unterhalb von sigma verschwinden, Kante wird subpixelgenau mit ~1,2 px Übergang
    sigma=max(1.2, min(a.shape)/700)
    g=cv2.GaussianBlur(a.astype(np.float32),(0,0),sigma)
    a=np.clip(0.5+(g-0.5)*np.sqrt(2*np.pi)*sigma/1.2,0,1).astype(np.float64)
    return a
nur=sys.argv[1:] or list(JOBS)
for n in nur:
    src,mk,rand=JOBS[n]
    im=Image.open(src)
    if mk=='vendor':
        a=np.asarray(im.convert('RGBA').getchannel('A')).astype(np.float64)/255; rgb=np.asarray(im.convert('RGB')).astype(np.float64)/255
    else:
        rgb=np.asarray(im.convert('RGB')).astype(np.float64)/255; a=np.asarray(Image.open(mk).convert('L')).astype(np.float64)/255
        if a.shape!=rgb.shape[:2]: a=np.asarray(Image.open(mk).convert('L').resize(im.size,Image.LANCZOS)).astype(np.float64)/255
        if 'alpha' not in mk: a=verfeinern(rgb,a)
    # auf Arbeitsgröße bringen (max. 2400 px breit), dann Hintergrundfarbe aus den Kanten herausrechnen
    s=min(1.0, 2400/rgb.shape[1], 1800/rgb.shape[0])
    if s<1: rgb,a=pm_resize(rgb,a,(int(rgb.shape[1]*s),int(rgb.shape[0]*s)))
    F=estimate_foreground_ml(rgb,a)
    ys,xs=np.where(a>0.01); F=F[ys.min():ys.max()+1,xs.min():xs.max()+1]; a=a[ys.min():ys.max()+1,xs.min():xs.max()+1]
    sc=min(W*(1-2*rand)/a.shape[1], H*(1-2*rand)/a.shape[0], 1.0)
    F,a=pm_resize(F,a,(round(a.shape[1]*sc),round(a.shape[0]*sc)))
    out=np.zeros((H,W,4)); y0=(H-a.shape[0])//2; x0=(W-a.shape[1])//2
    out[y0:y0+a.shape[0],x0:x0+a.shape[1],:3]=F; out[y0:y0+a.shape[0],x0:x0+a.shape[1],3]=a
    img=Image.fromarray((out*255+0.5).astype(np.uint8),'RGBA')
    img.save(OUT+n+'.webp','WEBP',quality=90,alpha_quality=100,method=6); img.save(OUT+n+'.png')
    print(n, 'Skalierung', round(sc,2), 'Objekt', a.shape[::-1])
