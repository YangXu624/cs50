zelda <- read.csv("zelda.csv")

zelda <- pivot_wider(
  zelda,
  id_cols = c(title, release),
  names_from = role,
  values_from = names
)

# Assuming zelda$release contains strings like "1998 - Nintendo 64"

# Split the release column
split_release <- strsplit(zelda$release, " - ")

# Extract year and system
zelda$year <- sapply(split_release, `[`, 1)   # Get the first element (year)
zelda$system <- sapply(split_release, `[`, 2) # Get the second element (system)


names(zelda) <- tolower(names(zelda))

View(zelda)