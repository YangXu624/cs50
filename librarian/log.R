authors <- read.csv("authors.csv")
books <- read.csv("books.csv")

filter1 <- books$author == "Mia Morgan"
mia_morgan <- books[filter1, ]

filter2 <- books$topic == "Music" &