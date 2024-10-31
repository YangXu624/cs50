load("zelda.RData")

zelda <- zelda |>
  arrange(year) |>
  group_by(title) |>
  distinct(title, year, .keep_all = TRUE)

View(zelda)