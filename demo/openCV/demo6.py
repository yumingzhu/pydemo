import  cv2
import  numpy as np
img =cv2.imread("G:/mywork/openwork/timg.jfif")
px=img[100,100]
# 获取当前 像素坐标的，  颜色 组成
print(px)
# 获取像素 当前位置 指定类型的,   0 , 1  , 2
blue=img[100,100,1]
print(blue)

