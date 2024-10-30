load("air.RData")
air$Emissions..Tons. <- as.numeric(gsub(",", "", air$Emissions..Tons.))

air <- air |>
  group_by(POLLUTANT) |>
  summarize(emissions = sum(Emissions..Tons.))

save(air, file = "6.RData")