load("air.RData")
air$Emissions..Tons. <- as.numeric(gsub(",", "", air$Emissions..Tons.))

air <- air |>
  arrange(desc(as.numeric(Emissions..Tons.)))
save(air, file = "2.RData")
