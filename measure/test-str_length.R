library(stringr)
library(testthat)

test_that("'str_length' returns length of string", {
  expect_equal(str_length("abcdefg"), 7)
  expect_equal(str_length("ab3d fg"), 7)
  expect_true(is.na(str_length(NA)))
  expect_equal(str_length(Inf), NA)
})

test_that("'str_length' returns length of vector", {
  expect_equal(str_length(c(1, 2, 3, 4)), 4)
})