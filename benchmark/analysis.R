#!/usr/bin/R

library(rjson)

args <- commandArgs(TRUE)
config <- fromJSON(file=args[1])

print(c("./analysis.R", config$topdatacsv))

d <- read.csv(config$topdatacsv,header=TRUE)

mean(d$rank)
length(d$rank)

