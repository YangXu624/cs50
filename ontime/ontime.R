rail <- read.csv("rail.csv")
bus <- read.csv("bus.csv")

route <- readline(prompt = "Route: ")

query_rail <- subset(rail, route %in% mode)
query_bus <- subset(bus, mode == route)

if (length(query_rail) > 0) {
  peak <- round(mean(query_rail$numerator / query_rail$denominator), 0)
  off_peak
}