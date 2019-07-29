# coding:utf-8
import numpy as np
import cv2
import time
 
fps = 10.0 #帧率
fourcc = cv2.VideoWriter_fourcc('M','J','P','G') #视频编码器
size = (1280,720) #视频分辨率,与原始图片保持一致,或者将图片皆resize到訪分辨率
out = cv2.VideoWriter('output.avi', fourcc, fps, size) #定义输出文件及其它参数
 
for i in range(1,20):
    n = str(i).zfill(2)
    image_file="/home/apollo/Desktop/0000/{0}.jpg".format(n)
    frame = cv2.imread(image_file)
    cv2.imshow("out",frame)
    out.write(frame)
 
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
 
 
out.release()
cv2.destroyAllWindows()
