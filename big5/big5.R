results <- read.table("tests.tsv", sep = "\t", header = TRUE)

results$gender <- factor(
results$gender,
labels = c("Unanswered", "Male", "Female", "Other")
)

results$extroversion <- round((results$E1 + results$E2 + results$E3) / 15, 2)
results$neuroticism <- round((results$N1 + results$N2 + results$N3) / 15, 2)
results$agreeableness <- round((results$A1 + results$A2 + results$A3) / 15, 2)
results$conscientiousness <- round((results$C1 + results$C2 + results$C3) / 15, 2)
results$openness <- round((results$O1 + results$O2 + results$O3) / 15, 2)


write.csv(results, "analysis.csv", row.names = FALSE)
