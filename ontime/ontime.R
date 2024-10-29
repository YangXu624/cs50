rail <- read.csv("rail.csv")
bus <- read.csv("bus.csv")

query_route <- readline(prompt = "Route: ")

filter <- grepl(query_route, rail$route)
query_rail <- rail[filter, ]
query_bus <- subset(bus, route == query_route)

if (nrow(query_rail) > 0) {
  peak <- subset(query_rail, peak == "PEAK")
  peak_mean <- round(mean(100 * peak$numerator / peak$denominator, na.rm = TRUE), 0)
  off_peak <- subset(query_rail, peak == "OFF_PEAK")
  off_peak_mean <- round(mean(100 * off_peak$numerator / off_peak$denominator, na.rm = TRUE), 0)

  cat("Peak mean: ", peak_mean, "\n")
  cat("Off peak mean: ", off_peak_mean, "\n")
} else {
  cat("No such route.")
}

if (nrow(query_bus) > 0) {
  peak <- subset(query_bus, peak == "PEAK")
  peak_mean <- round(mean(100 * peak$numerator / peak$denominator, na.rm = TRUE), 0)
  off_peak <- subset(query_bus, peak == "OFF_PEAK")
  off_peak_mean <- round(mean(100 * off_peak$numerator / off_peak$denominator, na.rm = TRUE), 0)

  cat("Peak mean: ", peak_mean, "\n")
  cat("Off peak mean: ", off_peak_mean, "\n")
} else {
  cat("No such route.")
}