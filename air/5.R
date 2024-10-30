load("air.RData")
air$emissions <- as.numeric(gsub(",", "", air$emissions))

air <- air |>
  group_by(county) |>
  slice_max(order_by = emissions)

save(air, file = "5.RData")