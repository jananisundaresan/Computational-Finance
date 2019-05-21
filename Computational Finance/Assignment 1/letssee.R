library(xts)
library(sparseIndexTracking)  
library(qrmtools)
#install.packages("sparseIndexTracking")
data<- get_data(c("^FTSE"), from="2010-01-01",to="2012-12-30")
data<-data/1000000
library(quantmod)
tckrs <- c("PRU","RIO","IAG","GSK","ABF.L","BATS.L","BRBY.L","EZJ.L","EXPN.L","HLMA.L","LLOY.L","SPY","MKS.L", "QQQ", "GDX", "DBO", "VWO","GOOGL","MSFT","AMZN","CPG","TSCO","BNZL.L","MRW.L")
getSymbols(tckrs, from = "2010-01-01",to="2012-12-31")
PRU<- PRU[,4]
RIO<- RIO[,4]
IAG<- IAG[,4]
EVR<- EVR[,4]
GSK<- GSK[,4]
ABF.L<- ABF.L[,4]
BATS.L<- BATS.L[,4]
BRBY.L<- BRBY.L[,4]
EZJ.L<- EZJ.L[,4]
EXPN.L <- EXPN.L[,4]
HLMA.L <- HLMA.L[,4]
LLOY.L<- LLOY.L[,4]
SPY<- SPY[,4]
MKS.L<- MKS.L[,4]
QQQ <- QQQ[,4]
GDX<- GDX[,4]
DBO<- DBO[,4]
VWO<- VWO[,4]
GOOGL <- GOOGL[,4]
MSFT <- MSFT[,4]
AMZN<- AMZN[,4]
CPG<- CPG[,4]
TSCO<- TSCO[,4]
BNZL.L<- BNZL.L[,4]
MRW.L<- MRW.L[,4]
#new<-INDEX_2010$X[,c("XRX UN Equity","BK UN Equity","VMC UN Equity","VAR UN Equity","WY UN Equity")]
X<- cbind(data,PRU,RIO,IAG,EVR,GSK,ABF.L,BATS.L,BRBY.L,EZJ.L,EXPN.L,HLMA.L,LLOY.L,SPY,MKS.L, QQQ, GDX, DBO, VWO,GOOGL,MSFT,AMZN,CPG,TSCO,BNZL.L,MRW.L)
X<-X[complete.cases(X), ]
print(dim(X))
XX<-X[,-1]
r<-X$X.FTSE
library(tidyquant)
#new<-as.xts(X, date_col = X$X.FTSE)
#w_ete <- spIndexTrack(new[,-6], new, lambda=log(100), u = 10, measure = "ete")
wete <- spIndexTrack(XX, r, lambda = 4e-5, u = 1, measure = 'ete')
cat('Number of assets used:', sum(wete > 1e-6))


# -11e-5 -10
#1e-6 12
#4e-5 10 from="2010-01-01",to="2012-12-30")
#without new -1e-5
# nn<-cbind(new,data,h)
# X<-nn[complete.cases(nn), ]
# XX<-X[,-6]
# r<-X$X.FTSE
# wete <- spIndexTrack(XX, r, lambda = 0.1e-5, u = 1, measure = 'ete')
# cat('Number of assets used:', sum(wete > 1e-6))
