filename <- readline("File: ")
pitstops <- read.csv(filename)
num_pitstops <- nrow(pitstops)

sorted_pitstops <- pitstops[order(pitstops$time), ]
first <- sorted_pitstops[1, ]
last <- sorted_pitstops[num_pitstops, ]

total_time <- sum(pitstops$time)

print(paste("Number of pitstops: ", num_pitstops))
print(paste("Fastest time: ", first$time))
print(paste("Slowest time: ", last$time))
print(paste("Total time: ", total_time))