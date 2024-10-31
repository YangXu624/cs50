load("zelda.RData")

zelda <- zelda |>
  arrange(year) |>
  group_by(title) |>
  filter()

View(zelda)