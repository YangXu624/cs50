load("zelda.RData")

zelda <- zelda |>
  arrange(year) |>
  group_by(title)


  filter(year == slice_head()$year)

View(zelda)