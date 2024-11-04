num_darts <- 1000000
num_in_circle <- 0

x <- runif(n = num_darts, min = -1, max = 1)
y <- runif(n = num_darts, min = -1, max = 1)

sum_squares <- x^2 + y^2
indices <- which(sum_squares <= 1)
num_in_circle <- length(indices)

pi_est <- 4 * num_in_circle / num_darts
print(pi_est)