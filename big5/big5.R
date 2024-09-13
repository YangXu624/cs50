results <- read.table("tests.tsv", sep="\t")

results[, 2] <- factor(
  results[, 2],
  levels = c("gender", "1", "2"),
  labels = c("gender" ,"Male", "Female")
)

results[5, 4:6] <- lapply(results[5, 4:6], as.numeric)
print(class(results[5, 4:6]))
ex <- sum(results[5, 4:6]) / 15
results$extroversion <-c("ex")