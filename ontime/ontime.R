rail <- read.csv("rail.csv")
bus <- read.csv("bus.csv")

route <- readline(prompt = "Route: ")

query <- subset(rail, route %in% mode)