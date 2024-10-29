authors <- read.csv("authors.csv")
books <- read.csv("books.csv")

# Writer
filter1 <- books$author == "Mia Morgan"
writer <- books[filter1, ]

# Musician
filter2 <- books$topic == "Music" & books$year == 1613
musician <- books[filter2, ]

# Traveler
filter3 <- (books$author == "Lysandra Silverleaf" | books$author == "Elena Petrova") & books$year == 1775
traveler <- books[filter3, ]

# Painter
filter4 <- (books$pages < 300 & books$pages > 200) & (books$year == 1990 | books$year == 1992)
painter <- books[filter4, ]

# Scientist
filter5 <- grepl("Quantum Mechanics", books$title)
scientist <- books[filter5, ]

zenthia <- subset(authors, hometown == "Zenthia")
filter6 <- books$author %in% zenthia$author & (books$year >= 1700 & books$year < 1800)
teacher <- books[filter6, ]
