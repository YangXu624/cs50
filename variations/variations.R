random_character <- function() {
  return(sample(letters))
}

print_sequence <- function(length) {
  seq <- random_character()
  for (i in 1:length) {
    cat(seq[i])
    Sys.sleep(0.25)
  }
}

print_sequence(20)