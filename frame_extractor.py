import os
import cv2


def frame_extract(directory):
    if not os.path.exists('training_set'):
        os.mkdir('training_set')
    filetypes = [".mp4", ".wmv", ".avi", ".mkv", ".flv", ".ts"]
    for filetype in filetypes:
        for filename in os.listdir(directory + "/videos"):
            if filename.endswith(filetype):
                vidcap = cv2.VideoCapture(directory + "/videos/" + filename)
                success, image = vidcap.read()
                count = 0
                while success:
                    cv2.imwrite(directory + "/training_set/" + str(filename)[:-len(filetype)] + "_" + "frame%d.jpg" % count, image)
                    success, image = vidcap.read()
                    count += 1


frame_extract(os.getcwd())






