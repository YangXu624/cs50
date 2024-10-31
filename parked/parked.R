words <- read_file("lyrics/astley.txt")

words <- words |>
  str_replace_all("\n", " ")

View(words)