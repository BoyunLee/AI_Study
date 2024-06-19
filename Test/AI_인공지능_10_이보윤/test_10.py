import cv2

video_path = "c:\\study\\test_boyun\\test_10\\video.mp4"

video = cv2.VideoCapture(video_path)

for i in range(20):
    ret, frame = video.read()
    if ret:
        image_path = f"C:/study/test_boyun/test_10/{i}.jpg"
        cv2.imwrite(image_path, frame)

video.release()