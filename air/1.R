air <- read.csv("air.csv")

air |>
  select(!c("Pollutant.Type", "SCC.Code", "EIS.Sector", "Source.Description", "EPA.Region", "FIPS"))

View(air)