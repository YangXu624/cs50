load("zelda.RData")
zelda <- zelda |>
  distinct(title, .keep_all = TRUE)
