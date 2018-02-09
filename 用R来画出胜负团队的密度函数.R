# 通过File-import 将数据集进入R
#mode(X5v5_去重数据)通过mode查看进入的数据集的类型，是list类型 

allData<-X5v5_去重数据

winTeam<-subset(allData,TeamWin==1)
loseTeam<-subset(allData,TeamWin==0)

pdf("~/我的文档/MBA养成记/3 论文写作/论文书写/thesisCode/胜负团队各变量的密度函数.pdf")


plot(density(winTeam$Paticipation),col="blue",main = "Paticipation",cex.main=0.7,cex.lab=0.5,cex.axis=0.7)
lines(density(loseTeam$Paticipation),col="red",main = "")

plot(density(winTeam$Teamkills),col="blue",main = "Teamkills",cex.main=0.7,cex.lab=0.5,cex.axis=0.7)
lines(density(loseTeam$Teamkills),col="red",main = "")

plot(density(winTeam$TeamAssist),col="blue",main = "TeamAssist",cex.main=0.7,cex.lab=0.5,cex.axis=0.7)
lines(density(loseTeam$TeamAssist),col="red",main = "")
par(cex.main=0.7,cex.lab=0.5,cex.axis=0.7)



plot(density(winTeam$TeamHeroHealing),col="blue",main = "TeamHeroHealing",ylim=c(0,0.0005))
lines(density(loseTeam$TeamHeroHealing),col="red",main = "",ylim=c(0,1))
par(cex.main=0.7,cex.lab=0.5,cex.axis=0.7)


plot(density(winTeam$TeamDeath),col="blue",main = "TeamDeath",ylim=c(0,0.05))
lines(density(loseTeam$TeamDeath),col="red",main = "")
par(cex.main=0.7,cex.lab=0.5,cex.axis=0.7)


plot(density(winTeam$TeamHeroDamage),col="blue",main = "TeamHeroDamage")
lines(density(loseTeam$TeamHeroDamage),col="red",main = "",ylim=c(0,1))
par(cex.main=0.7,cex.lab=0.5,cex.axis=0.7)

plot(density(winTeam$TeamTowerDamage),col="blue",main = "TeamTowerDamage",ylim=c(0,0.0003))
lines(density(loseTeam$TeamTowerDamage),col="red",main = "",ylim=c(0,1))
par(cex.main=0.7,cex.lab=0.5,cex.axis=0.7)

plot(density(winTeam$TeamGlodSpent),col="blue",main = "TeamGlodSpent")
lines(density(loseTeam$TeamGlodSpent),col="red",main = "")
par(cex.main=0.7,cex.lab=0.5,cex.axis=0.7)


plot(density(winTeam$TeamGold),col="blue",main = "TeamGold",ylim=c(0,0.0002))
lines(density(loseTeam$TeamGold),col="red",main = "")
par(cex.main=0.7,cex.lab=0.5,cex.axis=0.7)



dev.off()






