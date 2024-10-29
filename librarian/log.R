authors <- read.csv("authors.csv")
books <- read.csv("books.csv")

filter1 <- books$author == "Mia Morgan"
mia_morgan <- books[filter1, ]

filter2 <- books$topic == "Music" & books$year == 1613
musician <- books[filter2, ]

filter3 <- (books$author == "Lysandra Silverleaf" | books$author == "Elena Petrova") & books$year == 1775
traveler <- books[filter3, ]

filter4 <- (books$pages < 300 & books$pages > 200) & (books$year == 1990 | books$year == 1992)
painter <- books[filter4, ]

filter5 <- grepl("Quantum Mechanics", books$title)
scientist <- books[filter5, ]

zenthia <- subset(authors, hometown == "Zenthia")
filter