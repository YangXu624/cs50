words <- read_file("lyrics/astley.txt")

words <- words |>
  str_replace_all("\n", " ") |>
  str_replace_all("-", " ") |>
  str_split(" ", simplify = TRUE) |>
  as.vector() |>
  str_replace_all("\\(", "") |>
  str_replace_all("\\)", "") |>
  str_replace_all(",", "") |>
  str_to_title()

words_table <- tibble(word = words) |>
  filter(word != "") |>
  group_by(word) |>
  summarize(count = n()) |>
  arrange(desc(count))


ggplot(words_table, aes(x = word, y = count)) +
  geom_col(fill = word) +
  labs = (
    x = "Words",
    y = "Count",
    title = "Lyrics"
  )