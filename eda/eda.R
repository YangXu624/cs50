library(ggplot2)

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

# Create a data frame for ggplot2
data <- data.frame(
  darts = 1:num_darts,
  pi_est = pi_est
)

# Create the plot
plot <- ggplot(data, aes(x = darts, y = pi_est)) +
  geom_line() +
  geom_hline(yintercept = pi, color = "red", linetype = "dashed") +
  labs(x = "Number of Darts Thrown", y = "Pi Estimate", title = "Graph") +
  ylim(0, 5)

ggsave("visualization.png", plot = plot, width = 10, height = 6, dpi = 300)