from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import numpy as np
from sklearn.model_selection import train_test_split

def modelGP(dataSize, epochNum, hiddenLayerSize):
    ret = 0
    for i in range(0, 10):
        fileName = "./traces/GP" + str(i) + ".npz"
        gpData = np.load(fileName)

        selectedX, abandonedX, selectedY, abandonedY = train_test_split(gpData['x'], gpData['y'], train_size=dataSize)
        xTrain, xTest, yTrain, yTest = train_test_split(selectedX, selectedY)

        for j in range(0, 1):
            print("\n\nPredict the " + str(j+1) + "-th bit of the password")
            model = Sequential()
            model.add(Dense(hiddenLayerSize, activation="sigmoid", input_dim=xTrain.shape[1]))
            model.add(Dense(hiddenLayerSize, activation="sigmoid"))
            model.add(Dense(100, activation="softmax"))

            model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=['accuracy'])

            model.fit(xTrain, yTrain[:,j], nb_epoch=epochNum)
            score = model.evaluate(xTest, yTest[:,j])
            ret = ret + score[1]
    return ret/10.0