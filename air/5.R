load("air.RData")
air$Emissions..Tons. <- as.numeric(gsub(",", "", air$Emissions..Tons.))

air <- air |>
  group_by(State.County) |>
  slice_max(order_by = Emissions..Tons.)

save(air, file = "5.RData")