# Boston House Pricing Prediction with Custom Linear Regression and Gradient Descent

In this project, I aim to predict house prices in the Boston area using a custom implementation of linear regression and the gradient descent optimization algorithm. This README provides a brief overview of the project.

## Overview

**Linear regression** is a fundamental machine learning algorithm used to model the relationship between one or more input features and a target variable. In this project, I am applying linear regression to predict Boston house prices. 
## Implementation

We have implemented linear regression and gradient descent from scratch in Python. Here's a quick summary of what the code does:

- We initialize the model parameters:
  - `weights`: Initially set to zeros, these represent the coefficients of the features in the linear equation.
  - `bias`: Initially set to 0, this is the intercept term.
  - `learning_rate`: This controls the step size during gradient descent.
  - `epochs`: The number of iterations or epochs for training.

- The `gradient_descent` function:
  - Iteratively updates the weights and bias using gradient descent to minimize the cost function (mean squared error).
  - It calculates the predictions using the current weights and bias.
  - Computes the gradients for weights and bias.
  - Updates the weights and bias with the calculated gradients.
  - Tracks the cost (loss) for each epoch and stores it in the `costs` list.
  - Prints the loss at specific epochs (10, 20, 30, 40, and 50 in this case).

- Finally, we call the `gradient_descent` function with the training data and the defined parameters to train the model.

