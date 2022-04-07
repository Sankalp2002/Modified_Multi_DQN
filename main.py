#Copyright (C) 2020 Salvatore Carta, Anselmo Ferreira, Alessandro Sebastian Podda, Diego Reforgiato Recupero, Antonio Sanna. All rights reserved.

#os library is used to define the GPU to be used by the code, needed only in cerain situations (Better not to use it, use only if the main gpu is Busy)
#import os
#os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID";
#os.environ["CUDA_VISIBLE_DEVICES"]="0";

#This is the class call for the Agent which will perform the experiment
from deepQTrading import DeepQTrading

#Date library to manipulate time in the source code
import datetime

#Keras library to define the NN to be used
from keras.models import Sequential

#Layers used in the NN considered
from keras.layers import Dense, Activation, Flatten

#Activation Layers used in the source code
from keras.layers.advanced_activations import LeakyReLU, PReLU, ReLU

#Optimizer used in the NN
from tensorflow.keras.optimizers import Adam

#Libraries used for the Agent considered
from rl.agents.dqn import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import EpsGreedyQPolicy


#Library used for showing the exception in the case of error 
import sys

#import tensorflow as tf
#from keras.backend.tensorflow_backend import set_session
#config = tf.ConfigProto()
#config.gpu_options.per_process_gpu_memory_fraction = 0.3
#set_session(tf.Session(config=config))



#Let's capture the starting time and send it to the destination in order to tell that the experiment started 
startingTime=datetime.datetime.now()

#There are three actions possible in the stock market
#Hold(id 0): do nothing.
#Long(id 1): It predicts that the stock market value will raise at the end of the day. 
#So, the action performed in this case is buying at the beginning of the day and sell it at the end of the day (aka long).
#Short(id 2): It predicts that the stock market value will decrease at the end of the day.
#So, the action that must be done is selling at the beginning of the day and buy it at the end of the day (aka short). 
nb_actions = int(sys.argv[1])

isOnlyShort=sys.argv[2]==1

#This is a simple NN considered. It is composed of:
#One flatten layer to get 68 dimensional vectors as input
#One dense layer with 35 neurons and LeakyRelu activation
#One final Dense Layer with the 3 actions considered
#the input is 20 observation days from the past, 8 observations from the past week and 
#40 observations from the past hours
model = Sequential()
model.add(Flatten(input_shape=(1,1,68)))
model.add(Dense(35,activation='linear'))
model.add(LeakyReLU(alpha=.001))
model.add(Dense(nb_actions))
model.add(Activation('linear'))


#Define the DeepQTrading class with the following parameters:
#explorations: 0.2 operations are random, and 100 epochs.
#in this case, epochs parameter is used because the Agent acts on daily basis, so its better to repeat the experiments several
#times so, its defined that each epoch will work on the data from training, validation and testing.
#trainSize: the size of the train data gotten from the dataset, we are setting 5 stock market years, or 1800 days
#validationSize: the size of the validation data gotten from dataset, we are setting 6 stock market months, or 180 days
#testSize: the size of the testing data gotten from dataset, we are setting 6 stock market months, or 180 days
#outputFile: where the results will be written
#begin: where the walks will start from. We are defining January 1st of 2010
#end: where the walks will finish. We are defining February 22nd of 2019
#nOutput:number of walks
dqt = DeepQTrading(
    model=model,
    explorations=[(0.2,100)],
    trainSize=datetime.timedelta(days=360*2),
    validationSize=datetime.timedelta(days=30*2),
    testSize=datetime.timedelta(days=30*1),
    outputFile="./Output/csv/walks/walks",
    begin=datetime.datetime(2016,4,3,0,0,0,0),
    end=datetime.datetime(2021,12,19,0,0,0,0),
    nbActions=nb_actions,
    isOnlyShort=isOnlyShort,
    ensembleFolderName=sys.argv[3]
    )

dqt.run()

dqt.end()


