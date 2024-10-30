load("air.RData")


air <- air |>
  arrange(desc(Emissions..Tons.))

View(air)
