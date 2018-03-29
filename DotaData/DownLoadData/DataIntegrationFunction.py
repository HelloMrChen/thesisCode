# encoding=utf-8
#本表用来实现最终数据表整合的各种逻辑函数
import MySQLdb as mdb
import numpy as np
from DownLoadData.ObtainTableData import *

def obtainMatchDataByMatchIdRange(start,end):
    for i in range(start,end):
        try:
            obtainMatchDetailData(i)
            print "第 "+str(i)+ "场比赛数据获取成功,并将比赛概况插入到了matchSummary，选手表现插入到了matchPlayer表中"
        except:
            print "第 "+str(i)+" 场比赛数据获取失败，可能是比赛数据不公开，或者网络连接有问题"


#通过随机获取的比赛中的参赛玩家账号，自动获取其历史100场比赛
def batchObtainPlayerHistory():
    #链接数据库
    con = mdb.connect("localhost", "root", "123", "dataSource")
    with con:
        cur = con.cursor(mdb.cursors.DictCursor)
        # 执行查询
        cur.execute("select account_id from matchPlayers;")
        # 将查询结果存入变量rows
        rows = cur.fetchall()
        # 将rows转化为数组,转化后是一个字典类型的数组
        rows = np.array(rows)
    for num in range(len(rows)):
        if(rows[num]['account_id']!='4294967295'):# 这个玩家有问题，属于异常账号
            obtainMatchHistory(rows[num]['account_id'])
    pass

# batchObtainPlayerHistory()

#根据playerhistory获取玩家近百场比赛详情，调用存到obtainplayerHistoryMatchSummary函数将数据存到playerHistoryMatchSummary表中
def obtainHistoryMatchSummary():
    #创建数据库链接
    con=MySQLdb.connect('localhost','root','123','dataSource')

    #使用cursor 方法获取操作游标
    cur=con.cursor()

    sql='SELECT search_account_ID, match_id  FROM matchHistory'#从matchHistory中获取玩家账号和游戏id

    cur.execute(sql)
    rows=cur.fetchall()
    for num in range(len(rows)):
        # print rows[num][0],rows[num][1]
        obtainplayerHistoryMatchSummary(rows[num][0],rows[num][1])

    con.close
    pass

obtainHistoryMatchSummary()



