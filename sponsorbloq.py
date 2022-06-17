import sponsorblock as sb
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

vid_url = "https://www.youtube.com/watch?v=cZzFJQVoa38"
client = sb.Client()
segments = client.get_skip_segments(vid_url)

sponsor_timestamps = {}

for x in segments:
    if x.category == "sponsor":
        sponsor_timestamps[len(sponsor_timestamps)+1] = (x.start, x.end)

print(sponsor_timestamps)
#ffmpeg_extract_subclip("video1.mp4", start_time, end_time, targetname="test.mp4")

