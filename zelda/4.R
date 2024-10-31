load("zelda.RData")

zelda <- zelda |>
  filter(str_detect(producers, "Shigeru Miyamoto"))

View(zelda)