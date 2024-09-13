results <- read.table("tests.tsv", sep="\t")

results[ , 2] <- factor(
  results[ , 2],
  levels = c("gender", "1", "2"),
  labels = c("gender" ,"Male", "Female")
)

results$extroversion <-