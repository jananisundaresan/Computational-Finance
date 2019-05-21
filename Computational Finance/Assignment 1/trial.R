library(xts)
library(sparseIndexTracking)  
library(qrmtools)
        #install.packages("sparseIndexTracking")
data<- get_data(c("^FTSE"), from="2010-01-01",to="2010-12-30")
data<-data/1000000
# library(quantmod)
# tckrs <- c("SPY", "QQQ", "GDX", "DBO", "VWO")
# getSymbols(tckrs, from = "2015-01-01",to="2015-15-01")
# SPY <- SPY[,4]
# QQQ <- QQQ[,4]
# GDX<- GDX[,4]
# DBO<- DBO[,4]
# VWO<- VWO[,4]
# X<- cbind(SPY, QQQ, GDX, DBO, VWO,data)
# X<-X[complete.cases(X), ] 
# XX<-X[,-6]
# r<-X$X.FTSE
# ind<-INDEX_2010$SP500

CC<-cbind(INDEX_2010$X,data)
#w_ete <- spIndexTrack(X, r, lambda=log(100), u = 10, measure = "ete")
wete <- spIndexTrack(INDEX_2010$X, data, lambda = 1e-8, u = 1, measure = 'ete')
cat('Number of assets used:', sum(wete > 1e-6))




