# Hero-Video

- `hero.mp4` – Hintergrundvideo des Hero (H.264, 1280×720, stumm, ca. 9 s, aus `gemini_generated_video_25A97AA7.mov` konvertiert)
- `hero.webm` – gleiche Datei als VP9/WebM (Fallback für Browser ohne H.264)
- `hero-poster.jpg` – Standbild (letzter Frame), wird gezeigt, bis das Video geladen ist

Die Seite spielt das Video automatisch einmal ab und bleibt auf dem letzten Bild stehen.
Über `data-video-end` am `<section class="hero">` in `index.html` lässt sich eine frühere
Stopp-Sekunde setzen (0 = bis zum Ende abspielen).

Neues Video einbauen (Konvertierung ins Web-Format):

```bash
ffmpeg -i quelle.mov -an -c:v libx264 -pix_fmt yuv420p -crf 23 -movflags +faststart assets/video/hero.mp4
ffmpeg -i assets/video/hero.mp4 -an -c:v libvpx-vp9 -crf 33 -b:v 0 assets/video/hero.webm
ffmpeg -sseof -0.1 -i assets/video/hero.mp4 -frames:v 1 assets/video/hero-poster.jpg
```
