import os # windows 자원을 사용하기 위해 선언

import numpy as np, cv2
from Common.knn import find_number, place_middle            
import cv2
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import time
import pytesseract
import PIL
from PIL import Image


# 밑의 전역변수는 전처리를 하여 번호판을 자르기 위한 과정
MIN_AREA = 90 # 번호판 윤곽선 최소 범위 지정
MIN_WIDTH, MIN_HEIGHT = 1, 7 # 최소 너비 높이 지정
# MIN_AREA = 80 # 번호판 윤곽선 최소 범위 지정
# MIN_WIDTH, MIN_HEIGHT = 2, 8 # 최소 너비 높이 지정
MIN_RATIO, MAX_RATIO = 0.25, 1.0 # 최소 비율 범위 지정

MAX_DIAG_MULTIPLYER = 5 # 대각선의 길이
MAX_ANGLE_DIFF = 12.0 # 1번 tontour와 2번째 contour의 각도
MAX_AREA_DIFF = 0.5 # 면적의 차이
MAX_WIDTH_DIFF = 0.8 # 넓이의 차이
MAX_HEIGHT_DIFF = 0.2 # 높이의 차이
MIN_N_MATCHED = 3 # 위의 조건을 최소 3개 이상 만족

PLATE_WIDTH_PADDING = 1.3
PLATE_HEIGHT_PADDING = 1.5
MIN_PLATE_RATIO = 3
MAX_PLATE_RATIO = 10

oo = None

def preprocessing(car_no): # 원본 이미지에서 흐릿한 이미지의 검정과 흰색을 채워서 후보군 추출. 번호판 영역을 Crop하기 위한 함수.
    global oo
    image = cv2.imread("C:/study/KNN/ST/image/%01d.jpg" % car_no, cv2.IMREAD_COLOR) # 이미지를 호출
    # cv2.imshow("image", image)
    # cv2.waitKey()
    height, width, channel = image.shape # 높이, 넓이, 컬러
    # print("height=", height)
    # print("width=", width)
    # print("channel=", channel)
    if image is None: return None, None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 명암도 영상 변환 (색상 공간 변환)
    structuringElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    imgTopHat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, structuringElement)
    imgBlackHat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, structuringElement)
    # cv2.MORTH_ERODE = 침식
    # cv2.MORTH_DILATE = 팽창
    # cv2.MORTH_CLOSE = 닫기
    # cv2.MORTH_GRADIENT = 모폴로지 그래디언트 = 팽창, 침식

    imgGrayscalePlusTopHat = cv2.add(gray, imgTopHat)
    gray = cv2.subtract(imgGrayscalePlusTopHat, imgBlackHat)
    img_blurred = cv2.GaussianBlur(gray, ksize=(3, 3), sigmaX=0)
    img_thresh = cv2.adaptiveThreshold(
        img_blurred,
        maxValue=255.0,
        adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        thresholdType=cv2.THRESH_BINARY_INV,
        blockSize=19,
        C=9
    )
    
    # cv2.imshow("gray2", gray)
    # cv2.imwrite("gray2.jpg", gray)
    # cv2.waitKey()

    contours, _ = cv2.findContours(img_thresh, mode=cv2.RETR_TREE,
                                   method=cv2.CHAIN_APPROX_SIMPLE)

    temp_result = np.zeros((height, width, channel), dtype=np.uint8)
    cv2.drawContours(temp_result, contours=contours, contourIdx=-1,
                     color=(255, 255, 255))
    # cv2.imshow("zeros", temp_result)
    # cv2.waitKey()
    temp_result = np.zeros((height, width, channel), dtype=np.uint8)
    # cv2.imshow("temp_result", temp_result)
    # cv2.waitKey()
    contours_dict = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        rere = cv2.rectangle(temp_result, pt1=(x, y), pt2=(x + w, y + h),
                      color=(255, 255, 255), thickness=2)

        contours_dict.append({
            'contour': contour,
            'x': x,
            'y': y,
            'w': w,
            'h': h,
            'cx': x + (w / 2),
            'cy': y + (h / 2)
        })
    # cv2.imshow("temp_result", temp_result)
    # cv2.waitKey()
    possible_contours = []

    cnt = 0
    for d in contours_dict:
        area = d['w'] * d['h']
        ratio = d['w'] / d['h']

        if area > MIN_AREA \
                and d['w'] > MIN_WIDTH and d['h'] > MIN_HEIGHT \
                and MIN_RATIO < ratio < MAX_RATIO:
            d['idx'] = cnt
            cnt += 1
            possible_contours.append(d)

    temp_result = np.zeros((height, width, channel), dtype=np.uint8)

    for d in possible_contours:
        cv2.rectangle(temp_result, pt1=(d['x'], d['y']), pt2=(d['x'] + d['w'], d['y'] + d['h']),
                      color=(255, 255, 255), thickness=2)
    # cv2.imshow("temp_result2", temp_result)
    # cv2.waitKey()

    def find_chars(contour_list):
        
        matched_result_idx = []
        for d1 in contour_list:
            matched_contours_idx = []
            for d2 in contour_list:
                if d1['idx'] == d2['idx']:
                    continue

                dx = abs(d1['cx'] - d2['cx'])
                dy = abs(d1['cy'] - d2['cy'])

                diagonal_length1 = np.sqrt(d1['w'] ** 2 + d1['h'] ** 2)

                distance = np.linalg.norm(np.array([d1['cx'], d1['cy']]) - np.array([d2['cx'], d2['cy']]))
                if dx == 0:
                    angle_diff = 90
                else:
                    angle_diff = np.degrees(np.arctan(dy / dx))
                area_diff = abs(d1['w'] * d1['h'] - d2['w'] * d2['h']) / (d1['w'] * d1['h'])
                width_diff = abs(d1['w'] - d2['w']) / d1['w']
                height_diff = abs(d1['h'] - d2['h']) / d1['h']

                if distance < diagonal_length1 * MAX_DIAG_MULTIPLYER \
                        and angle_diff < MAX_ANGLE_DIFF and area_diff < MAX_AREA_DIFF \
                        and width_diff < MAX_WIDTH_DIFF and height_diff < MAX_HEIGHT_DIFF:
                    matched_contours_idx.append(d2['idx'])

            matched_contours_idx.append(d1['idx'])

            if len(matched_contours_idx) < MIN_N_MATCHED:
                continue

            matched_result_idx.append(matched_contours_idx)

            unmatched_contour_idx = []
            for d4 in contour_list:
                if d4['idx'] not in matched_contours_idx:
                    unmatched_contour_idx.append(d4['idx'])

            unmatched_contour = np.take(possible_contours,
                                        unmatched_contour_idx)

            recursive_contour_list = find_chars(unmatched_contour)

            for idx in recursive_contour_list:
                matched_result_idx.append(idx)
                print(matched_result_idx)

            break

        return matched_result_idx

    result_idx = find_chars(possible_contours)
    matched_result = []
    for idx_list in result_idx:
        matched_result.append(np.take(possible_contours, idx_list))

    temp_result = np.zeros((height, width, channel), dtype=np.uint8)
    # print("temp_result=", temp_result)
    # cv2.imshow("temp_result3-1", temp_result)
    # cv2.waitKey()
    for r in matched_result:
        for d in r:
            cv2.rectangle(temp_result, pt1=(d['x'], d['y']),
                          pt2=(d['x'] + d['w'], d['y'] + d['h']),
                          color=(255, 255, 255), thickness=1)


    # cv2.imshow("temp_result3", temp_result)
    # cv2.waitKey()
    plate_imgs = []
    plate_infos = []
    image_count = 2
    for i, matched_chars in enumerate(matched_result):

        sorted_chars = sorted(matched_chars, key=lambda x: x['cx'])

        plate_cx = (sorted_chars[0]['cx'] + sorted_chars[-1]['cx']) / 2
        plate_cy = (sorted_chars[0]['cy'] + sorted_chars[-1]['cy']) / 2

        plate_width = (sorted_chars[-1]['x'] + sorted_chars[-1]['w'] - sorted_chars[0]['x']) * PLATE_WIDTH_PADDING

        sum_height = 0
        sum_count = 0
        for d in sorted_chars:
            sum_height += d['h']
            sum_count += 1


        plate_height = int(sum_height / len(sorted_chars) * PLATE_HEIGHT_PADDING)
        triangle_height = sorted_chars[-1]['cy'] - sorted_chars[0]['cy']
        triangle_hypotenus = np.linalg.norm(
            np.array([sorted_chars[0]['cx'], sorted_chars[0]['cy']]) -
            np.array([sorted_chars[-1]['cx'], sorted_chars[-1]['cy']])
        )
        angle = np.degrees(np.arcsin(triangle_height / triangle_hypotenus))

        rotation_matrix = cv2.getRotationMatrix2D(center=(plate_cx, plate_cy), angle=angle, scale=1.0)

        img_rotated = cv2.warpAffine(img_thresh, M=rotation_matrix, dsize=(width, height))

        img_cropped = cv2.getRectSubPix(
            img_rotated,
            patchSize=(int(plate_width), int(plate_height)),
            center=(int(plate_cx), int(plate_cy))
        )
        if img_cropped.shape[1] / img_cropped.shape[0] < MIN_PLATE_RATIO or img_cropped.shape[1] / img_cropped.shape[0] < MIN_PLATE_RATIO > MAX_PLATE_RATIO:
            continue

        plate_imgs.append(img_cropped)        
        plate_infos.append({
            'x': int(plate_cx - plate_width / 2),
            'y': int(plate_cy - plate_height / 2),
            'w': int(plate_width),
            'h': int(plate_height)
            
        })

        img_cropped = 255-img_cropped
        # cv2.imshow("img_cropped", img_cropped)
        # cv2.waitKey()
        # img_cropped = 255-img_cropped
        if sum_count > 0:
            global oo
            # oo = str(car_no) + "_" + "%d.jpg" % image_count
            # oo = str(car_no) + "_" + str(image_count) + ".jpg"
            cv2.imwrite("C:/study/KNN/ST/image/"+ str(car_no) + "_" + "%d.jpg" % image_count, img_cropped)
            image_count += 1

        return cv2.resize(img_cropped, (144, 28))


def kNN_train(train_fname, K, nclass, nsample):
    size = (40, 40) # train_numbers.png 학습 이미지를 40 x 40으로 자름.
    train_img = cv2.imread(train_fname, cv2.IMREAD_GRAYSCALE)  
    # cv2.imshow("img_cropped", train_img)
    # cv2.waitKey()
    h, w = train_img.shape[:2] # 높이와 넓이를 알기 위한 메서드
    dy = h % size[1]// 2
    dx = w % size[0]// 2
    train_img = train_img[dy:h-dy-1, dx:w-dx-1] # 학습영상 여백 제거
    cv2.threshold(train_img, 32, 255, cv2.THRESH_BINARY, train_img) # 내가 정한 임계치 이상 255, 이하 0

    cells = [np.hsplit(row, nsample) for row in np.vsplit(train_img, nclass)]
    
    # for row in np.vsplit():
    #     cells=np.hsplit(row, nsample)
    
        
    nums = [find_number(c) for c in np.reshape(cells, (-1, 40,40))]
    trainData = np.array([place_middle(n, size) for n in nums])  
    labels = np.array([i for i in range(nclass) for j in range(nsample)], np.float32)
    #np.savetxt("./nnpp.txt", labels)
    knn = cv2.ml.KNearest_create()
    knn.train(trainData, cv2.ml.ROW_SAMPLE, labels)  
    return knn


def preprocessing_plate(plate_img):
    global oo
    plate_img = cv2.resize(plate_img, (180, 35))            
    flag = cv2.THRESH_BINARY | cv2.THRESH_OTSU              
    cv2.threshold(plate_img, 32, 255, flag, plate_img)      

    h, w = plate_img.shape[:2]
    dx, dy = (7, 3)
    ret_img= plate_img[dy:h-dy, dx:w-dx]                   
    # cv2.imshow("img_cropped", ret_img)
    # cv2.waitKey()
    oo = str(car_no) + "_" + "%d.jpg" 
    cv2.imwrite("C:/study/KNN/ST/image/" + str(car_no) + "_" + "%d.jpg", ret_img)
    cv2.imshow("ret_img", ret_img)
    return ret_img

def find_objects(sub_mat):
    global oo
    results = cv2.findContours(sub_mat, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # cv2.RETR_EXTERNAL 가장 외각을 찾음. cv2.CHAIN_APPROX_SIMPLE
    contours = results[0] if int(cv2.__version__[0]) >= 4 else results[1] # python 버전 체킹 현재는 python 3버전만 쓰기 때문에 contours = results 와 같음

    rois = [cv2.boundingRect(contour) for contour in contours] # 위 cv2.findContours()에서 찾은 외각의 좌표를 for문으로 돌림 그리고 boundinRect로 자름
    rois = [(x, y, w, h, w*h) for x,y,w,h in rois if w / h < 2.5] # rois에서 잘린 이미지의 x, y, w, h 로 받고, 만약 w / h < 2.5 보다 작으면 w*h를 하겠금 되어 있음

    text_rois = [(x, y, x+w, y+h) for x, y, w, h, a in rois if 45 < x < 80 and a > 60] # 문자검출을 위한 코드 단 현재 3자리수 번호판은 인식안됨
    num_rois  = [(x, y, w, h) for x, y, w, h, a in rois  if not(45 < x < 80) and a > 150] # 숫자검출을 위한 코드 

    if text_rois:                      # 분리된 문자 영역 누적
       
        pts= np.sort(text_rois, axis=0) # Y 방향 정렬
        
        x0, y0 = pts[ 0, 0:2] # 시작좌표 중 최대인 x, y 좌표                 
        x1, y1 = pts[-1, 2:] # 종료좌표 중 최대인 x, y 좌표        
        w, h = x1-x0, y1-y0 # 너비, 높이 계산
        num_rois.append((x0, y0, w, h)) # 문자 영역 구성 및 저장
        iwcount = 0
        # print(num_rois)
        for num_roiss in num_rois:
            #print(num_roiss)
            image = cv2.imread("C:/study/KNN/ST/image/" + str(oo), cv2.IMREAD_ANYDEPTH)
            print(image)
            # print("image=", image)
            # cv2.imshow("image", image)
            # cv2.waitKey()
            start_x = num_roiss[0]
            start_y = num_roiss[1]
            end_x = num_roiss[0] + num_roiss[2]
            end_y = num_roiss[1] + num_roiss[3]
            cropped_image = image[start_y:end_y, start_x:end_x]
            cv2.imwrite("C:/study/KNN/ST/image/"+str(iwcount)+".jpg", cropped_image)
            cv2.imshow("C:/study/KNN/ST/image/"+str(iwcount)+".jpg", cropped_image)
            # cv2.waitKey()
            iwcount += 1
    return num_rois

def classify_numbers(cells, nknn, tknn, K1, K2, object_rois):
    if len(cells) < 4:
        print("검출된 숫자(문자)가 7개가 아닙니다.")
        return

    texts  = "가나다라마거너더러머버서어저고노도로모보" \
             "소오조구누두루무부수우주아바사자바하허호"

    numbers = [find_number(cell) for cell in cells]
    datas = [place_middle(num, (40,40)) for num in numbers]
    datas = np.reshape(datas, (len(datas), -1))
    idx = np.argsort(object_rois, axis=0).T[0]
    text = datas[idx[2]].reshape(1,-1)

    _, resp1, _, _ = nknn.findNearest(datas, K1)  

    _, [[resp2]], _, _ = tknn.findNearest(text, K2)  

    resp1 = resp1.flatten().astype('int')
    results = resp1[idx].astype(str)
    results[2] = texts[int(resp2)]

    return results
##############START#############
while True:
    car_no = int(input("자동차 영상 번호 (0~20): ")) #입력 받을 때 까지 input을 기다림.
    
    candidate_imgs = preprocessing(car_no) #preprocessing에 위에서 입력 받은 input 함수의 값을 인자로 전달. 그리고 함수 호출이 끝나면
                                           #candidate_imgs에 값을 넣어 주는 것으로 보아 return 값이 있다고 판단함..
    
    K1, K2 = 10, 10

    nknn = kNN_train("C:/study/KNN/ST/image/train_numbers.png", K1, 10, 20) 

    tknn = kNN_train("C:/study/KNN/ST/image/train_texts.png", K2, 40, 20)  

    plate_img = preprocessing_plate(candidate_imgs)   

    cells_roi = find_objects(cv2.bitwise_not(plate_img))
    cells = [plate_img[y:y+h, x:x+w] for x,y,w,h in cells_roi]
    carnumber = classify_numbers(cells, nknn, tknn, K1, K2, cells_roi)      
    car = ''.join(carnumber)
    tm = (datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f'))
    car = tm + "_" + car + '.jpg'
    file_oldname = os.path.join("C:\\study\\KNN\ST\\car", str(car_no) + '.jpg')
    os.rename(file_oldname, car)

# for car_no in range(74, 75, 1):
#     candidate_imgs = preprocessing(car_no)
    
#     K1, K2 = 10, 10

#     nknn = kNN_train("C:/study/KNN/ST/image/train_numbers.png", K1, 10, 20) 

#     tknn = kNN_train("C:/study/KNN/ST/image/train_texts.png", K2, 40, 20)  

#     plate_img = preprocessing_plate(candidate_imgs)   

#     cells_roi = find_objects(cv2.bitwise_not(plate_img))
#     cells = [plate_img[y:y+h, x:x+w] for x,y,w,h in cells_roi]
#     carnumber = classify_numbers(cells, nknn, tknn, K1, K2, cells_roi)      
#     car = ''.join(carnumber)
#     tm = (datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f'))
#     car = tm + "_" + car + '.jpg'
#     file_oldname = os.path.join("C:\\study\\KNN\ST\\car", str(car_no) + '.jpg')
#     os.rename(file_oldname, car)


    