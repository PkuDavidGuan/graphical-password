from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import numpy as np
from sklearn.model_selection import train_test_split


def modelText(dataSize, epochNum):
    ret = 0
    for i in range(0, 10):
        fileName = "./traces/text" + str(i) + ".npz"
        textData = np.load(fileName)
        selectedX, abandonedX, selectedY, abandonedY = train_test_split(textData['x'], textData['y'], train_size=dataSize)
        xTrain, xTest, yTrain, yTest = train_test_split(selectedX, selectedY)

        tmp = 1.0
        for j in range(0, 12):
            print("\n\nPredict the " + str(j+1) + "-th bit of the password")
            model = Sequential()
            model.add(Dense(64, activation="sigmoid", input_dim=xTrain.shape[1]))
            model.add(Dense(64, activation="sigmoid"))
            model.add(Dense(95, activation="softmax"))

            model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=['accuracy'])

            model.fit(xTrain, yTrain[:,j], nb_epoch=epochNum)

            score = model.evaluate(xTest, yTest[:,j])
            tmp = tmp * score[1]
        ret = ret + tmp
    return ret/10.0

