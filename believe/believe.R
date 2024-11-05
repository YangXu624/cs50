# Define the encode function
encode <- function(mat) {
  rows <- nrow(mat)
  cols <- ncol(mat)
  result <- c()  # Initialize an empty vector to store the output

  # Traverse the matrix in a zigzag pattern
  for (sum_index in 1:(rows + cols - 1)) {
    if (sum_index %% 2 == 1) {
      # Odd sum_index: traverse bottom-left to top-right
      for (i in 0:(sum_index - 1)) {
        row <- sum_index - i
        col <- i + 1
        if (row <= rows && col <= cols) {
          result <- c(result, mat[row, col])
        }
      }
    } else {
      # Even sum_index: traverse top-right to bottom-left
      for (i in 0:(sum_index - 1)) {
        row <- i + 1
        col <- sum_index - i
        if (row <= rows && col <= cols) {
          result <- c(result, mat[row, col])
        }
      }
    }
  }

  # Concatenate the elements in result to form the output string
  paste(result, collapse = "")
}