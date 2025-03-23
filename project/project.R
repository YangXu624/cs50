# Install necessary libraries
library(keras)

# Sigmoid Activation Function
sigmoid <- function(Z) {
    return(1 / (1 + exp(-Z)))
}

# Derivative of Sigmoid
sigmoid_derivative <- function(Z) {
    S <- sigmoid(Z)
    return(S * (1 - S))
}

# Softmax Activation Function
softmax <- function(Z) {
    exp_Z <- exp(Z)
    col_sum <- colSums(exp_Z)  # Sum each column
    return(exp_Z / col_sum)
}

# Forward Propagation
forward <- function(X, W, b, activationFunction) {
    Z <- X %*% W + b  # Linear combination: Z = X * W + b
    return(activationFunction(Z))  # Apply activation function
}

# Backward Propagation
backward <- function(X, Y, A, W, activationFunction, learning_rate = 0.01) {
    # Assume X: input, Y: true labels, A: output of forward function (predictions)

    m <- nrow(X)  # Number of training examples

    # Calculate the derivative for output layer (for softmax + cross-entropy)
    if (identical(activationFunction, softmax)) {
        # For multi-class classification, the derivative of softmax with cross-entropy loss is:
        dA <- A - Y  # Gradient of loss w.r.t output (A is predicted, Y is true)
    }

    # Compute gradients for weights and bias (backpropagation)
    dZ <- dA  # For output layer (softmax)

    # Calculate gradients of weights and bias
    dW <- t(X) %*% dZ / m  # Gradient w.r.t. weights
    db <- colSums(dZ) / m   # Gradient w.r.t. bias

    # Update weights and bias using gradient descent
    W <- W - learning_rate * dW
    b <- b - learning_rate * db

    return(list(W = W, b = b))
}

# Training the Neural Network
train <- function(X, Y, W1, b1, W2, b2, activationFunction, epochs = 1000, learning_rate = 0.01) {
    for (epoch in 1:epochs) {
        # Forward pass: hidden layer
        A1 <- forward(X, W1, b1, sigmoid)  # A1 is the output of hidden layer

        # Forward pass: output layer
        A2 <- forward(A1, W2, b2, softmax)  # A2 is the output of the network

        # Backward pass
        gradients <- backward(X, Y, A2, W2, softmax, learning_rate)

        # Update weights and biases
        W2 <- gradients$W
        b2 <- gradients$b

        # Optionally print the loss (for monitoring)
        if (epoch %% 100 == 0) {
            loss <- -sum(Y * log(A2)) / nrow(X)  # Cross-entropy loss
            print(paste("Epoch", epoch, "Loss:", loss))
        }
    }
    return(list(W1 = W1, b1 = b1, W2 = W2, b2 = b2))
}

# Load the MNIST dataset
mnist <- dataset_mnist()

# Extract training and testing data
X_train <- mnist$train$x  # 60,000 images of size 28x28
Y_train <- mnist$train$y  # Labels (0-9) for training set
X_test <- mnist$test$x    # 10,000 images for testing
Y_test <- mnist$test$y    # Labels (0-9) for testing set

# Check the structure of the data
str(X_train)

# Normalize the data to the range [0, 1]
X_train <- X_train / 255
X_test <- X_test / 255

# Reshape the data (add a channel dimension if using CNN, not needed for basic models)
X_train <- array_reshape(X_train, c(nrow(X_train), 28, 28, 1))
X_test <- array_reshape(X_test, c(nrow(X_test), 28, 28, 1))

# One-hot encode the labels
Y_train <- to_categorical(Y_train, 10)  # 10 classes (digits 0-9)
Y_test <- to_categorical(Y_test, 10)

# Example: Modify your neural network to use the MNIST data

# Define the model architecture (1 hidden layer, 1 output layer)
W1 <- matrix(runif(28 * 3), nrow = 28)  # 28 input features (28x28 images) -> 3 neurons in hidden layer
b1 <- matrix(0, nrow = 1, ncol = 3)

W2 <- matrix(runif(3 * 10), nrow = 3)   # 3 neurons in hidden layer -> 10 output classes
b2 <- matrix(0, nrow = 1, ncol = 10)

# Train the model using the MNIST data
results <- train(X_train, Y_train, W1, b1, W2, b2, softmax, epochs = 5, learning_rate = 0.01)

# Evaluate the model on the test data
A1 <- forward(X_test, W1, b1, sigmoid)
A2 <- forward(A1, W2, b2, softmax)

# Calculate accuracy
predictions <- apply(A2, 1, which.max) - 1  # Get the predicted class (0-9)
accuracy <- mean(predictions == apply(Y_test, 1, which.max) - 1)  # Compare with true labels
print(paste("Test accuracy:", accuracy))

