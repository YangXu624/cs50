# Read the tab-separated values file into a data frame
results <- read.table("tests.tsv", sep = "\t", header = TRUE)

# Step 1: Convert the second column to a factor with appropriate labels
results[, 2] <- factor(results[, 2], levels = c("1", "2"), labels = c("Male", "Female"))

# Step 2: Create new columns for the five personality traits
results$extroversion <- NA  # Predefine the extroversion column
results$neuroticism <- NA   # Predefine the neuroticism column
results$agreeableness <- NA  # Predefine the agreeableness column
results$conscientiousness <- NA  # Predefine the conscientiousness column
results$openness <- NA      # Predefine the openness column

# Step 3: Calculate the scores for each trait, ignoring the first row
for (i in 2:nrow(results)) {

  # Extroversion: sum columns 4 to 6 and divide by 15
  sum_extroversion <- sum(as.numeric(results[i, 4:6]), na.rm = TRUE)
  results$extroversion[i] <- round(sum_extroversion / 15, 2)

  # Neuroticism: sum columns 7 to 9 and divide by 15
  sum_neuroticism <- sum(as.numeric(results[i, 7:9]), na.rm = TRUE)
  results$neuroticism[i] <- round(sum_neuroticism / 15, 2)

  # Agreeableness: sum columns 10 to 12 and divide by 15
  sum_agreeableness <- sum(as.numeric(results[i, 10:12]), na.rm = TRUE)
  results$agreeableness[i] <- round(sum_agreeableness / 15, 2)

  # Conscientiousness: sum columns 13 to 15 and divide by 15
  sum_conscientiousness <- sum(as.numeric(results[i, 13:15]), na.rm = TRUE)
  results$conscientiousness[i] <- round(sum_conscientiousness / 15, 2)

  # Openness: sum columns 16 to 18 and divide by 15
  sum_openness <- sum(as.numeric(results[i, 16:18]), na.rm = TRUE)
  results$openness[i] <- round(sum_openness / 15, 2)
}

# Step 4: Create a new header and update the dataframe to use the correct column names
new_header <- results[1, ]  # Capture the first row as the header
df <- results[-1, ]         # Remove the first row from the data

# Rename the columns based on the new header
colnames(df) <- new_header
colnames(df)[colnames(df) == "1"] <- "gender"  # If "1" is a column, replace with "gender"

# Step 5: Write the cleaned-up data to a CSV file
write.csv(df, file = "analysis.csv", row.names = FALSE)
