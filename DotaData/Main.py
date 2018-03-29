#encoding=utf-8

import dota2api
from DownLoadData.ObtainTableData import *
from DownLoadData.DataIntegrationFunction import *

api = dota2api.Initialise("86CAA11FA6D1484AA1777AFDA6E3EF0B")

#获取某场比赛详细数据以及玩家详细数据 get_match_detail,参数分别为matchid start,end

obtainMatchDataByMatchIdRange(3371385500,3371385600)# 前开后闭

#获取matchPlayer表中所有选手的近百场比赛的数据，并将指标相关字段汇总到playerHistoryMatchSummary表中
batchObtainPlayerHistory()
obtainHistoryMatchSummary()

print "程序完成，请执行sql开始整理数据"

#获取正在进行的联赛游戏数据  get_live_league_games
#get_live_league_games()






