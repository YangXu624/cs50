load("air.RData")
air$Emissions..Tons. <- as.numeric(gsub(",", "", air$Emissions..Tons.))

air <- air |>
  arrange(desc(Emissions..Tons.)) |>
  group_by(State.County) |>
  slice(max)

save(air, file = "4.RData")