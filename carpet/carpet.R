calculate_growth_rate <- function(years, visitors) {
  growth <- c()
  for (i in 1:length(years) - 1) {
    growth[i] <- (visitors[i + 1] - visitors[i]) / visi
  }
}

predict_visitors <- function(years, visitors, year) {
  # TODO: Predict visitors in given year
}

visitors <- read.csv("visitors.csv")
year <- as.integer(readline("Year: "))
predicted_visitors <- predict_visitors(visitors$year, visitors$visitors, year)
cat(paste0(predicted_visitors, " million visitors\n"))
