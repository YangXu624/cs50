# Sigmoid Activation Function
sigmoid <- function(Z) {
  return(1 / (1 + exp(-Z)))
}

# Derivative of Sigmoid
sigmoid_derivative <- function(Z) {
  S <- sigmoid(Z)
  return(S * (1 - S))
}

# Forward Propagation
forward <- function(X, W, b, activationFunction) {
  Z <- X %*% W + matrix(rep(b, nrow(X)), ncol = length(b), byrow = TRUE)  # Add bias term
  return(activationFunction(Z))
}

# Backward Propagation
backward <- function(X, Y, A, W, b, activationFunction, learning_rate = 0.01) {
  m <- nrow(X)  # Number of training examples

  # Calculate the derivative for output layer (for sigmoid, or softmax + cross-entropy)
  if (identical(activationFunction, sigmoid)) {
    dA <- A - Y  # For sigmoid output layer
  } else if (identical(activationFunction, softmax)) {
    # For multi-class classification, the derivative of softmax with cross-entropy loss is:
    dA <- A - Y  # Gradient of loss w.r.t output (A is predicted, Y is true)
  }

  # Compute gradients for weights and bias (backpropagation)
  dZ <- dA  # Gradient w.r.t. the pre-activation Z of output layer

  # Calculate gradients of weights and bias for output layer
  dW <- t(X) %*% dZ / m  # Gradient w.r.t. weights
  db <- colSums(dZ) / m   # Gradient w.r.t. bias

  W <- W - learning_rate * dW  # Update weights using gradient descent
  b <- b - learning_rate * db  # Update bias using gradient descent

  return(list(W = W, b = b))  # Return updated weights and biases
}



# Training the Neural Network
train <- function(X, Y, W1, b1, W2, b2, activationFunction, epochs = 1000, learning_rate = 0.01) {
  for (epoch in 1:epochs) {
    # Forward pass: hidden layer
    A1 <- forward(X, W1, b1, sigmoid)  # A1 is the output of the hidden layer

    # Forward pass: output layer
    A2 <- forward(A1, W2, b2, sigmoid)  # A2 is the output of the network

    # Backward pass
    gradients1 <- backward(X, Y, A2, W2, b2, sigmoid, learning_rate)  # Backpropagate through output layer
    gradients2 <- backward(A1, Y, A2, W1, b1, sigmoid, learning_rate)  # Backpropagate through hidden layer

    # Update weights and biases for both layers
    W1 <- gradients2$W
    b1 <- gradients2$b
    W2 <- gradients1$W
    b2 <- gradients1$b

    # Optionally print the loss (for monitoring)
    if (epoch %% 100 == 0) {
      loss <- -sum(Y * log(A2) + (1 - Y) * log(1 - A2)) / nrow(X)
      print(paste("Epoch", epoch, "Loss:", loss))
    }
  }
  return(list(W1 = W1, b1 = b1, W2 = W2, b2 = b2))
}



# Create synthetic data for a binary classification task
set.seed(42)
X_train <- matrix(runif(2000), nrow = 1000, ncol = 2)
Y_train <- ifelse(X_train[, 1] + X_train[, 2] > 1, 1, 0)

X_test <- matrix(runif(200), nrow = 100, ncol = 2)
Y_test <- ifelse(X_test[, 1] + X_test[, 2] > 1, 1, 0)

# Initialize weights and biases for binary classification
W1 <- matrix(runif(2 * 5), nrow = 2)  # 2 features -> 5 neurons in hidden layer
b1 <- matrix(0, nrow = 1, ncol = 5)  # Bias for 5 neurons

W2 <- matrix(runif(5 * 1), nrow = 5)  # 5 neurons in hidden layer -> 1 output neuron
b2 <- matrix(0, nrow = 1, ncol = 1)  # Bias for 1 output neuron

# Train the model
results <- train(X_train, Y_train, W1, b1, W2, b2, sigmoid, epochs = 500, learning_rate = 0.01)

# Evaluate the model on the test data
A1 <- forward(X_test, results$W1, results$b1, sigmoid)
A2 <- forward(A1, results$W2, results$b2, sigmoid)

# Calculate accuracy
predictions <- ifelse(A2 > 0.5, 1, 0)  # Threshold for binary classification
accuracy <- mean(predictions == Y_test)
print(paste("Test accuracy:", accuracy))
