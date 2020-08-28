import base64

from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = '16030606'
API_KEY = '6QPiH6xxxeboptfPhnr2ZDkA'
SECRET_KEY = 'ZBX9GOQFQuCaVYzLHNX3TIK9doBrVvSa'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


def  detect_demo():
    image = "G:/mywork/openwork/opencv-4.1.0/samples/data/jt.jpg"
    f = open(image, 'rb')
    image = base64.b64encode(f.read())
    image64 = str(image, 'utf-8')
    imageType = "BASE64"
    """ 如果有可选参数 """
    options = {}
    options["max_face_num"] = 5
    options["face_field"] = "age,beauty"

    # """ 调用人脸检测 """
    # client.detect(image, imageType);
    print(client.detect(image64, imageType,options));
def  search_demo():
    image = "G:/mywork/openwork/opencv-4.1.0/samples/data/hg.jpg"
    f = open(image, 'rb')
    image = base64.b64encode(f.read())
    image64 = str(image, 'utf-8')
    imageType = "BASE64"
    groupIdList = "1"
    """ 调用人脸搜索 """
    result=client.search(image64, imageType, groupIdList);
    print(result)
# """ 如果有可选参数 """
# options = {}
# options["face_field"] = "age"
# options["max_face_num"] = 2
# options["face_type"] = "LIVE"
#
# """ 带参数调用人脸检测 """
# client.detect(image, imageType, options)
def   addUser():
    image = "G:/mywork/openwork/opencv-4.1.0/samples/data/lena.jpg"
    f = open(image, 'rb')
    image = base64.b64encode(f.read())
    image64 = str(image, 'utf-8')
    imageType = "BASE64"
    groupId = "1"
    userId = "123456789"
    """ 调用人脸注册 """
    result=client.addUser(image64, imageType, groupId, userId);
    print(result)
def  getUser():
    groupId = "1"
    userId = "123456789"
    """ 调用用户信息查询 """
    result=client.getUser(userId, groupId);
    print(result)
def  faceGetlist():
    groupId = "1"
    userId = "123456789"
    """ 调用获取用户人脸列表 """
    result=client.faceGetlist(userId, groupId);
    print(result)
if __name__ == '__main__':
    detect_demo()
