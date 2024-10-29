get_scores <- function(country) {
  years <- c("2024", "2023", "2022", "2021", "2020")
  scores <- c()
  for (year in years) {
    data <- read.csv(paste0(year, ".csv"))
    filter <- data$country == country
    selected <- data[filter, ]
    selected <- selected[, -1]
    scores[year] <- apply(selected, MARGIN = 1, FUN = sum)
  }
  return(scores)
}

country <- readline("Country: ")
scores <- get_scores(country)
for (score in scores) {
  cat(score, "\n")
}
