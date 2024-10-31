load("zelda.RData")

zelda1 <- zelda |>
  arrange(year) |>
  group_by(title)

zelda2 <- zelda1 |>
  slice_head()

zelda <- zelda1 |>
  semi_join(zelda2, by = c("title", "year"))

save(zelda, file = "3.RData")