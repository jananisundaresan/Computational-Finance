library(xts)
library(sparseIndexTracking)  
library(qrmtools)
library(quantmod)
library(Rcpp)
library(PerformanceAnalytics)
library(tidyquant)
library(ggplot2)
library(dplyr)
library(scales)
#install.packages("ggthemes")
library(ggthemes)
library(magrittr)
#install.packages("h2o")
library(h2o)
library(timetk)
library(zoo)
library(qrmtools)

#install.packages("sparseIndexTracking")
data<- get_data(c("^FTSE"), from="2010-01-01",to="2011-12-30")
data<-data/1000000

tckrs <- c("PRU","RIO","IAG","GSK","ABF.L","BATS.L","BRBY.L","EZJ.L","EXPN.L","HLMA.L","LLOY.L","SPY","MKS.L", "QQQ", "GDX", "DBO", "VWO","GOOGL","MSFT","AMZN","CPG","TSCO","BNZL.L","MRW.L")
getSymbols(tckrs, from = "2010-01-01",to="2011-12-31")
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
wete <- spIndexTrack(XX, r, lambda = 2e-5, u = 1, measure = 'ete')
cat('Number of assets used:', sum(wete > 1e-6))
X<- c(1e-2,2e-2,3e-2,4e-2,5e-2)
Y<- c(12,9,8,7,5)
a<-data.frame(X,Y)
R<-df <- df[!is.infinite(rowSums(df)),]
z<-data.frame(cumprod(1 + XX %*% wete$w))
z<-z[!is.infinite(rowSums(z)),]
v<-cumprod(1 + r)
plot(cbind("PortfolioETE" = z, v[1:230]), legend.loc = "topleft", main = "Cumulative P&L")

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

library(ggplot2)


# Charge the plotly library
library(plotly)

# Let's use the diamonds data set :
d <- diamonds[sample(nrow(diamonds), 1000), ]

# Make a basic scatter plot :
p <- plot_ly(a,x=X,y=Y,type = 'scatter', mode = 'lines',
             marker = list(size = 10,
                           color = 'rgba(255, 182, 193, .9)',
                           line = list(color = 'rgba(152, 0, 0, .8)',
                                       width = 2))) %>%
  layout(title = 'Sparse Index Tracking - Selection of Stocks',
         yaxis = list(zeroline = FALSE,title='Number of Stocks'),
         xaxis = list(zeroline = FALSE,title='Regularization Parameer - Lambda',titlefont = 20,tickfont=14))

