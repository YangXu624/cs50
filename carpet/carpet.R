calculate_growth_rate <- function(years, visitors) {
  growth_rate <- (as.integer(visitors[length(visitors)]) - as.integer(visitors[1])) / (as.integer(years[length(years)]) - as.integer(years[1]))
  return(growth_rate)
}

predict_visitors <- function(years, visitors, year) {
  diff <- year - as.integer(years[length(years)])
  new <- as.integer(visitors[length(visitors)]) + calculate_growth_rate(years, visitors) * diff
}

visitors <- read.csv("visitors.csv")
year <- as.integer(readline("Year: "))
predicted_visitors <- predict_visitors(visitors$year, visitors$visitors, year)
cat(paste0(predicted_visitors, " million visitors\n"))
