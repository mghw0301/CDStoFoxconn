import csv
import cv2
import os
import numpy as np

FOLDER = 'E:\\tf_models_hw\\supernova_dataset\\'#图片路径
CSV_FILE = 'train.csv'#用于获取图片信息

with open(CSV_FILE, 'r') as fid:
    print('Checking file:', CSV_FILE, 'in folder:', FOLDER)

    file = csv.reader(fid, delimiter=',')
    first = True

    cnt = 0
    error_cnt = 0
    error = False
    for row in file:
        if error == True:
            error_cnt += 1
            error = False

        if first == True:
            first = False
            continue

        cnt += 1

        name, width, height, xmin, ymin, xmax, ymax = row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(
            row[5]), int(row[6])
        """
        #如果不知道图片真实尺寸，需要根据如下代码获取
        path = os.path.join(FOLDER, name+'.jpg')
        img = cv2.imread(path)

        if type(img) == type(None):
            error = True
            print('Could not read image', img)
            continue
        org_height, org_width = img.shape[:2]

        """

        org_height, org_width = height,width
        if org_width != width:
            error = True
            print('Width mismatch for image: ', name, width, '!=', org_width)

        if org_height != height:
            error = True
            print('Height mismatch for image: ', name, height, '!=', org_height)

        if xmin > org_width:
            error = True
            print(xmin,org_width)
            print('XMIN > org_width for file', name)

        if xmax > org_width:
            error = True
            print('XMAX > org_width for file', name)

        if ymin > org_height:
            error = True
            print('YMIN > org_height for file', name)

        if ymax > org_height:
            error = True
            print('YMAX > org_height for file', name)

        if error == True:
            print('Error for file: %s' % name)
            print()

    print('Checked %d files and realized %d errors' % (cnt, error_cnt))