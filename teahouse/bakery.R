flavor <- readline(prompt = "Flavor: ")
caffeine <- readline(prompt = "Caffeine: ")

if (flavor != "Sweet" & flavor != "Savory") {
  cat("Invalid Choice. Flavor is either Sweet or Savory.\n")
}

if (caffeine != "Yes" & caffeine != "No") {
  cat("Invalid Choice. Caffeine is either Yes or No.\n")
}

if (flavor == "Light") {
  if (caffeine == "Yes") {
    cat("green tea")
  } else {
    cat("chamomile tea")
  }
} else {
  if (caffeine == "Yes") {
    cat("black tea")
  } else if (caffeine == "No") {
    cat("rooibos tea")
  }
}