import tensorflow as tf

hello = tf.constant('Hello, Tensorflow world')
sess = tf.Session()

print(sess.run(hello))