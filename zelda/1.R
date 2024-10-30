zelda <- read.csv("zelda.csv")

zelda <- pivot_wider(
  zelda,
  id_cols = title,
  names_from = role,
  values_from = names
)