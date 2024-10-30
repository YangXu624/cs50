air <- read.csv("air.csv")

air <- air |>
  select(!c("Pollutant.Type", "SCC.Code", "EIS.Sector", "Source.Description", "EPA.Region", "FIPS")) |>
  rename(
    state = State,
    county = State.County,
    pollutant = POLLUTANT,
    emissions = Emissions..Tons.,
    level_1 = SCC.LEVEL.1,
    level_2 = SCC.LEVEL.1,
    level_3 = SCC.LEVEL.1,
    level_4 = SCC.LEVEL.1
  ) |>
  as_tibble()

save(air, file = "air.RData")