rm(list = ls())
setwd('E:/FingerTwisters/data')
library(ggplot2)

S1 = read.table('trials_homewood.txt', header = T)
S2 = read.table('trials_keyboard.txt', header = T)

S1$Keyboard = 'HW'
S2$Keyboard = 'FP'
dat = rbind(S1,S2)

# order IKI values
# plot them in increasing order

# Remove RT / Compute IKI
S1$IKI = c(0,diff(S1$Time))*1000
S2$IKI = c(0,diff(S2$Time))*1000


S1 = subset(S1, Keypress != 1)

IKI = S1$IKI
IKIs = sort(IKI)
data = data.frame(IKI = na.exclude(IKI), IKIs = IKIs)
ggplot(data, aes(x = 1:nrow(data), y = IKIs)) + geom_point(alpha = 0.5) + xlab('') + ylab('IKI Difference (ms)') + theme_bw() 

data2 = subset(data, IKIs<301 & IKIs>99)
ggplot(data2, aes(x = 1:nrow(data2), y = IKIs)) + geom_point(alpha = 0.5, size = 0.7) + 
  xlab('') + ylab('IKI Difference (ms)') + theme_bw() + scale_y_continuous(breaks = seq(100,300,20))

pdf('Standard_keyboard.pdf')
dev.off()


S2 = subset(S2, Keypress != 1)

IKI = S2$IKI
IKIs = sort(IKI)
data = data.frame(IKI = na.exclude(IKI), IKIs = IKIs)
ggplot(data, aes(x = 1:nrow(data), y = IKIs)) + geom_point(alpha = 0.5) + xlab('') + ylab('IKI Difference (ms)') + theme_bw() 

data2 = subset(data, IKIs<201 & IKIs>49)
ggplot(data2, aes(x = 1:nrow(data2), y = IKIs)) + geom_point(alpha = 0.5, size = 0.7) + 
  xlab('') + ylab('IKI Difference (ms)') + theme_bw() + scale_y_continuous(breaks = seq(60,200,20))


pdf('Empirisoft_keyboard.pdf')
dev.off()

