import tensorflow as tf
from tensorflow import keras

class DL:
    def __init__(self):
        """
        Initialize the Deep Learning object. The model attribute is initialized to None.
        """
        self.model = None

    def create_model(self, input_shape, output_shape):
        """
        Create a sequential Keras model with the following layers:
        1. A Dense layer with 128 neurons, 'relu' activation function, and input shape defined by the input_shape parameter.
        2. A Dense layer with 64 neurons and 'relu' activation function.
        3. A Dense layer with output_shape neurons and 'softmax' activation function.
        Compile the model with 'adam' optimizer, 'sparse_categorical_crossentropy' loss function, and 'accuracy' metric.

        :param input_shape: The input shape for the first layer of the model.
        :param output_shape: The number of neurons in the final layer of the model.
        """
        self.model = keras.Sequential([
            keras.layers.Dense(128, activation='relu', input_shape=input_shape),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(output_shape, activation='softmax')
        ])

        self.model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

    def train_model(self, train_data, train_labels, epochs=5):
        """
        Train the model using the provided train_data and train_labels for the number of epochs defined by the epochs parameter.
        The default value for epochs is 5.

        :param train_data: The input data for training the model.
        :param train_labels: The labels corresponding to the train_data.
        :param epochs: The number of times the model will be trained on the entire dataset. Default is 5.
        """
