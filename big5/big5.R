results <- read.table("tests.tsv", sep="\t")

results[2, ] <- factor(
  results[2, ],
  levels = c("1", "2"),
  labels = c("Male", "Female")
)

