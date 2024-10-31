# Load necessary libraries
library(ggplot2)
library(dplyr)
library(readr)   # For read_file()
library(stringr) # For string manipulation functions

# Read the lyrics file
words <- read_file("lyrics/astley.txt")

# Process the words
words <- words |>
  str_replace_all("\n", " ") |>
  str_replace_all("-", " ") |>
  str_split(" ", simplify = TRUE) |>
  as.vector() |>
  str_replace_all("\\(", "") |>
  str_replace_all("\\)", "") |>
  str_replace_all(",", "") |>
  str_to_title()

# Create a table of word counts
words_table <- tibble(word = words) |>
  filter(word != "") |>
  group_by(word) |>
  summarize(count = n(), .groups = 'drop') |>
  arrange(desc(count))

# Set the factor levels for the plot
words_table <- words_table |>
  mutate(word = factor(word, levels = word[order(-count)]))

# Create the plot
plot <- ggplot(words_table, aes(x = word, y = count)) +
  geom_col(fill = "steelblue") +
  labs(
    x = "Words",
    y = "Count",
    title = "Lyrics"
  ) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Save the plot
ggsave("lyrics.png", plot = plot, width = 10, height = 6, dpi = 300)
