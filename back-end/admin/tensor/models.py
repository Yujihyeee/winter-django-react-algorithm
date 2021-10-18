import numpy as np
import tensorflow as tf


class Perceptron(object):
    def __init__(self):
        pass


class Calculator(object):

    def __init__(self):
        print(f'TensorFlow Version: {tf.__version__}')

    def process(self):
        self.plus(4, 8)
        print('*' * 100)
        self.mean()

    def plus(self, a, b):
        print(tf.constant(a) + tf.constant(b))

    def mean(self):
        x_array = np.arange(18).reshape(3, 2, 3)
        x2 = tf.reshape(x_array, shape=(-1, 6))
        # 각 열의 합
        xsum = tf.reduce_sum(x2, axis=0)
        # 각 열의 평균
        xmean = tf.reduce_mean(x2, axis=0)

        print(f'입력 크기: {x_array.shape} \n')
        print(f'크기가 변경된 입력 크기: {x2.numpy()} \n')
        print(f'열의 합: {xsum.numpy()} \n')
        print(f'열의 평균: {xmean.numpy()} \n')
