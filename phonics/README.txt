Bé Học Vui - Phase 2 Phonics (Generated placeholders)
Contents:
- audio/ : placeholder WAV files per phoneme (sine beep). Replace with real mp3/wav audio if desired.
- lessons/ : JSON lesson files organized by level
- metadata.json : package metadata

Notes:
- Audio files are WAV. If you need MP3, convert them using ffmpeg:
  ffmpeg -i audio/a_short.wav audio/a_short.mp3
- To integrate into the app, copy the 'audio' and 'lessons' folders into the appropriate frontend/backend assets.
