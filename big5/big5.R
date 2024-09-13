results <- read.table("tests.tsv", sep="\t")

results[, 2] <- factor(
  results[, 2],
  levels = c("gender", "1", "2"),
  labels = c("gender" ,"Male", "Female")
)

results$extroversion[1] <- "extroversion"
for (i in 2:nrow(results)){
  sum <- 0
  for (j in 4:6) {
    sum <- sum + as.numeric(results[i, j])
  }
  results$extroversion[i] <- sum
}

results$extroversion[1] <- "extroversion"
for (i in 2:nrow(results)){
  sum <- 0
  for (j in 4:6) {
    sum <- sum + as.numeric(results[i, j])
  }
  results$extroversion[i] <- sum
}

df <- results
new_header <- df[1, ]
df <- df[-1, ]  # Remove the first row from the data frame
colnames(df) <- new_header  # Set new column names
colnames(df)[colnames(df) == "1"] <- "gender"
write.csv(df, file = "analysis.csv", row.names = FALSE)

table <- read.csv("analysis.csv")
