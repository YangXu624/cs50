load("air.RData")
air$emissions <- as.numeric(gsub(",", "", air$emissions))

air <- air |>
  group_by(level_1, pollutant) |>
  summarize(emissions = sum(emissions))

air <- air %>%
  rename(source = level_1)

save(air, file = "7.RData")