load("air.RData")


air <- air |>
  arrange(desc(Emissions..Tons.))

save(air, file = "2.RData")
