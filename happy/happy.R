y2024 <- read.csv("2024.csv")
y2024 <- y2024[-1, ]
apply(y2024, MARGIN = 1, FUN = sum)

country <- readline("Country: ")
