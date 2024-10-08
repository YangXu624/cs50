# Read the tab-separated values file into a data frame
results <- read.table("tests.tsv", sep = "\t", header = TRUE)

# Step 1: Convert the second column to a factor with appropriate labels
results$gender <- factor(
data$gender,
labels = c("Unanswered", "Male", "Female", "Other")
)

results$extroversion <- round((data$E1 + data$E2 + data$E3) / 15, 2)
results$neuroticism <- round((data$N1 + data$N2 + data$N3) / 15, 2)
results$agreeableness <- round((data$A1 + data$A2 + data$A3) / 15, 2)
results$conscientiousness <- round((data$C1 + data$C2 + data$C3) / 15, 2)
results$openness <- round((data$O1 + data$O2 + data$O3) / 15, 2)


write.csv(results, "analysis.csv", row.names = FALSE)
