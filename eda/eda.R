num_darts <- 1000
num_in_circle <- 0

pi_est <- numeric(num_darts)

for (i in 1:num_darts) {
  x <- runif(n = 1, min = -1, max = 1)
  y <- runif(n = 1, min = -1, max = 1)

  if (x^2 + y^2 <= 1) {
    num_in_circle <- num_in_circle + 1
  }

  pi_est[i] <- 4 * num_in_circle / i
}

plot(
  x = 1:num_darts,
  y = pi_est,
  ylim = c(0, 5),
  type = "l",
  xlab = "Number of Darts Thrown",
  ylab = "Pi Estimate",
  main = "Graph"
)

abline(h = pi, col = "red", lty = 2)