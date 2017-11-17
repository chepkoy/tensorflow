import tensorflow as tf


# Tensors for the graph
a = tf.constant(6, name='constant_a')
b = tf.constant(3, name='constant_b')
c = tf.constant(10, name='constant_c')
d = tf.constant(5, name='constant_d')

#Nodes and operations of the graph
mul = tf.multiply(a,b, name="mul")
div = tf.div(c, d, name="div")
addn = tf.add_n([mul, div], name="addn")

sess = tf.Session()

print(sess.run(addn))

# Directory for the events
writer = tf.summary.FileWriter('./events', sess.graph)
writer.close()
sess.close()


