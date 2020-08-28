import  numpy as np
import  cv2
from   matplotlib  import   pyplot  as plt

img =cv2.imread("G:/mywork/openwork/timg.jfif",0)
plt.imshow(img,cmap="gray",interpolation="bicubic")
plt.xticks([100])
plt.ylabel([100])
plt.show()