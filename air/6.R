load("air.RData")
air$emissions <- as.numeric(gsub(",", "", air$emissions))

air <- air |>
  group_by(pollutant) |>
  summarize(emissions = sum(emissions)) |>
  arrange(desc(emissions))

save(air, file = "6.RData")