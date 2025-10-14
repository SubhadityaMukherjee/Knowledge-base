
---
toc: true
title: Time series forecasting using LSTM

tags: ["article"]
date modified: 
date created: 
---
# Time series forecasting using LSTM 

:::section{.abstract}

## Overview
Any temporal data can be framed as a time series task. Data such as heart rates, stock market prices, sensor logs and many others fall under the category of time series data. There are many Deep Learning architectures that are used to model such data, LSTMs being one of them. This article focuses on building an LSTM time series model.
:::

:::section{.main}

## What are we building? 
In this article, we will be creating an LSTM time series model. We will be using data that we generate and create a simple LSTM that can model it accurately. To perform this task, we will write functions that can generate data, model it and perform predictions on future points. 
We will implement this model using Tensorflow and the below sections explain how to perform just that.

## Pre-Requisites
Before moving on to creating the LSTM time series model, we must understand some pre-requisite information.

### What is Time Series?
A time series data is any **temporal** data that has a **discrete time interval** and almost **equidistant time steps**. The general task is to estimate the function that was used to generate such the time series. If the function can be estimated correctly, future points that the model has not encountered yet can be predicted.
Examples of time series include heart rate data, stock market data and many others.

### RNNs
RNNs are a family of models that take entire series as inputs and return series as outputs. This algorithm is a sequential process and contains hidden states that model the underlying data. Unlike a simple Convolutional network that uses Backpropagation, an RNN uses a modified variant called Backpropagation through time (BPTT) that enables it to embed temporal data. An RNN is said to be Turing complete and is used in domains such as Natural Language Processing, Computer Vision, Robotics and many others.
The RNN architecture is made up of **gates** and is shown below.

[IMAGE {1} RNN START SAMPLE]
![RNN](https://hackmd.io/_uploads/B1W-pj49i.png)
[IMAGE {1} FINISH SAMPLE]

### Problems with Classical RNNs
RNNs suffer from a variety of problems due to their sequential nature.
- RNNs fail to model longer sequences. This property makes it very hard to use for data that has a long temporal span.
- The classical RNN also had an issue with exploding and vanishing gradients due to the way the underlying architecture worked. These problems make an RNN very unstable. 

### What is LSTM?
LSTMs are a modified version of RNNs with different gates that enable the architecture to model much longer sequences. The LSTMs use gated connections that learn which features to forget and which to remember. The ability to choose what to forget makes them much better than a classical RNN. LSTMs are also a lot more stable and have a smaller chance of exploding or vanishing gradients.
The LSTM architecture is shown below.

[IMAGE {2} LSTM START SAMPLE]
![LSTM](https://hackmd.io/_uploads/HynWai49o.png)
[IMAGE {2} FINISH SAMPLE]


### How are we going to build this? 
To build an LSTM time series model, we will write functions that can generate a time series data. Once we have the data, we will pre-process it and make it fit to be used by the model. We will also write a function that can display the results of the model. After creating these helper functions, we will create a simple LSTM model and train it using the data we generated previously.
The LSTM time series model we will be using in this article is just comprised of a single LSTM block followed by a FC layer and is very easy to implement. After implementing all the required functions, we will train the model and use it to predict future points.
The following sections detail the implementation. 

### Final Output 
The final output of the LSTM time series model is a prediction of future points that the model has not encountered yet. The output we get after training the model for ~50 epochs is shown below.
[IMAGE {3} Final Output START SAMPLE]
![Final Output](https://hackmd.io/_uploads/HksfaoNqi.png)
[IMAGE {3} FINISH SAMPLE]


## Requirements 
There are many libraries that we need to implement an LSTM time series model. Since we will be building the architecture in Tensorflow, we import it first. We will also be using the numerical processing library numpy, the tabular data library pandas and the plotting libraries matplotlib and seaborn. The rc module in matplotlib enables configuring some of the plots and comes in handy later on.
```python
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt
from matplotlib import rc
```

## Building the Time Series Forecaster
The Time Series Forecaster model has a simple LSTM based architecture. Before creating it, we have to write functions to set up the library, generate and load and finally pre-process the data. 
The model we will use for this article is a Sequential model comprising an LSTM block followed by a Fully Connected layer. We will then use the generated data and this model to train a LSTM time series prediction model. We will use the trained model to predict points in the future that the model has not seen before.
The following sections detail all of these points.

### Setup
To set up our modules, we set the RANDOM_SEED variable. This variable sets the seed for the random number generator and ensures that we get the same “random” numbers every time. This is not useful in practice but is done only for demonstration purposes. We also modify the plot to be a white style grid with a muted palette for better display.
```python
sns.set(style='whitegrid', palette='muted', font_scale=1.5)
rcParams['figure.figsize'] = 16, 10
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
tf.random.set_seed(RANDOM_SEED)
```

### Data
To generate the data, we create a custom function that uses a combination of a Sin wave and a small Gaussian noise. These values are generated in the range of (0,200) with a step of 0.1 . 
To see how this data looks like, we can plot it using matplotlib.

```python
data_time = np.arange(0, 200, 0.1)
sin_values = np.sin(data_time) + np.random.normal(scale=0.5, size=len(data_time))
plt.plot(data_time, sin_values, label='sine (with noise)');
```

[IMAGE {4} Original Data START SAMPLE]
![Original Data](https://hackmd.io/_uploads/S1gKQToEqj.png)
[IMAGE {4} FINISH SAMPLE]

### Data Pre-processing
Now, we need to convert this data into a DataFrame before passing it to the model. Doing so makes future processes much easier. We also split the data into training and testing components.
The first few rows of the DataFrame are shown here.

[IMAGE {5} Pre-Processing START SAMPLE]
![Pre-Processing](https://hackmd.io/_uploads/S1H4aoV9j.png)
[IMAGE {5} FINISH SAMPLE]


```python
data_full = pd.DataFrame(dict(sine=sin_values), index=data_time, columns=['sine'])
data_full.head()

len_train = int(len(data_full) * 0.8)
len_test = len(data_full) - len_train
train, test = data_full.iloc[0:len_train], data_full.iloc[len_train:len(data_full)]
```

Now that we have created a data frame, we will use it to generate batches of data. We do this using the following function and create the input and labels for both training and testing.
```python
def gen_data(X, y, num_steps=1):
    Xs, ys = [], []
    for i in range(len(X) - num_steps):
        Xs.append(X.iloc[i:(i + num_steps)].values)       
        ys.append(y.iloc[i + num_steps])
    return np.array(Xs), np.array(ys)
    
num_steps = 10
trainX, trainY = gen_data(train, train.sine, num_steps)
testX, testY = gen_data(test, test.sine, num_steps)
```

### Implementing the Sequential model
We can finally implement the LSTM time series model. This is a very simple model and just has a single LSTM layer followed by a FC layer. 
We compile the model with the **Mean Squared Error** loss function and an **Adam** Optimiser. This compiled model can now be trained on the generated data.

```python
lstm_model = keras.Sequential()
lstm_model.add(keras.layers.LSTM(128, input_shape=(trainX.shape[1], trainX.shape[2])))
lstm_model.add(keras.layers.Dense(1))
lstm_model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.001))
```

### Early Stopping Callback
Time series model tend to Overfit really easily. To reduce the probability of Overfitting, the Early Stopping callback is used. This callback uses the number of epochs as a hyper parameter. If the validation accuracy does not increase for a few epochs, the model is saved and training is stopped. This stops the training before the model starts to focus too much on the training data.

```python
callbacks=[tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)]
```

### Model Training
Once we have defined all the required functions, we can train the model. In this article we train the LSTM time series model for 30 epochs with a batch size of 16. We use a validation split of 0.1% and also supply the Early Stopping callback that we defined earlier.
```python
history = lstm_model.fit(
    trainX, trainY, 
    epochs=30, 
    batch_size=16, 
    validation_split=0.1,
    shuffle=False,
    callbacks=[tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)],
)
```

[IMAGE {6} Training START SAMPLE]
![Training](https://hackmd.io/_uploads/BJdHTo4qj.png)
[IMAGE {6} FINISH SAMPLE]

### Evaluation
After training the model, we can use the *evaluate* function to perform a batch evaluation on the test dataset. We can see that the model performs pretty decently. 
```python
lstm_model.evaluate(testX)
```
To visualize the training performance, we plot both the training and validation losses throughout history. We can see that the model is learning stably and is neither Overfitting nor Underfitting the data.
```python
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend();
```
[IMAGE {7} Evaluation START SAMPLE]
![Evaluation](https://hackmd.io/_uploads/BymPpjN9s.png)
[IMAGE {7} FINISH SAMPLE]

### Predicting a new point in the future
No LSTM time series model is useful without the ability to predict future points. We can use the *predict* function on a set of future points to see how well the model can predict the results. After performing inference, we plot the results against the actual data.

```python
y_pred = lstm_model.predict(testX)
plt.plot(testY, marker='.', label="true")
plt.plot(y_pred, 'r', label="prediction")
plt.ylabel('Value')
plt.xlabel('Time Step')
plt.legend()
plt.show();
```

We can see that the model did perform pretty decently. Further improvements in performance can be obtained by training for longer, using more data and many other methods that are beyond the scope of this article.

:::
:::section{.summary}

## Conclusion
- In this article, we learnt what an LSTM model is and why it was created.
- We learnt how to create an LSTM model in Tensorflow.
- We also learnt how to generate our own time series data using a sin curve.
- Finally, we trained an LSTM time series model on the generated data.
- We also learned how to use the trained model to predict points in the future and display its predictions.
:::



