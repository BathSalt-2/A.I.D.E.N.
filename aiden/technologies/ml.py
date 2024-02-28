from sklearn.ensemble import RandomForestClassifier  # Import the RandomForestClassifier from sklearn.ensemble
from sklearn.model_selection import train_test_split  # Import the train_test_split function from sklearn.model_selection
from sklearn.metrics import accuracy_score  # Import the accuracy_score function from sklearn.metrics
import pandas as pd  # Import pandas library

class ML:
    def __init__(self):
        """
        Initialize the ML class with a RandomForestClassifier model.
        """
        self.model = RandomForestClassifier()

    def train(self, data, target):
        """
        Train the model using the provided data and target.

        Args:
            data (pandas.DataFrame): The input data to train the model on.
            target (pandas.Series): The target variable to train the model on.

        Returns:
            float: The accuracy of the model on the test set.
        """
        X = data  # Assign the input data to X
        y = target  # Assign the target variable to y

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Split the data into training and testing sets

        self.model.fit(X_train, y_train)  # Train the model on the training set

        y_pred = self.model.predict(X_test)  # Make predictions on the test set

        accuracy = accuracy_score(y_test, y_pred)  # Calculate the accuracy of the model on the test set

        return accuracy

    def predict(self, data):
        """
        Make predictions using the trained model.

        Args:
            data (pandas.DataFrame): The input data to make predictions on.

        Returns:
            numpy.ndarray: The predicted target variable.
        """
        prediction = self.model.predict(data)  # Make predictions on the input data

        return prediction

   
