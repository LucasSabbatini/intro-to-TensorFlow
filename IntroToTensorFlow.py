import tensorflow as tf

hello_constant = tf.constant('Hello, world!')

with tf.Session() as sess:
	output = sess.run(hello_constant)
	print(output)

# Tensor is the object in which data is stored in tensorflow, and they come in a variaety of sizes

A = tf.constant(1234)
# A is a 0 dimensional int32 tensor

B = tf.constant([123, 456, 789])
# B is a 1 dimensional int32 tensor

C = tf.constant([ [123], [456] ])
# C is a 2 dimensional int32 tensor

# tensor tf.constant() is called constant because its vallue never changes

