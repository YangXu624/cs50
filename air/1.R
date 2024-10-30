air <- read.csv("air.csv")

air <- air |>
  select(!c("Pollutant.Type", "SCC.Code", "EIS.Sector", "Source.Description", "EPA.Region", "FIPS")) |>
  as_tibble()

save(air, file = "air.RData")