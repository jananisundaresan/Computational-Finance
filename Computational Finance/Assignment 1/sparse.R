library(xts)
library(sparseIndexTracking)  #install.packages("sparseIndexTracking")
library(ggplot2)
library(dplyr)
library(scales)
#install.packages("ggthemes")
library(ggthemes)
library(magrittr)
#install.packages("h2o")
library(h2o)
library(timetk)
library(tidyquant) 


if (!require("quantmod")) {
  install.packages("quantmod")
  library(quantmod)
}
start <- as.Date("2015-01-01")
end <- as.Date("2015-01-31")

getSymbols(c("EZJ,SGE,GVC"), src = "yahoo", from = start, to = end)
stocks <- as.xts(data.frame( EZJ = EZJ[, "EZJ.Close"],SGE = SGE[, "SGE.Close"],GVC = GVC[, "GVC.Close"]
                            ))
# write.zoo(stocks, file="C:/Users/Janani/Desktop/2019/s.zoo", sep=",")
# write.zoo(FTSE, file="C:/Users/Janani/Desktop/2019/f.zoo", sep=",")
# FTSE<-FTSE[1:30,]
# EZJ <- EZJ[1:30,]
# SGE<- SGE[1:30,]
# GVC<-GVC[1:30,]

X_train <- stocks[1:20] 
X_test <- stocks[21:30] 
r_train <- FTSE[1:20] 
r_test <- FTSE[21:30]

w_ete <- spIndexTrack(X_train, r_train, lambda = 0.001, u = 0.5, measure = 'ete') 
cat('Number of assets used:', sum(w_ete > 1e-6))