load("air.RData")
air$Emissions..Tons. <- as.numeric(gsub(",", "", air$Emissions..Tons.))

air <- air |>
  group_by(SCC.LEVEL.1, POLLUTANT) |>
  summarize(emissions = sum(Emissions..Tons.))

air <- air %>%
  rename(source = SCC.LEVEL.1)

save(air, file = "7.RData")