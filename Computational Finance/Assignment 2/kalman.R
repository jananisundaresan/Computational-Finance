#packages
library(ggplot2)
library(dplyr)
library(broom)
library(tidyr)
library(tidyverse)
library(plyr)
library(corrplot)
library(gridExtra)
library(scales)
library(corrplot)
library(car)
library(lars)
library(mlbench)
library(e1071)
library(grid)
library(cowplot)
library(xlsx)
library(ggpubr)
library(doBy)
library(rcompanion)
library(boot)
library(effsize)
library(psych)
library(plotly)
library(imputeTS)
library(Rserve)
library(tseries)
library(astsa)
library(forecast)
library(imputeTS)
library(Rserve)
library(tseries)
library(astsa)
library(fUnitRoots)
library(urca)
library(vars)
library(aod)
library(zoo)
library(tseries)
library(lmtest)
library(CausalImpact)
library(ISwR)
attach(Theoph)
library(faraway)
library(MASS)
library(lars)
library(broom)
library(ResourceSelection)
library(ggplot2)
library(forecast)
library(plotly)
library(ggfortify)
library(tseries)
library(gridExtra)
library(docstring)
library(readr)
library(here)

#read data

data<- read.csv("C:/users/Janani/Desktop/2019/Computational Finance/Assignment 2/GSPC.csv")
attach(data)
plot_time_series <- function(ts_object, ts_object_name){
  
  if (is.ts(ts_object) == TRUE){
    
    if(missing(ts_object_name)) {
      
      warning('Title for plot not entered!')
      
    } else {
      
      startYear <- start(ts_object) # Grabs start date
      
      endYear <- end(ts_object) # Grabs end date
      
      tsPlot <- autoplot(ts_object,
                         
                         ts.colour = 'turquoise4',
                         
                         size = 1,
                         
                         main = sprintf("Plot of %s Time Series (%s - %s)",
                                        
                                        ts_object_name, startYear[1], endYear[1])) +
        
        theme(axis.text.x = element_text(angle = 35, hjust = 1),
              
              panel.background = element_rect(fill = "gray98"),
              
              axis.line.x = element_line(colour="gray"),
              
              axis.line.y = element_line(colour="gray")) +
        
        labs(x = "Year", y = "Closing Values") 
      
      return(tsPlot)
      
    }
    
  }
  
  else {
    
    warning('Make sure object entered is time-series object!')
    
  }
  
}
sp_500 <- ts(data$Adj.Close, start=c(1995, 1), freq=12)
plot_time_series(sp_500, 'S&P 500')

sp500_training <- ts(sp_500, start=c(1995, 1), end=c(2014, 12), freq=12)
Box.test(sp_500, lag = 20, type = 'Ljung-Box')
adf.test(sp500_training)

plot_decomp <- function(ts_object, ts_object_name){
  
  #' Plots Seasonal Decomposition for Time Series Object
  
  #'
  
  #' Decomposes time series object to \emph{Seasonal},
  
  #' \emph{Remainder}, and \emph{Trend}.
  
  #' Utilizing \code{ggplot2} with custom themes to ensure plots are
  
  #' consistent. Utlizes \code{autoplot} function for plots.
  
  #'
  
  #' @param ts_object time series object used to create plot
  
  #' @param ts_object_name preferred title of plot
  
  #' @examples
  
  #' data(AirPassengers)
  
  #'
  
  #' air_pass_ts <- as.ts(AirPassengers)
  
  #'
  
  #' plot_decomp(air_pass_ts, 'Air Passengers Data Set')
  
  if (is.ts(ts_object) == TRUE){
    
    autoplot(stl(ts_object, s.window = "periodic"),
             
             main = sprintf("Decomposition Plot of %s", ts_object_name),
             
             ts.colour = "orange") +
      
      theme(panel.background = element_rect(fill = "gray98"),
            
            axis.line.y   = element_line(colour="gray"),
            
            axis.line.x = element_line(colour="gray"))
    
  } else {
    
    warning('Make sure object entered is time-series object!')
    
  }
  
}
plot_decomp(sp500_training, 'S&P 500')
Acf(sp500_training, type="correlation", lag=20, main="ACF S&P INDEX 500P")

plot_acf_pacf <- function(ts_object, ts_object_name){
  
  #' Plot ACF and PACF for Time Series Object
  
  #'
  
  #' Creates \emph{Autocorrelation} and \emph{Partial Autocorrelation} plot
  
  #' utilizing \code{ggplot2} with custom themes to ensure plots are
  
  #' consistent. Utlizes \code{autoplot} function for plots.
  
  #'
  
  #' @param ts_object time series object used to create plot
  
  #' @param ts_object_name preferred title of plot
  
  #' @examples
  
  #' data(AirPassengers)
  
  #'
  
  #' air_pass_ts <- as.ts(AirPassengers)
  
  #'
  
  #' plot_acf_pacf(air_pass_ts, 'Air Passengers Data Set')
  
  if (is.ts(ts_object) == TRUE){
    
    if(missing(ts_object_name)) {
      
      warning('Title for plot not entered!')
      
    } else {
      
      a <- autoplot(acf(ts_object, plot = FALSE),
                    
                    colour = 'turquoise4',
                    
                    conf.int.fill = '#4C4CFF',
                    
                    conf.int.value = 0.95, conf.int.type = 'ma') +
        
        theme(panel.background = element_rect(fill = "gray98"),
              
              axis.line.y   = element_line(colour="gray"),
              
              axis.line.x = element_line(colour="gray")) +
        
        ggtitle(sprintf("ACF plot of %s", ts_object_name))
      
      
      
      b <- autoplot(pacf(ts_object, plot = FALSE),
                    
                    colour = 'turquoise4',
                    
                    conf.int.fill = '#4C4CFF',
                    
                    conf.int.value = 0.95, conf.int.type = 'ma') +
        
        theme(panel.background = element_rect(fill = "gray98"),
              
              axis.line.y   = element_line(colour="gray"),
              
              axis.line.x = element_line(colour="gray")) + labs(y="PACF") +
        
        ggtitle(sprintf("PACF plot of %s", ts_object_name))
      
      
      
      grid.arrange(a, b)
      
    }
    
  } else {
    
    warning('Make sure object entered is time-series object!')
    
  }
  
}

plot_acf_pacf(sp500_training, 'S&P 500')

tsDiff <- diff(sp500_training)
plot_time_series(tsDiff, 'First Difference')
plot_acf_pacf(tsDiff, 'First Difference Time Series Object')
fit <- Arima(sp500_training, order = c(3,1,1),
             include.drift = TRUE)
summary(fit)
ggtsdiag_custom <- function(object, ts_object_name, gof.lag = 10,
                            
                            conf.int = TRUE,
                            
                            conf.int.colour = '#0000FF', conf.int.linetype = 'dashed',
                            
                            conf.int.fill = NULL, conf.int.alpha = 0.3,
                            
                            ad.colour = '#888888', ad.linetype = 'dashed', ad.size = .2,
                            
                            nrow = NULL, ncol = 1, ...) {
  
  rs <- stats::residuals(object)
  
  if (is.null(rs)) {
    
    rs <- object$residuals
    
  }
  
  if (is.null(rs)) {
    
    rs <- object$resid
    
  }
  
  
  
  p.std <- ggplot2::autoplot(rs, na.action = stats::na.pass,
                             
                             ts.colour = 'turquoise4', size = 1.05) +
    
    ggplot2::geom_hline(yintercept = 0,
                        
                        linetype = ad.linetype, size = ad.size,
                        
                        colour = ad.colour) +
    
    labs(subtitle = '') +
    
    ggplot2::ggtitle(sprintf("Residual Diagnostics for %s \nNon-Standardized Residuals",
                             
                             ts_object_name))
  
  
  
  acfobj <- stats::acf(rs, plot = FALSE, na.action = stats::na.pass)
  
  p.acf <- autoplot(acfobj, conf.int = conf.int,
                    
                    conf.int.colour = conf.int.colour,
                    
                    conf.int.linetype = conf.int.linetype,
                    
                    conf.int.fill = conf.int.fill,
                    
                    conf.int.alpha = conf.int.alpha,
                    
                    colour = 'turquoise4', size = 1.25)
  
  p.acf <- p.acf + ggplot2::ggtitle('ACF of Residuals')
  
  
  
  nlag <- gof.lag
  
  pval <- numeric(nlag)
  
  for (i in 1L:nlag) pval[i] <- stats::Box.test(rs, i, type = "Ljung-Box")$p.value
  
  lb.df <- data.frame(Lag = 1L:nlag, `p value` = pval,
                      
                      lower = -0.05, upper = 0.05)
  
  # Unnable to create column with space by above expression
  
  colnames(lb.df) <- c('Lag', 'p value', 'lower', 'upper')
  
  p.lb <- ggplot2::ggplot(data = lb.df, mapping = ggplot2::aes_string(x = 'Lag')) +
    
    ggplot2::geom_point(mapping = ggplot2::aes_string(y = '`p value`'), na.rm = TRUE,
                        
                        colour = 'turquoise4') +
    
    ggplot2::scale_y_continuous(limits=c(-0.1, 1)) +
    
    ggplot2::ggtitle('p values for Ljung-Box statistic')
  
  
  
  p.lb <- ggfortify:::plot_confint(p = p.lb, data = lb.df, conf.int = conf.int,
                                   
                                   conf.int.colour = conf.int.colour,
                                   
                                   conf.int.linetype = conf.int.linetype,
                                   
                                   conf.int.fill = conf.int.fill, conf.int.alpha = conf.int.alpha)
  
  
  
  if (is.null(ncol)) { ncol <- 0 }
  
  if (is.null(nrow)) { nrow <- 0 }
  
  new('ggmultiplot', plots = list(p.std, p.acf, p.lb), nrow = nrow, ncol = ncol)
  
}


ggtsdiag_custom(fit,'ARIMA(3,1,1)') +
  theme(panel.background = element_rect(fill = "gray98"),
        panel.grid.minor = element_blank(),
        axis.line.y = element_line(colour="gray"),
        axis.line.x = element_line(colour="gray"))

residFit <- ggplot(data=fit, aes(residuals(fit))) +
  geom_histogram(aes(y =..density..),
                 binwidth = 5,
                 col="turquoise4", fill="white") +
  geom_density(col=1) +
  theme(panel.background = element_rect(fill = "gray98"),
        panel.grid.minor = element_blank(),
        axis.line   = element_line(colour="gray"),
        axis.line.x = element_line(colour="gray")) +
  ggtitle("Plot of SP 500 ARIMA Model Residuals")

for_sp500_all <- forecast(fit, h = 12)
sp500_test <- window(sp_500, 2015, c(2015, 12))
round(accuracy(for_sp500_all, sp500_test), 3)
