from pytube import Channel
from pytube import YouTube
import os
from moviepy.editor import *
import moviepy.editor as mpe
import ffmpeg


#c = Channel('https://www.youtube.com/c/ProgrammingKnowledge')

def combine_audio(vidname, audname, outname, frames):
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname, fps=frames)

def frame_calc_2(directory):
    filetypes = [".mp4", ".wmv", ".avi", ".mkv", ".flv"]
    for filetype in filetypes:
        for filename in os.listdir(directory):
            if filename.endswith(filetype):
                file = directory + "/" + str(filename)
                with open(file, 'r') as f:
                    clip = VideoFileClip(file)
                    rate = clip.fps
            else:
                continue
    return rate


vid_url = 'https://www.youtube.com/watch?v=km2OPUctni4'
vid_tit = YouTube(vid_url).title
down_vid = YouTube(vid_url).streams.order_by("resolution").last().download()
down_aud = YouTube(vid_url).streams.filter(only_audio=True).last().download()


fps = frame_calc_2(down_vid[:-len(vid_tit)-4])

try:
    os.rename(down_aud,  down_aud[:-5]+"1"+".mp3")
except FileExistsError:
    pass

video_name = down_vid[len(os.getcwd())+1:]
audio_name = down_aud[len(os.getcwd())+1:-5]+"1"+".mp3"

combine_audio(video_name, audio_name, "test_works.mp4", fps)

