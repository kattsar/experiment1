rm(list = ls())
setwd("C:\\Users\\Κατερίνα\\Nextcloud\\Keyboard comparison")
library(ggplot2)

S1 = read.table('trials_normal.txt', header = T)
S2 = read.table('trials_upgrade.txt', header = T)

S1$Keyboard = 'HW'
S2$Keyboard = 'FP'
dat = rbind(S1,S2)

# order IKI values
# plot them in increasing order

# Remove RT / Compute IKI
S1$IKI = c(0,diff(S1$RT))*1000
S2$IKI = c(0,diff(S2$RT))*1000


S1 = subset(S1, Keypress != "key1")

IKI = S1$IKI
IKIs = sort(IKI)
data = data.frame(IKI = na.exclude(IKI), IKIs = IKIs)
ggplot(data, aes(x = 1:nrow(data), y = IKIs)) + geom_point(alpha = 0.5) + xlab('') + ylab('IKI Difference (ms)') + theme_bw() 

data2 = subset(data, IKIs<704 & IKIs>15)
ggplot(data2, aes(x = 1:nrow(data2), y = IKIs)) + geom_point(alpha = 0.5, size = 0.7) + 
  xlab('') + ylab('IKI Difference (ms)') + theme_bw() + scale_y_continuous(breaks = seq(20,800,20))

pdf("C:\\Users\\Κατερίνα\\Nextcloud\\Keyboard comparison\\Standard_keyboard_KT.pdf")
dev.off()


S2 = subset(S2, Keypress != "key1")

IKI = S2$IKI
IKIs = sort(IKI)
data = data.frame(IKI = na.exclude(IKI), IKIs = IKIs)
ggplot(data, aes(x = 1:nrow(data), y = IKIs)) + geom_point(alpha = 0.5) + xlab('') + ylab('IKI Difference (ms)') + theme_bw() 

data2 = subset(data, IKIs<657 & IKIs>36)
ggplot(data2, aes(x = 1:nrow(data2), y = IKIs)) + geom_point(alpha = 0.5, size = 0.7) + 
  xlab('') + ylab('IKI Difference (ms)') + theme_bw() + scale_y_continuous(breaks = seq(40,700,20))


pdf('Empirisoft_keyboard.pdf')
dev.off()

