import json
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten


class GestureRecognizerModel:

    def read_data(self, dataSet):
        with open(f"Service/Model/NeuralNetwork/GestureData/{dataSet}/{dataSet}_Data.json", "r") as dataFile:
            data = json.load(dataFile)
            data = np.array(data)

            trainingData = np.concatenate((data[:495], data[505:]), axis=0)
            testData = data[495:505]

            return trainingData, testData


    def load_data(self):
        dataFilesList = ["1_Five_Sign", "2_Two_Sign", "3_Okay_Sign", "4_Fist_Sign",
                        "5_Right_Sign", "6_Left_Sign", "7_Up_Sign", "8_Down_Sign"]

        trainingDataList, testDataList = [], []
        for file in dataFilesList:
            trainingSet, testSet = self.read_data(dataSet=file)
            trainingDataList.append(trainingSet)
            testDataList.append(testSet)


        trainingData = np.concatenate(trainingDataList, axis=0)
        testData = np.concatenate(testDataList, axis=0)

        return trainingData, testData


    def train_network(self):

        trainingData, testData = self.load_data()

        trainingOutputsList = [[i]*990 for i in range(8)]
        testOutputsList = [[i]*10 for i in range(8)]

        trainingSet = np.concatenate(trainingOutputsList, axis=0)
        testSet = np.concatenate(testOutputsList, axis=0)

        trainingOutputs = keras.utils.to_categorical(trainingSet, 8)
        testOutputs = keras.utils.to_categorical(testSet, 8)

        model = keras.Sequential([
            Flatten(input_shape=(21, 2, 1)),
            Dense(1024, activation='relu'),
            Dense(8, activation='softmax'),
        ])

        print("model-summary")
        print(model.summary())

        optimizerByAdam = keras.optimizers.SGD(learning_rate=0.1, momentum=0.0, nesterov=True)

        model.compile(
            optimizer=optimizerByAdam,
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

        log = model.fit(trainingData, trainingOutputs, batch_size=10, epochs=100,
                        validation_data=(testData, testOutputs))

        model.evaluate(testData, testOutputs)

        self.test_network(model, testData)

        print("model.get_weights()")
        print(model.get_weights())

        plt.plot(log.history['loss'])
        plt.plot(log.history['val_loss'])
        plt.grid(True)
        plt.show()

        model.save('GestureModel')


    def test_network(self, model, testData):

        for indexSet in range(8):
            x = np.expand_dims(testData[indexSet*10], axis=0)
            res = model.predict(x)
            print(res)
            print(np.argmax(res))



model = GestureRecognizerModel()
model.train_network()





