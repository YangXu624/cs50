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
  results$extroversion[i] <- round(sum / 15, 2)
}

results$neuroticism[1] <- "neuroticism"
for (i in 2:nrow(results)){
  sum <- 0
  for (j in 7:9) {
    sum <- sum + as.numeric(results[i, j])
  }
  results$neuroticism[i] <- round(sum / 15, 2)
}

results$agreeableness[1] <- "agreeableness"
for (i in 2:nrow(results)){
  sum <- 0
  for (j in 10:12) {
    sum <- sum + as.numeric(results[i, j])
  }
  results$agreeableness[i] <- round(sum / 15, 2)
}

results$conscientiousness[1] <- "conscientiousness"
for (i in 2:nrow(results)){
  sum <- 0
  for (j in 13:15) {
    sum <- sum + as.numeric(results[i, j])
  }
  results$conscientiousness[i] <- round(sum / 15, 2)
}

results$openness[1] <- "openness"
for (i in 2:nrow(results)){
  sum <- 0
  for (j in 16:18) {
    sum <- sum + as.numeric(results[i, j])
  }
  results$openness[i] <- round(sum / 15, 2)
}

df <- results
new_header <- df[1, ]
df <- df[-1, ]  # Remove the first row from the data frame
colnames(df) <- new_header  # Set new column names
colnames(df)[colnames(df) == "1"] <- "gender"
write.csv(df, file = "analysis.csv", row.names = FALSE)

table <- read.csv("analysis.csv")
View(table)
