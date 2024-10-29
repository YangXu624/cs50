flavor <- readline(prompt = "Flavor: ")
if (flavor == "Light") {
  caffeine <- readline(prompt = "Caffeine: ")
  if (caffeine == "Yes") {
    cat("Green tea")
  } else if (caffeine == "No") {
    cat("Chamomile tea")
  } else {
    cat("Invalid Choice. Caffeine is either Yes or No.")
  }
} else if (flavor == "Bold") {
  caffeine <- readline(prompt = "Caffeine: ")
  if (caffeine == "Yes") {
    cat("Black tea")
  } else if (caffeine == "No") {
    cat("Rooibos tea")
  } else {
    cat("Invalid Choice. Caffeine is either Yes or No.")
  }
} else {
  cat("Invalid Choice. Flavor is either Light or Bold.")
}