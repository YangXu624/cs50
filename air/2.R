load("air.RData")

non_numeric <- air[is.na(as.numeric(air$Emissions..Tons.)), "Emissions..Tons."]
print(non_numeric)
air <- air |>
  arrange(desc(as.numeric(Emissions..Tons.)))
View(air)
save(air, file = "2.RData")
