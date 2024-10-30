load("air.RData")

air <- air |>
  filter(State.County == "OR - Washington")

View(air)