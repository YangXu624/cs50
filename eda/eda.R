num_darts <- 100000
num_in_circle <- 0

for (i in 1:num_darts) {
  x <- runif(n = 1, min = -1, max = 1)
  y <- runif(n = 1, min = -1, max = 1)
  if (x^2 + y^2 <= 1) {
    num_in_circle <- num_in_circle + 1
  }
}

pi_est <- 4 * num_in_circle / num_darts
print(pi_est)