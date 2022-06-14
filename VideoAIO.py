from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import Channel
from pytube import YouTube
import os.path
import os
from youtube_transcript_api import YouTubeTranscriptApi
from moviepy.editor import *


def directory_select(null):
    directory_selected = filedialog.askdirectory()
    frame_calc(directory_selected + "/")


def directory_select2(null):
    directory_selected = filedialog.askdirectory()
    resolution_calc(directory_selected + "/")


def resolution_calc(directory):
    filetypes = [".mp4", ".wmv", ".avi", ".mkv", ".flv"]
    for filetype in filetypes:
        for filename in os.listdir(directory):
            if filename.endswith(filetype):
                print(filename)
                file = directory + str(filename)
                with open(file, 'r') as f:
                    clip = VideoFileClip(file)
                    video_resolution = clip.size
                    print("Resolution is : " + str(video_resolution))
            else:
                continue


def frame_calc(directory):
    filetypes = [".mp4", ".wmv", ".avi", ".mkv", ".flv"]
    for filetype in filetypes:
        for filename in os.listdir(directory):
            if filename.endswith(filetype):
                print(filename)
                file = directory + str(filename)
                with open(file, 'r') as f:
                    clip = VideoFileClip(file)
                    rate = clip.fps
                    print("FPS : " + str(rate))
            else:
                continue


def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%d:%02d:%02d" % (hour, min, sec)


def string_search(string):
    for filename in os.listdir(folder_selected_s):
        if filename.endswith(".txt"):
            txt_file = open(folder_selected_s + "/" + str(filename), "r")
            for line in txt_file:
                if string in line:
                    print(str(txt_file)[80:-29])
                    print(line)
                    try:
                        timestamp = convert(float((next(txt_file))[9:-2]))
                        print(timestamp)
                    except:
                        pass


def string_value(string_s):
    global folder_selected_s
    folder_selected_s = filedialog.askdirectory()
    string_search(string_s)


def valueGET(val1):
    global folder_selected
    folder_selected = filedialog.askdirectory()
    channel_sub_download(val1)


def txt_saver(filename, string_save):
    remove_list = ["{'text':", "[", "]", "}"]
    for x in remove_list:
        string_save = string_save.replace(x, "")
    string_save = string_save.replace(",", ",\n")
    with open(os.path.join(folder_selected, " %s.txt" % filename), 'w+') as f:
        f.write(string_save)


def video_url_extractor(channel_url, list_of_url):
    channel_url_list = Channel(channel_url)
    for url in channel_url_list.video_urls:
        list_of_url.append(url)
    return list_of_url


def channel_sub_download(channel_url):
    url_list = []
    url_list = video_url_extractor(channel_url, url_list)
    for url in url_list:
        try:
            video_sub = YouTubeTranscriptApi.get_transcript(url[32:43])
            video_title = YouTube(url)
            video_title = video_title.title
            special_char = ["#", "%", "&", "{", "}", "\\", "<", ">", "*", "?", "/", "$", "!", "'", '"', ":", "@", "+", "`", "|", "="]
            for char in special_char:
                video_title = video_title.replace(char, "")
            txt_saver(video_title, str(video_sub))
        except:
            pass


def main():
    tab1 = ttk.Frame(tabs)
    tab2 = ttk.Frame(tabs)
    tab3 = ttk.Frame(tabs)
    tab4 = ttk.Frame(tabs)
    tabs.add(tab1, text="Download youtube sub from channel")
    tabs.add(tab2, text="Text search")
    tabs.add(tab3, text="frame rate of all videos in directory")
    tabs.add(tab4, text="Resolution of all videos in directory")

    label4 = Entry(tab1, width=60)
    label4.pack(side=TOP, padx=0, pady=10)

    string_s = Entry(tab2, width=60)
    string_s.pack(side=TOP, padx=0, pady=10)

    string_s_b = Button(tab2, text="Enter text to search for above and click here", width=40, command=lambda: string_value(string_s.get()))
    string_s_b.pack(side=TOP, padx=0, pady=10)

    submit_url = Button(tab1, text="Enter Channel url above and click here", width=40, command=lambda: valueGET(label4.get()))
    submit_url.pack(side=TOP, padx=0, pady=10)

    empty = Entry(tab3, width=0)
    empty2 = Entry(tab3, width=0)

    directory_select_v = Button(tab3, text="Select directory by clicking here", width=40, command=lambda: directory_select(empty.get()))
    directory_select_v.pack(side=TOP, padx=0, pady=10)

    directory_select_v_2 = Button(tab4, text="Select directory by clicking here", width=40, command=lambda: directory_select2(empty.get()))
    directory_select_v_2.pack(side=TOP, padx=0, pady=10)

    root.geometry("1000x480")
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.title("Video AIO")
    tabs = ttk.Notebook(root)
    tabs.pack(fill=BOTH, expand=TRUE)
    main()
