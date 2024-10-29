y2024 <- read.csv("2024.csv")
apply(y2024, MARGIN = 1, FUN = sum)

country <- readline("Country: ")
