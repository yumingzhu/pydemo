import  cv2
import  numpy as np
img =cv2.imread("G:/mywork/openwork/timg.jfif")
#通过item 更加方便的操作 像素点
print(img.item(10,10,2))
img.itemset((10,10,2),100)
print(img.item(10,10,2))
# 打印但却图片的维度  (768, 1000, 3)     宽高，颜色的类型
print(img.shape)

# 获取图片区域范围的信息， 并且移动它的位置,  img[高,宽]
# ball=img[160:260,300:400]
# img[160:260,450:550]=ball
# img=cv2.imshow("test",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#使用numpy索引， 对图片中索引蓝色部分赋值为0
img[:,:,0]=0
cv2.imshow("xx",img)
cv2.waitKey(0)
cv2.destroyAllWindows()