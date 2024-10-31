library(ggplot2)
library(dplyr)

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

words_table <- words_table |>
  mutate(word = factor(word, levels = word[order(-count)]))

plot <- ggplot(words_table, aes(x = word, y = count)) +
  geom_col(fill = "steelblue") +
  labs(
    x = "Words",
    y = "Count",
    title = "Lyrics"
  ) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggsave("lyrics.png", plot = plot, width = 10, height = 6, dpi = 300)