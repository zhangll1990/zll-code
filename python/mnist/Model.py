import  tensorflow  as tf

#Y=W*x + b
def regression(x):
    w = tf.Variable(tf.zeros([784,10],name='w'))
    b = tf.Variable(tf.zeros([10],name='b'))
    y = tf.nn.softmax(tf.matmul(x,w) + b)
    return y, [w,b]
