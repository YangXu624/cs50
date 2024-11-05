library(testthat)
source("believe.R")

test_that("Matrix 1 is encoded appropriately", {
  expect_equal(encode(matrix(1:9, nrow = 3, ncol = 3, byrow = TRUE)), "124753689")
})

test_that("Matrix 2 is encoded appropriately", {
  expect_equal(encode(matrix(0, nrow = 1, ncol = 1, byrow = TRUE)), "0")
})

test_that("Function raises error for non-matrix inputs", {
  expect_error(encode("hello :)"))
})

test_that("Matrix 2 is encoded appropriately", {
  expect_equal(encode(matrix(0:8, nrow = 3, ncol = 3, byrow = TRUE)), "013642578")
})