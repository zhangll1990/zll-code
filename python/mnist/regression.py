import os
import sys
print sys.path
import test
import tensorflow as tf
import Model
data = test.read_data_sets('MNIST-data',one_hot=True)

#create model
with tf.variable_scope("regression"):
    x = tf.placeholder(tf.float32,[None,784])
    y , variables = Model.regression(x)

#training
y_ = tf.placeholder("float",[None,10])
cross_entcopy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entcopy)
corrent_prediction = tf.equal(tf.arg_max(y,1),tf.arg_max(y_,1))
accuracy = tf.reduce_mean(tf.cast(corrent_prediction,tf.float32))

save = tf.train.Saver(variables)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in  range(1000):
        batch_xs,batch_ys = data.train.next_batch(100)
        sess.run(train_step,feed_dict={x:batch_xs,y_ :batch_ys})
    print((sess.run(accuracy,feed_dict={x:data.test.images,y_:data.test.labels})))
    path = save.save(sess,os.path.join(os.path.dirname(__file__),'data','regression.ckpt'),write_meta_graph=False,write_state=False)
    print("Saved",path)