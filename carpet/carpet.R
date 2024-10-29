calculate_growth_rate <- function(years, visitors) {
  growth_rate <- (visitors[length(visitors)] - visitors[1]) / (as.integer(years[length(years)]) - as.integer(years[1]))
  return(growth_rate)
}

predict_visitors <- function(years, visitors, year) {
  diff <- year - as.integer(years[length(years)])
  rate <- calculate_growth_rate(years, visitors)
  new <- visitors[length(visitors)] + rate * diff
  return(new)
}

visitors <- read.csv("visitors.csv")
year <- as.integer(readline("Year: "))
predicted_visitors <- predict_visitors(visitors$year, visitors$visitors, year)
cat(paste0(predicted_visitors, " million visitors\n"))
