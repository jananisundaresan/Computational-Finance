library(ggpmisc)
sp_500 <- ts(data$Adj.Close[1:122], start=c(1995, 1), freq=12)
ggplot(tsDiff, as.numeric = FALSE) + geom_line() + 
  stat_peaks(colour = "red") +
  stat_peaks(geom = "text", colour = "red", 
             vjust = -0.5, x.label.fmt = "%Y") +
  stat_valleys(colour = "blue") +
  stat_valleys(geom = "text", colour = "blue", angle = 45,
               vjust = 1.5, hjust = 1,  x.label.fmt = "%Y")+
  ylim(300, 1600)+ggtitle("Plot of S&P index for 1995 - 2004")+
  theme(plot.title = element_text(hjust = 0.5))+
  xlab("1/1/1995 - 12/31/2004") + ylab("S&P Index 500") 

sp_5001 <- ts(data$Adj.Close[123:260], start=c(2005, 1), freq=12)
ggplot(sp_5001, as.numeric = FALSE) + geom_line() + 
  stat_peaks(colour = "red") +
  stat_peaks(geom = "text", colour = "red", 
             vjust = -0.5, x.label.fmt = "%Y") +
  stat_valleys(colour = "blue") +
  stat_valleys(geom = "text", colour = "blue", angle = 45,
               vjust = 1.5, hjust = 1,  x.label.fmt = "%Y")+
  ylim(500, 2250)+ggtitle("Plot of S&P index for 2005 - 2015")+
  theme(plot.title = element_text(hjust = 0.5))+
  xlab("1/1/2005 - 12/31/2015") + ylab("S&P Index 500") 

data1<- read.csv("C:/users/Janani/Desktop/2019/Computational Finance/Assignment 2/GSPC.csv")
one<- as.data.frame(sp_500[1:130])
two

acf_rugarch = function(x, ...)
{   
  T = length(x)
  insample = 1:T
  xseries = x
  lag.max = as.integer(10*log10(T))
  acfx    = acf(xseries, lag.max = lag.max, plot = FALSE)
  clim0   = qnorm((1 + 0.95)/2)/sqrt(acfx$n.used)
  ylim 	= range(c(-clim0, clim0, as.numeric(acfx$acf)[-1]))
  xlim=range(0,2,0.25)
  clx     = vector(mode = "character", length = lag.max)
  clx[which(as.numeric(acfx$acf)[-1]>=0)] = "steelblue"
  clx[which(as.numeric(acfx$acf)[-1]<0)] = "orange"
  barplot(height = as.numeric(acfx$acf)[-1], names.arg = as.numeric(acfx$lag)[-1], ylim = 1.2*ylim, col = clx,
          ylab = "ACF", xlab="Lag", main = "ACF of S&P INDEX 500", cex.main = 0.8)
  abline(h = c(clim0, -clim0), col = "tomato1", lty = 2)
  abline(h = 0, col = "black", lty = 1)
  box()   
  grid()
}


acf_rugarch(na.omit(diff(tsDiff)))

p <- ggplot(data = tsDiff) + 
  geom_line(color = "#00AFBB", size = 1)+ggtitle("Plot of First Difference")
p
# Set axis limits c(min, max)
min <- as.Date("1995-1-1")
max <- NA
p + scale_x_date(limits = c(min, max))

# Fit the AR model to x
AR <- arima(sp_5001, order = c(2,1,1))
ts.plot(sp500_training)
AR_fitted <- sp_5001 - residuals(AR)
points(AR_fitted, type = "l", col = 2, lty = 2)
title("Third Order AutoRegressive Model Fitted vs Residuals")

phi <- 0.6; sig.eta <- 1; sig.epsilon <- 2.5
#data1<- read.csv("C:/users/Janani/Desktop/2019/Computational Finance/Assignment 2/GSPC.csv")
#n<- (sp_500)

n <- 267
## simulate AR(1) + noise
y <- arima.sim(n = n, list(ar = phi, ma = numeric(0), sd = 1))
y <- y + rnorm(n, sd = sig.epsilon)
plot(y, type = "o", pch = 16, cex = 0.6)
## write the State Space model
mod <- list(T = phi,  Z = 1, h = sig.epsilon^2, V = sig.eta^2)
## initialisation part
P <- sig.eta^2 / (1-phi^2)
mod <- c(mod, list(a = 0, P = P, Pn = P))
## smooth
res <- KalmanSmooth(y = y, mod = mod, nit = -1)
lines(res$smooth, col = "orangered", lwd = 2)
legend("topleft", lty = rep(1, 1), lwd = c(1, 2),
       pch = c(16, NA), col = c("black", "orangered"),
       legend = c("S&P index", "a (smoothed)"))
