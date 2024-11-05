library(testthat)
library(stringr)

# Test 1: Non-alphabetical characters (whitespace, punctuation, emoji)
test_that("str_length handles non-alphabetical characters correctly", {
  expect_equal(str_length(" "), 1)                    # Single whitespace
  expect_equal(str_length("!@#"), 3)                  # Punctuation
  expect_equal(str_length("😊"), 1)                   # Emoji
  expect_equal(str_length("Hello 😊!"), 8)            # Mixed text and emoji
})

# Test 2: Special values (NA, NaN, Inf, -Inf)
test_that("str_length returns NA for special values", {
  expect_equal(str_length(NA), NA_integer_)           # NA should return NA
  expect_error(str_length(NaN), "expecting a character")  # NaN is not valid input
  expect_error(str_length(Inf), "expecting a character")  # Inf is not valid input
  expect_error(str_length(-Inf), "expecting a character") # -Inf is not valid input
})

# Test 3: Vector inputs (character vector)
test_that("str_length handles character vector inputs correctly", {
  expect_equal(str_length(c("apple", "banana", "cherry")), c(5, 6, 6))  # Vector of strings
})

# Test 4: Data frame as input
test_that("str_length errors when given a data frame as input", {
  df <- data.frame(x = c("a", "bb", "ccc"))
  expect_error(str_length(df), "expecting a character") # Data frames are invalid input
})
