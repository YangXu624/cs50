flavor <- readline(prompt = "Flavor: ")
caffeine <- readline(prompt = "Caffeine: ")

if (flavor != "Sweet" & flavor != "Savory") {
  cat("Invalid Choice. Flavor is either Sweet or Savory.\n")
}

if (caffeine != "Yes" & caffeine != "No") {
  cat("Invalid Choice. Caffeine is either Yes or No.\n")
}

if (flavor == "Sweet") {
  if (caffeine == "Yes") {
    cat("coffee bun")
  } else {
    cat("red bean bun")
  }
} else {
  if (caffeine == "Yes") {
    cat("sugarless coffee bun")
  } else if (caffeine == "No") {
    cat("sausage bun")
  }
}