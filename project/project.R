sigmoid <- function()

forward <- function(X, W, b, activationFunction) {
  Z <- X %*% W + b
  A <- activationFunction(Z)
}