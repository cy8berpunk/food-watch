import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import to_categorical
from matplotlib import pyplot

from data_proc import data

def simple_rnn(x, y, batch_size):
	model = Sequential()
	model.add(LSTM(100, batch_size=batch_size, input_shape=(batch_size,x.shape[2])))
	model.add(Dropout(0.5))
	model.add(Dense(100, activation='relu'))
	model.add(Dense(2, activation='softmax'))
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

	return model

def train(filepath, batch_size, epochs):
	x_train, x_test, y_train, y_test = data.load_data(filepath)

	model = simple_rnn(x_train, y_train, batch_size)

	model.fit_generator(data.data_batch_generator(filepath, batch_size, x_train, y_train), steps_per_epoch=len(x_train), epochs=epochs)

	_, accuracy = model.evaluate(test_x, test_y)

	return accuracy

def main():

	train("data/test_data.csv", 50, 10)

if __name__ == '__main__':
    main()
