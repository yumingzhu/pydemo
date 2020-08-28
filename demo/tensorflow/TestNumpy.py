import  numpy as np

# x_data = np.float32(np.random.rand(2, 100)) # 随机输入
# y_data = np.dot([0.100, 0.200], x_data) + 0.300
# print(x_data)
# # print(y_data)
#得到一个二维数组, 其中 包含2个数组, 每个数组 3个元素
# x_data=np.random.rand(2,3)
#dot 求积, 每个x_data 乘之后,再相加
# y=np.dot([0.100,0.200],x_data)

# 定义一个二维数组 ， 里面一共有300,个数， 分别从，-1,到1
x_data=np.linspace(-1,1,300)[:,np.newaxis]
# print(x_data)
# 加噪音，， 均值为0，  方差为0.05，大小何x_data产不多
noise=np.random.normal(0,0.05,x_data.shape)
#print(noise)
#对 x 进行平方
y_data=np.square(x_data)-0.5+noise
print(y_data)






