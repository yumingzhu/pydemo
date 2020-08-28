import cv2
import numpy as  np
from matplotlib import pyplot as plt


def getExecute_Time():
    img1 = cv2.imread("G:/mywork/openwork/timg.jpg")
    e1 = cv2.getTickCount()
    for i in range(5, 49, 2):
        img1 = cv2.medianBlur(img1, i)
    e2 = cv2.getTickCount()
    t = (e2 - e1) / cv2.getTickFrequency()
    print(t)


# 图像平滑操作，
def filter2D_demo():
    img = cv2.imread("G:/mywork/openwork/opencv-4.1.0/samples/data/opencv-logo.png")
    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv2.filter2D(img, -1, kernel)
    plt.subplot(121), plt.imshow(img), plt.title("Original")
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title("AVeraging")
    plt.xticks([]), plt.yticks([])
    plt.show()


def blur_demo():
    img = cv2.imread("G:/mywork/openwork/opencv-4.1.0/samples/data/opencv-logo.png")
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()


def erode_demo():  # 腐蚀
    img = cv2.imread('G:/mywork/openwork/opencv-4.1.0/samples/data/j.png')
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=1)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(erosion), plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()


def dilate_demo():  # 膨胀
    img = cv2.imread('G:/mywork/openwork/opencv-4.1.0/samples/data/j.png')
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.dilate(img, kernel, iterations=1)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(erosion), plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()


def morphologyEx_demo():
    img = cv2.imread('G:/mywork/openwork/opencv-4.1.0/samples/data/j.png')
    kernel = np.ones((5, 5), np.uint8)
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    # gradient = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(gradient), plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()


def sobel_demo():
    img = cv2.imread('G:/mywork/openwork/opencv-4.1.0/samples/data/sudoku.png')
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()


def canny_demo():  # canny 边界检测
    img = cv2.imread("G:/mywork/openwork/opencv-4.1.0/samples/data/messi5.jpg")
    edges = cv2.Canny(img, 200, 100)
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()


def drawContour_demo():
    img = cv2.imread('G:/mywork/openwork/opencv-4.1.0/samples/data/test.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色转灰度
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)  # 进行二值化
    # 输入图片 ，轮廓检索模式， 轮廓近似的方法
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #  返回结果的类型，     轮廓的点集合， 轮廓层析集合
    # 检索模式为树形cv2.RETR_TREE，
    # 轮廓存储模式为简单模式cv2.CHAIN_APPROX_SIMPLE，如果设置为 cv2.CHAIN_APPROX_NONE，所有的边界点都会被存储。
    # 参数，  原始图片，  图片轮廓集合，  ， 轮廓的色彩， 轮廓的粗细
    img = cv2.drawContours(img, contours, -1, (0, 255, 255), 3)  # 此时是将轮廓绘制到了原始图像上
    # 第三个参数是轮廓的索引（在绘制独立轮廓是很有用，当设置为 -1 时绘制所有轮廓）。接下来的参数是轮廓的颜色和厚度等
    cv2.imshow('img', img)  # 显示原始图像
    cv2.waitKey()  # 窗口等待按键，无此代码，窗口闪一下就消失


def moments_demo():
    img = cv2.imread('G:/mywork/openwork/opencv-4.1.0/samples/data/test.jpg', 0)
    # imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色转灰度
    ret, thresh = cv2.threshold(img, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    print(ret)
    cnt = contours[0]
    M = cv2.moments(cnt)
    print(M)


def getimg_demo():
    img = cv2.imread('G:/mywork/openwork/opencv-4.1.0/samples/data/test.jpg', 0)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def calcHist():
    img = cv2.imread("G:/mywork/openwork/opencv-4.1.0/samples/data/messi5.jpg")
    plt.hist(img.ravel(), 256, [0, 256]);
    plt.show()


def calcHist_demo2():
    img = cv2.imread("G:/mywork/openwork/opencv-4.1.0/samples/data/messi5.jpg")
    color = ('b', 'g', 'r')
    # 对一个列表或数组既要遍历索引又要遍历元素时
    # 使用内置 enumerrate 函数会有更加直接，优美的做法
    # enumerate 会将数组或列表组成一个索引序列。
    # 使我们再获取索引和索引内容的时候更加方便
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
    plt.show()


def matchTemplate_demo():
    img = cv2.imread("G:/mywork/openwork/opencv-4.1.0/samples/data/messi5.jpg")
    img2 = img.copy()
    template = cv2.imread("G:/mywork/openwork/opencv-4.1.0/samples/data/messi_face.jpg", 0)
    w, h = template.shape[::-1]
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    for meth in methods:
        img = img2.copy()
        # exec 语句用来执行储存在字符串或文件中的 Python 语句。
        # 例如，我们可以在运行时生成一个包含 Python 代码的字符串，然后使用 exec 语句执行这些语句。
        # eval 语句用来计算存储在字符串中的有效 Python 表达式
        method = eval(meth)
        # Apply template Matching
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # 使用不同的比较方法，对结果的解释不同
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img, top_left, bottom_right, 255, 2)
        plt.subplot(121), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        plt.show()


def img_resize_demo():
    img = cv2.imread("G:/mywork/openwork/opencv-4.1.0/samples/data/messi5.jpg")
    h, w, m = img.shape
    dsth = int(h * 0.5)
    dstw = int(w * 0.5)
    dst = cv2.resize(img, (dstw, dsth))
    cv2.imshow("image", dst)
    cv2.imshow("image2", img)
    cv2.waitKey(0)


def vider_split():
    cap = cv2.VideoCapture("G:/mywork/openwork/sourcedemo/3-4机器学习/1.mp4")
    isOpened = cap.isOpened()
    print(cap.isOpened())
    fps = cap.get(cv2.CAP_PROP_FPS)  # 帧率
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # w   h
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(fps, width, height)
    i = 0;
    while (isOpened):
        if i == 10:
            break
        else:
            i = i + 1
        flag, frame = cap.read()  # 读取每一张张 flag   frame
        fileName = "image" + str(i) + ".jpg"
        print(fileName)
        if flag == True:
            cv2.imwrite(fileName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
    print("end")


def bilateeralFilter_demo():
    img = cv2.imread("G:/mywork/openwork/opencv-4.1.0/samples/data/1.png")
    cv2.imshow("src", img)
    dst = cv2.bilateralFilter(img, 15, 35, 35)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def video_merge():
    img = cv2.imread("G:/mywork/openwork/opencv-4.1.0/samples/data/image1.jpg")
    imgInfo = img.shape
    size = (imgInfo[0], imgInfo[1])
    print(size)
    # 文件名称， 编码器， 帧率  ，  大小
    videoWriter = cv2.VideoWriter("3.avi",  cv2.VideoWriter_fourcc('I', '4', '2', '0'), 5, size)
    for i in range(1, 11):
        fileName = 'G:/mywork/openwork/opencv-4.1.0/samples/data/image' + str(i) + ".jpg"
        img = cv2.imread(fileName)
        videoWriter.write(img)
    #这个很重要， 如果没有这个的话， 视频还是被操作的， 回打不开视频，
    videoWriter.release()
def   face_demo():
    face_xml = cv2.CascadeClassifier('G:/mywork/openwork/opencv-4.1.0/samples/data/haarcascade_frontalface_default.xml')
    eye_xml = cv2.CascadeClassifier('G:/mywork/openwork/opencv-4.1.0/samples/data/haarcascade_eye.xml')
    img=cv2.imread("G:/mywork/openwork/opencv-4.1.0/samples/data/jt.jpg")
    cv2.imshow("src",img)
    gary=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_xml.detectMultiScale(gary,1.3,5)
    print("face=",len(faces))
    print(faces)
    #down
    for  (x,y,w,h)  in faces:# x，y 为脸部的左上方的点，     （w,h） 为当前脸的宽高
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_face=gary[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
    cv2.imshow('dst', img)
    cv2.waitKey(0)
def  svm_demo():
    # 1 准备data
    rand1 = np.array([[155, 48], [159, 50], [164, 53], [168, 56], [172, 60]])
    rand2 = np.array([[152, 53], [156, 55], [160, 56], [172, 64], [176, 65]])
    # 2 label
    label = np.array([[0], [0], [0], [0], [0], [1], [1], [1], [1], [1]])
    # 3 data
    data=np.vstack((rand1,rand2))
    data=np.array(data,dtype='float32')
    #训练
    svm=cv2.ml.SVM_create()
    # 属性设置
    svm.setType(cv2.ml.SVM_C_SVC)
    svm.setKernel(cv2.ml.SVM_LINEAR)
    svm.setC(0.01)
    # 训练
    result=svm.train(data,cv2.ml.ROW_SAMPLE,label)
    pt_data=np.vstack([[167,55],[162,57]])
    pt_data=np.array(pt_data,dtype='float32')
    (par1,par2)=svm.predict(pt_data)
    print(par2)
if __name__ == '__main__':
    svm_demo()
