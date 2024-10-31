load("zelda.RData")

zelda <- zelda |>
  filter(str_detect(producers, "Shigeru Miyamoto"))

zelda1 <- zelda |>
  arrange(year) |>
  group_by(title)

zelda2 <- zelda1 |>
  slice_head()

zelda <- zelda1 |>
  semi_join(zelda2, by = c("title", "year")) |>
  arrange(year, title, system)

save(zelda, file = "4.RData")