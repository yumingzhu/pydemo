import  tensorflow as tf


# 给定type  ,tf 大部分只能处理float 32数据
input1=tf.placeholder(tf.float32)
input2=tf.placeholder(tf.float32)

#tensorflow 1.0 修改版
output=tf.multiply(input1,input2)

with tf.Session() as sess:
    # placeholder 在sess.run() 的时候传入值
    print(sess.run(output,feed_dict={input1:[7.0],input2:[2.0]}))



