load("air.RData")
air$emissions <- as.numeric(gsub(",", "", air$emissions))

air <- air |>
  filter(county == "OR - Washington") |>
  arrange(desc(emissions))

save(air, file = "4.RData")