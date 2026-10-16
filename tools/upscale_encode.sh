#!/bin/bash
# Frames (3840x2160) -> 4K-Video für Desktop, 1440p-Version für Mobil, Standbild aus dem 4K-Video
set -e
cd "$(dirname "$0")"
ffmpeg -v error -y -framerate 24 -i out/f%04d.png -an -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 20 -preset slow -movflags +faststart kamera-hero-video-4k.mp4
ffmpeg -v error -y -i kamera-hero-video-4k.mp4 -an -vf "scale=2560:1440:flags=lanczos" -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 21 -preset slow -movflags +faststart kamera-hero-video-mobil.mp4
ffmpeg -v error -y -sseof -0.1 -i kamera-hero-video-4k.mp4 -frames:v 1 -q:v 2 kamera-hero-standbild-4k.jpg
ls -la kamera-hero-video-4k.mp4 kamera-hero-video-mobil.mp4 kamera-hero-standbild-4k.jpg
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,nb_frames -of default=nw=1 kamera-hero-video-4k.mp4
