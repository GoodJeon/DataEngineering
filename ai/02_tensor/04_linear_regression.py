import tensorflow as tf



# 1. 데이터 준비
X = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# 2. 가설 설정
# H(hypothesis) = W (weight) * X + b (bias)
# tf.random_normal : random으로 표준분포 값 설정
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')


H = W * X +  b



# 3. 준비
# loss function
# Mean Square Error
loss = tf.reduce_mean(tf.square(H - y))

# optimizer
# 경사 하강법 (gradient descent) : loss가 최소화 되는 값을 찾기
# 0.01 = learning rate
optimizer = tf.train.GradientDescentOptimizer(0.01)
# loss가 최소화 되도록
train = optimizer.minimize(loss)


# session
sess = tf.Session()

# 변수 초기화
sess.run(tf.global_variables_initializer())



# 4. 학습
# 학습 횟수
epochs = 5000
for step in range(epochs):
    tmp, loss_val, W_val, b_val = sess.run([train, loss, W, b], feed_dict={X:[1,2,3,4,5],y:[3,5,7,9,11]})
    if step % 1000 == 0:
        print(f'W:{W_val} \t b:{b_val} \t loss:{loss_val}')


# 5. 예측
print(sess.run(H, feed_dict={X:[10,11,12,13,14]}))