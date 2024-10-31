load("zelda.RData")
zelda <- zelda |>
  arrange(year) |>
  # distinct(title, .keep_all = TRUE)

View(zelda)