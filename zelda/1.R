zelda <- read.csv("zelda.csv")

zelda <- pivot_wider(
  zelda,
  id_cols = c(title, release),
  names_from = role,
  values_from = names
)

# Step 1: Split the release column into year and system
split_release <- strsplit(zelda$release, " - ")

zelda$year <- sapply(split_release, `[`, 1)   # Get the first element (year)
zelda$system <- sapply(split_release, `[`, 2) # Get the second element (system)

# Step 2: Remove the original release column
zelda$release <- NULL

# Step 3: Reorder the columns
zelda <- zelda[, c(names(zelda)[1], "year", "system", setdiff(names(zelda), c(names(zelda)[1], "year", "system")))]

names(zelda) <- tolower(names(zelda))

zelda <- as_tibble(zelda)

save(zelda, file = zel)