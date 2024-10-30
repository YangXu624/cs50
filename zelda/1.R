zelda <- read.csv("zelda.csv")

zelda <- pivot_wider(
  zelda,
  id_cols = c(title, release),
  names_from = role,
  values_from = names
)

View(zelda)