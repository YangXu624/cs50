random_character <- function() {
  return(sample(letters))
}

print_sequence <- function(length) {
  for (i in 1:20) {
    cat(random_character)
    Sys.sleep(0.25)
  }
}

print_sequence