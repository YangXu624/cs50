rail <- read.csv("rail.csv")
bus <- read.csv("bus.csv")

route <- readline(prompt = "Route: ")

query_rail <- subset(rail, route %in% mode)
query_bus <- subset(bus, mode == route)

if (length(query_rail) > 0) {
  peak <- subset(query_rail, peak == "PEAK")
  peak_mean <- round(mean(peak$numerator / peak$denominator), 0)
  off_peak <- subset(query_rail, peak == "OFF_PEAK")
  off_peak_mean <- round(mean(off_peak$numerator / off_peak$denominator), 0)

  cat("Peak mean: ", peak_mean, ".\n")
  cat("Off peak mean: ", off_peak_mean, ".\n")
} else {
  cat("No such route.")
}