import  cv2
import  numpy as np
img =cv2.imread("G:/mywork/openwork/timg.jfif",0)
cv2.imshow("image",img)
code=cv2.waitKey(0)&0xFF
if code==27:
    cv2.destroyAllWindows()
elif  code== ord('s'):
    cv2.imwrite("G:/mywork/openwork/xxx.jpg",img)
    cv2.destroyAllWindows()

print(code)