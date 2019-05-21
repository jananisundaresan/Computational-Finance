library(quadprog)
library(IntroCompFinR)
library(PerformanceAnalytics)
library(zoo)
cex.val=1
asset.names <- c("GVC", "STAN", "NMC")
mu.vec = c(0.11,0.01,0.26)
names(mu.vec) = asset.names
sigma.mat = matrix(c(0.000259, 0.000036, 0.000048,
                     0.000036, 0.000518, 0.000067,
                     0.000048, 0.000067, 0.000458),
                   nrow=3, ncol=3)
dimnames(sigma.mat) = list(asset.names, asset.names)
r.f = 0.005
mu.vec
sd.vec = sqrt(diag(sigma.mat))
cov2cor(sigma.mat)

plot(sd.vec, mu.vec,  ylim=c(-0.5, 0.5), xlim=c(-0.5, 0.5), ylab="Mean Return",
     xlab="Volatility", pch=16, col="blue", cex=1.75, cex.lab=1.75)  + scale_x_continuous(breaks = seq(-0.5,0.5,by =0.1))   
text(sd.vec, mu.vec, labels=asset.names, pos=4, cex = cex.val)
text(0, r.f, labels=expression(r[f]), pos=2, cex = cex.val) +title("Mean-Voltality Portfolio")

#quadrop
D.mat = 2*sigma.mat
d.vec = rep(0, 3)
A.mat = cbind(rep(1,3), diag(3))
b.vec = c(1, rep(0,3))

args(solve.QP)
qp.out = solve.QP(Dmat=D.mat, dvec=d.vec,
                  Amat=A.mat, bvec=b.vec, meq=1)
class(qp.out)
names(qp.out)
qp.out$solution
sum(qp.out$solution)
qp.out$value

## Use the quadprog function <code>solve.QP()</code> to compute global minimum variance portfolio

#Compute the mean and volatility of the minimum variance portfolio
# Expected return
er.gmin.ns = as.numeric(crossprod(qp.out$solution, mu.vec))
# Volatility
sd.gmin.ns = sqrt(qp.out$value)

er.gmin.ns
sd.gmin.ns

args(globalMin.portfolio)
gmin.port = globalMin.portfolio(mu.vec, sigma.mat,
                                shorts=FALSE)
gmin.port

eMsft.port = efficient.portfolio(mu.vec, sigma.mat, target.return = mu.vec["STAN"])
eMsft.port

D.mat = 2*sigma.mat
d.vec = rep(0, 3)
A.mat = cbind(mu.vec, rep(1,3), diag(3))
b.vec = c(mu.vec["MSFT"], 1, rep(0,3))

qp.out = solve.QP(Dmat=D.mat, dvec=d.vec,
                  Amat=A.mat, bvec=b.vec, meq=2)
names(qp.out$solution) = names(mu.vec)
round(qp.out$solution, digits=3)
efficient.portfolio(mu.vec, sigma.mat, target.return = mu.vec["STAN"], shorts = FALSE)


ef = efficient.frontier(mu.vec, sigma.mat, alpha.min=0, 
                        alpha.max=1, nport=10)
ef$weights

plot(ef$sd, ef$er, type="b", ylim=c(0, 0.3), xlim=c(0, 0.05), 
     pch=16, col="blue", cex=2, ylab=expression(mu[p]), xlab=expression(sigma[p]))
points(sd.vec, mu.vec, pch=16, col="black", cex=2)
text(sd.vec, mu.vec, labels=asset.names, pos=4)
text(ef$sd[1], ef$er[1], labels="port 10", pos=4)
text(ef$sd[2], ef$er[2], labels="port 9", pos=4)

mu.vals = seq(gmin.port$er, max(mu.vec), length.out=10)
w.mat = matrix(0, length(mu.vals), 3)
sd.vals = rep(0, length(sd.vec))
colnames(w.mat) = names(mu.vec)
D.mat = 2*sigma.mat
d.vec = rep(0, 3)
A.mat = cbind(mu.vec, rep(1,3), diag(3))
for (i in 1:length(mu.vals)) {
  b.vec = c(mu.vals[i],1,rep(0,3))
  qp.out = solve.QP(Dmat=D.mat, dvec=d.vec,
                    Amat=A.mat, bvec=b.vec, meq=2)
  w.mat[i, ] = qp.out$solution
  sd.vals[i] = sqrt(qp.out$value)
}

plot(ef$sd, ef$er, type="b", ylim=c(0, 0.3), xlim=c(0.01, 0.025), 
     pch=16, col="blue", cex=2, ylab=expression(mu[p]), xlab=expression(sigma[p]))
points(sd.vec, mu.vec, pch=16, col="black", cex=2)
text(sd.vec, mu.vec, labels=asset.names, pos=4)
points(sd.vals, mu.vals, type="b", pch=16, col="red", cex=1.5)
text(ef$sd[1], ef$er[1], labels="port 10", pos=2)
text(ef$sd[2], ef$er[2], labels="port 9", pos=2)

ef.ns = efficient.frontier(mu.vec, sigma.mat, alpha.min=0, 
                           alpha.max=1, nport=10, shorts=FALSE)
ef.ns$weights

plot(ef$sd, ef$er, type="b", ylim=c(0, 0.3), xlim=c(0.01,0.025), ylab="Mean Return",
     xlab="Volatility",
     pch=16, col="blue", cex=2)+title("Efficient Frontier - Shortsale vs No Shortsale")
points(sd.vec, mu.vec, pch=16, col="black", cex=2)
text(sd.vec, mu.vec, labels=asset.names, pos=4)
points(ef.ns$sd, ef.ns$er, type="b", pch=16, col="red")
text(ef$sd[1], ef$er[1], labels="port 10", col="blue", pos=3)
text(ef$sd[2], ef$er[2], labels="port 9", col="blue", pos=3)
text(ef.ns$sd[10], ef.ns$er[10], labels="port 10", col="red", pos=1)
text(ef.ns$sd[9], ef.ns$er[9], labels="port 9", col="red", pos=1)



