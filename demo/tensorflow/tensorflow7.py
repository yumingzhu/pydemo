import  tensorflow as tf
import  numpy as np
import matplotlib.pylab as plt
def  add_layer(inputs,in_site,out_size,activation_function=None):
    # Weights是个矩阵，[行，列]为[in_size,out_size]
    Weights=tf.Variable(tf.random_normal([in_site,out_size])) #正态分布
    biases=tf.Variable(tf.zeros([1,out_size])+0.1)
    # Weights*x+b的初始值， 也就是未激活的值
    wx_plus_b=tf.matmul(inputs,Weights)+biases;

    # 激活
    if activation_function is None:
        outputs=wx_plus_b
    else:
        outputs=activation_function(wx_plus_b)
    return outputs


"""定义数据形式"""
#  (-1,1) 之间， 有300个单位， 后面的是维度，   x_data 是有300 行  （300个例子）
x_data=np.linspace(-1,1,300)[:,np.newaxis]
# 加噪声,均值为0，方差为0.05，大小和x_data一样
noise=np.random.normal(0,0.05,x_data.shape)
y_data=np.square(x_data)-0.5+noise

xs=tf.placeholder(tf.float32,[None,1])
ys=tf.placeholder(tf.float32,[None,1])
"""建立网络"""
# 定义隐藏层， 输入一个节点， 输出10个节点
li=add_layer(xs,1,10,activation_function=tf.nn.relu)
# 定义输出层
prediction=add_layer(li,10,1,activation_function=None)

"""预测"""
loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))

"""训练"""
#优化算法， minimize(loss) 以0.1 的学习效率 对loss 进行减小
train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
        if  i%50==0:
            # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
            print(sess.run(prediction,feed_dict={xs:x_data,ys:y_data}))
