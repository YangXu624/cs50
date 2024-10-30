load("air.RData")

air <- air |>
  filter(State.County == "OR - Washington") |>
  arrange(desc(as.numeric(Emissions..Tons.)))

View(air)