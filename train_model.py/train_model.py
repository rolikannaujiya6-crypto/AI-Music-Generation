import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Sample notes
notes = [56,60,63,63,60,67,70,67,63,63,56,67,61,56,65,68,56,61,67,56]

sequence_length = 5

X = []
y = []

for i in range(len(notes) - sequence_length):
    X.append(notes[i:i+sequence_length])
    y.append(notes[i+sequence_length])

X = np.array(X)
y = np.array(y)

X = X.reshape((X.shape[0], X.shape[1], 1))

model = Sequential()
model.add(LSTM(128, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')

model.fit(X, y, epochs=20, batch_size=8)

model.save("music_model.h5")

print("Model trained successfully!")