read.csv(file = 'Advertising.csv', header = F)
head(a)
plot(a)
lm(a)
k= summary(lm(Sales~TV+Radio+Newspaper, data=a))
k
cor(a)


a <- c(1,1)

1:10

afun <- function(x,y)
{
  v <- x + y
  return(v)
}

afun(3,4)

v <- 0
for ( iiii in 1:100)
{
  v <- iiii + v
  return(v)
}
v
