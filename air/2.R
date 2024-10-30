air <- load("air.RData")

air <- air |>
  arrange(desc(as.numeric(Emissions..Tons.)))

View(air)