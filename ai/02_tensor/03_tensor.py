# WARNING:tensorflow:From 02_tensor.py:13: The name tf.Session is deprecated. Please use tf.compat.v1.Session instead.
# 이게 보기 싫으면 이렇게 import
import tensorflow.compat.v1 as tf


# placeholder : 그래프를 실행하는 시점에 데이터를 입력받을 수 있도록 공간만 만들어 놓음
node1 = tf.placeholder(dtype=tf.float32)
node2 = tf.placeholder(dtype=tf.float32)

node3 = node1 + node2


sess = tf.Session()

# data 입력해주면서 실행
X = [10, 20, 30]
y = [40, 50, 60]


# 여기가 그래프를 실행하는 시점으로, feed_dict를 사용해 데이터를 입력해줌
print(sess.run(node3, feed_dict={node1:X,node2:y}))