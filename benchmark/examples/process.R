#!/usr/bin/R

d <- read.csv('output.csv',header=TRUE)
d

mean(d$text)
