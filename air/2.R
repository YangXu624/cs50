load("air.RData")
air$emissions <- as.numeric(gsub(",", "", air$emissions))

air <- air |>
  arrange(desc(as.numeric(emissions)))
save(air, file = "2.RData")
