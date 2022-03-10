import tensorflow as tf


# 1. 데이터 준비
# X_data : 3번의 쪽지시험 결과 / y_data : 실제 평가 결과
X_data = [
    [73, 80, 75],
    [93, 88, 93],
    [89, 91, 90],
    [96, 89, 100],
    [73, 66, 70]
]

y_data = [
    [80],
    [91],
    [88],
    [94],
    [61]
]

# shape = [5, 3] -> 5개 리스트 안에 3개의 요소
# shape이 None : 갯수 상관 없다는 뜻
X = tf.placeholder(shape=[None,3], dtype=tf.float32)
y = tf.placeholder(shape=[None,1], dtype=tf.float32)



# 2. 가설 설정
# [3, 1] -> X와 행렬연산 해야 하기 때문에!!
W = tf.Variable(tf.random_normal([3,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# H = W * X  + b
H = tf.matmul(X, W) + b



# 3. 준비
# loss function
loss = tf.reduce_mean(tf.square(H - y))

# optimizer
learning_rate = 0.00004
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)

# session
sess = tf.Session()
# 변수 초기화
sess.run(tf.global_variables_initializer())



# 4. 학습
epochs = 10000
for step in range(epochs):
    _, loss_val, W_val, b_val = sess.run([train, loss, W, b], feed_dict={X:X_data, y:y_data})
    if step % 1000 == 0:
        print(f'W:{W_val} \t b:{b_val} \t loss:{loss_val}')




# 5. 예측 및 평가
print(sess.run(H, feed_dict={X:[[100, 80, 87]]}))