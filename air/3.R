load("air.RData")

air <- air |>
  filter(State.County == "OR - Washington")

save(air, file = "3.RData")