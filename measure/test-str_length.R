library(testthat)
library(stringr)

test_that("str_length handles non-alphabetical characters correctly", {
  expect_equal(str_length(" "), 1)                    # Single whitespace
  expect_equal(str_length("!@#"), 3)                  # Punctuation
})

test_that("str_length returns NA for special values", {
  expect_equal(str_length(NA), NA_integer_)           # NA should return NA
})

test_that("str_length handles character vector inputs correctly", {
  expect_equal(str_length(c("apple", "banana", "cherry")), c(5, 6, 6))  # Vector of strings
})

test_that("str_length handles non-alphabetical characters correctly", {
  expect_equal(str_length("😊"), 1)                   # Emoji
  expect_equal(str_length("Hello 😊!"), 8)            # Mixed text and emoji
})