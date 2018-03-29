# 通过File-import 将数据集进入R
#mode(X5v5_去重数据)通过mode查看进入的数据集的类型，是list类型 


allData<-数据整理1

winTeam<-subset(allData,TeamWin==1)
loseTeam<-subset(allData,TeamWin==0)

#开始输出团队层面的作战指标

pdf("~/我的文档/MBA养成记/3 论文写作/论文书写/thesisCode/胜负团队层面各指标的密度函数.pdf")

par(mfrow=c(4,3)) # 将屏幕分为3*3 的函数

plot(density(winTeam$Teamkills),col="blue",main = "Teamkills",cex.axis=0.7) #画出一个图形
lines(density(loseTeam$Teamkills),col="red",main = "",lty=2) #在已经画出的图形上追加新的图形
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$TeamLastHits),col="blue",main = "TeamLastHits",cex.axis=0.7)
lines(density(loseTeam$TeamLastHits),col="red",main = "",ylim=c(0,0.05),lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$TeamDenies),col="blue",main = "TeamDenies",cex.axis=0.7)
lines(density(loseTeam$TeamDenies),col="red",main = "",ylim=c(0,0.05),lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$TeamHeroDamage),col="blue",main = "TeamHeroDamage",cex.axis=0.7)
lines(density(loseTeam$TeamHeroDamage),col="red",main = "",ylim=c(0,0.05),lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$TeamTowerDamage),col="blue",main = "TeamTowerDamage",ylim=c(0,0.0003))
lines(density(loseTeam$TeamTowerDamage),col="red",main = "",ylim=c(0,1),lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$TeamDeath),col="blue",main = "TeamDeath",ylim=c(0,0.05),cex.axis=0.7)
lines(density(loseTeam$TeamDeath),col="red",main = "",lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$TeamAssist),col="blue",main = "TeamAssist",cex.axis=0.7)
lines(density(loseTeam$TeamAssist),col="red",main = "",lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$TeamHeroHealing),col="blue",main = "TeamHeroHealing",ylim=c(0,0.0005),cex.axis=0.7)
lines(density(loseTeam$TeamHeroHealing),col="red",main = "",ylim=c(0,1),lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");


plot(density(winTeam$TeamGPM),col="blue",main = "TeamGPM",cex.axis=0.7,ylim=c(0,0.003))
lines(density(loseTeam$TeamGPM),col="red",main = "",lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$TeamXPM),col="blue",main = "TeamXPM",cex.axis=0.7)
lines(density(loseTeam$TeamXPM),col="red",main = "",lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");



plot(density(winTeam$TeamGlodSpent),col="blue",main = "TeamGlodSpent",cex.axis=0.7)
lines(density(loseTeam$TeamGlodSpent),col="red",main = "",lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");


dev.off()


#开始输出队员历史水平的差异值  

pdf("~/我的文档/MBA养成记/3 论文写作/论文书写/thesisCode/胜负团队成员历史水平的密度函数.pdf")

par(mfrow=c(4,3)) # 将屏幕分为3*3 的函数

plot(density(winTeam$teamPlayerHistoryAvgKills),col="blue",main = "HistoryAvgKills",cex.axis=0.7) #画出一个图形
lines(density(loseTeam$teamPlayerHistoryAvgKills),col="red",main = "",lty=2) #在已经画出的图形上追加新的图形

plot(density(winTeam$teamPlayerHistoryAvgLastHits),col="blue",main = "HistoryAvgLastHits",cex.axis=0.7)
lines(density(loseTeam$teamPlayerHistoryAvgLastHits),col="red",main = "",ylim=c(0,0.05),lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$teamPlayerHistoryAvgDenies),col="blue",main = "HistoryAvgDenies",cex.axis=0.7)
lines(density(loseTeam$teamPlayerHistoryAvgDenies),col="red",main = "",ylim=c(0,0.05),lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$teamPlayerHistoryAvgHeroDamage),col="blue",main = "HistoryAvgHeroDamage",cex.axis=0.7)
lines(density(loseTeam$teamPlayerHistoryAvgHeroDamage),col="red",main = "",ylim=c(0,0.05),lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$teamPlayerHistoryAvgTowerDamage),col="blue",main = "HistoryAvgTowerDamage",ylim=c(0,2))
lines(density(loseTeam$teamPlayerHistoryAvgTowerDamage),col="red",main = "",ylim=c(0,2),lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$teamPlayerHistoryAvgDeaths),col="blue",main = "HistoryAvgDeaths",ylim=c(0,0.45),cex.axis=0.7)
lines(density(loseTeam$teamPlayerHistoryAvgDeaths),col="red",main = "",lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$teamPlayerHistoryAvgAssists),col="blue",main = "HistoryAvgAssists",cex.axis=0.7)
lines(density(loseTeam$teamPlayerHistoryAvgAssists),col="red",main = "",lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$teamPlayerHistoryAvgHeroHealing),col="blue",main = "HistoryAvgHeroHealing",ylim=c(0,0.004),cex.axis=0.7)
lines(density(loseTeam$teamPlayerHistoryAvgHeroHealing),col="red",main = "",ylim=c(0,1),lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");


plot(density(winTeam$teamPlayerHistoryAvgGPM),col="blue",main = "HistoryAvgGPM",cex.axis=0.7)
lines(density(loseTeam$teamPlayerHistoryAvgGPM),col="red",main = "",lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$teamPlayerHistoryAvgXPM),col="blue",main = "HistoryAvgXPM",cex.axis=0.7)
lines(density(loseTeam$teamPlayerHistoryAvgXPM),col="red",main = "",lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");



plot(density(winTeam$teamPlayerHistoryAvgGlodSpent),col="blue",main = "playerAvgGlodSpent",cex.axis=0.7)
lines(density(loseTeam$teamPlayerHistoryAvgGlodSpent),col="red",main = "",lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");

plot(density(winTeam$teamPlayerHistoryAvgWinRate),col="blue",main = "playerAvgWinRate",cex.axis=0.7)
lines(density(loseTeam$teamPlayerHistoryAvgWinRate),col="red",main = "",lty=2)
legend("topright",c("win","lose"),lty=c(1,2),col = c("blue","red"),cex = 0.7,bty="n");


dev.off()



