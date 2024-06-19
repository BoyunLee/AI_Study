import os
import cv2

def get_files(path):
    list_files = []
    for root, subdirs, files in os.walk(path):
        for f in files:
            fullpath = os.path.join(root, f)
            list_files.append(fullpath)
    return list_files

image_files = get_files('C:\\study\\20240308')

if image_files:
    img = cv2.imread(image_files[0])
    height, width, channel = img.shape

    fps = 1
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    writer = cv2.VideoWriter(os.path.join(BASE_DIR, 'puppy.mp4'), fourcc, fps, (width, height))

    for file in image_files:
        img = cv2.imread(file)
        writer.write(img)
        if cv2.waitKey(33) == 27:
            break

    writer.release()