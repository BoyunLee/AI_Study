import numpy as np
import cv2

def resize20(digitImg):
    img = cv2.imread(digitImg)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret = cv2.resize(gray, (20, 20), fx=1, fy=1, interpolation=cv2.INTER_AREA)
    
    ret, thr = cv2.threshold(ret, 127, 255, cv2.THRESH_BINARY_INV)
    
    cv2.imshow('ret', thr)
    
    return thr.reshape(-1, 400).astype(np.float32)
    
def learningDigit():
    img = cv2.imread('images/digits.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
    x = np.array(cells)
    
    train = x[:, :].reshape(-1, 400).astype(np.float32)
    
    k = np.arange(10)
    train_labels = np.repeat(k, 500)[:, np.newaxis]
    
    np.savez('D:\\Development\\bugyungde\ML\\default\\digits_for_ocr.npz', train=train, train_labels=train_labels)
    print('data saved')
    
def loadLearningDigit(ocrdata):
    with np.load(ocrdata) as f:
        traindata = f['train']
        traindata_labels = f['train_labels']
        
    return traindata, traindata_labels

def OCR_for_Digits(test, traindata, traindata_labels):
    knn = cv2.ml.KNearest_create()
    knn.train(traindata, cv2.ml.ROW_SAMPLE, traindata_labels)
    ret, result, neighbors, dist = knn.findNearest(test, k=5)
    
    return result
    
def main():
    #learningDigit() #이미지 학습할때 주석제거
    #return
    ocrdata = 'digits_for_ocr.npz'
    traindata, traindata_labels = loadLearningDigit(ocrdata)
    digits = ['images/' + str(x) + '.png' for x in range(6)]
    
    print(traindata.shape)
    print(traindata_labels.shape)
    
    savenpz = False
    for digit in digits:
        test = resize20(digit)
        result = OCR_for_Digits(test, traindata, traindata_labels)
        
        print(result)
        
        k = cv2.waitKey(0)
        if k > 47 and k < 58:
            savenpz = True
            traindata = np.append(traindata, test, axis=0)
            new_label = np.array(int(chr(k))).reshape(-1, 1)
            traindata_labels = np.append(traindata_labels, new_label, axis=0)
            
    cv2.destroyAllWindows()
    if savenpz:
        np.savez('digits_for_ocr.npz', train=traindata, train_labels=traindata_labels)
        
main()


################################################################################################

# #-*- coding: utf-8 -*-
# import cv2
# import numpy as np
# import glob
# import sys

# FNAME = 'digits.npz'

# def machineLearning():
#     img = cv2.imread('images/digits.png')
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
#     x = np.array(cells)
#     train = x[:,:].reshape(-1,400).astype(np.float32)

#     k = np.arange(10)
#     train_labels = np.repeat(k,500)[:,np.newaxis]

#     np.savez(FNAME,train=train,train_labels = train_labels)

# def resize20(pimg):
#     img = cv2.imread(pimg)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     grayResize = cv2.resize(gray,(20,20))
#     ret, thresh = cv2.threshold(grayResize, 125, 255,cv2.THRESH_BINARY_INV)

#     cv2.imshow('num',thresh)
#     return thresh.reshape(-1,400).astype(np.float32)

# def loadTrainData(fname):
#     with np.load(fname) as data:
#         train = data['train']
#         train_labels = data['train_labels']

#     return train, train_labels

# def checkDigit(test, train, train_labels):
#     knn = cv2.ml.KNearest_create()
#     knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

#     ret, result, neighbours, dist = knn.findNearest(test, k=5)

#     return result

# if __name__ == '__main__':
#     if len(sys.argv) == 1:
#         print ('option : train or test')
#         exit(1)
#     elif sys.argv[1] == 'train':
#         machineLearning()
#     elif sys.argv[1] == 'test':
#         train, train_labels = loadTrainData(FNAME)

#         saveNpz = False
#         for fname in glob.glob('images/num*.png'):
#             test = resize20(fname)
#             result = checkDigit(test, train, train_labels)

#             print( result )

#             k = cv2.waitKey(0)

#             if k > 47 and k<58:
#                 saveNpz = True
#                 train = np.append(train, test, axis=0)
#                 newLabel = np.array(int(chr(k))).reshape(-1,1)
#                 train_labels = np.append(train_labels, newLabel,axis=0)


#         cv2.destroyAllWindows()
#         if saveNpz:
#             np.savez(FNAME,train=train, train_labels=train_labels)
#     else:
#         print ('unknow option')

#####################################################################

