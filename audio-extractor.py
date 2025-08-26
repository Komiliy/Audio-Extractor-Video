import moviepy

cvt_video = moviepy.VideoFileClip("Orif Alimaxsumov.mp4")
ext_audio = cvt_video.audio

ext_audio.write_audiofile("audio_Extracted.mp3")
