load("air.RData")
air$Emissions..Tons. <- as.numeric(gsub(",", "", air$Emissions..Tons.))

air <- air |>
  filter(State.County == "OR - Washington") |>
  arrange(desc(Emissions..Tons.))

save(air, file = "4.RData")