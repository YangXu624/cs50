get_scores <- function(country) {
  years <- c("2020", "2021", "2022", "2023", "2024")
  scores <- c()
  for (year in years) {
    data <- read.csv(paste0(year, ".csv"))
    filter <- data$country == country
    selected <- data[filter, ]
    selected <- selected[, -1]
    cat(country, year, round(apply(selected, MARGIN = 1, FUN = sum), 2), "\n", sep = "")
  }
}

country <- readline("Country: ")
scores <- get_scores(country)
