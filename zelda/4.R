load("zelda.RData")

zelda <- zelda |>
  filter(producer == "Shigeru Miyamoto")

View(zelda)