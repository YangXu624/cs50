get_scores <- function(country) {
  years <- c("2020", "2021", "2022", "2023", "2024")
  for (year in years) {
    data <- read.csv(paste0(year, ".csv"))
    if (country %in% data$country) {
      filter <- data$country == country
      selected <- data[filter, ]
      selected <- selected[, -1]
      score <- round(apply(selected, MARGIN = 1, FUN = sum), 2)
      if (is.na(score)) {
        score <- "data unavailable"
      }
      cat(country, " (", year, "): ", score, "\n", sep = "")
    } else {
      score <- "data unavailable"
      cat(country, " (", year, "): ", score, "\n", sep = "")
    }
  }
}

country <- readline("Country: ")
scores <- get_scores(country)
