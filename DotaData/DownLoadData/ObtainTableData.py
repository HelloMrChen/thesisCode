# encoding=utf-8
# 本表只用来存放获取表数据的各种函数，不实现太多的业务逻辑

import MySQLdb
import dota2api

api = dota2api.Initialise("86CAA11FA6D1484AA1777AFDA6E3EF0B")


# 输入比赛Match_ID 输出到数据库比赛概况和比赛队员详细信息
def obtainMatchDetailData(match_id):
    macth_detail_dict = api.get_match_details(match_id)  # 此处应该设置为函数参数
    matchSummary_match_id = macth_detail_dict.get('match_id', None)
    matchSummary_radiant_win = macth_detail_dict.get('radiant_win', None)
    matchSummary_duration = macth_detail_dict.get('duration', None)
    matchSummary_start_time = macth_detail_dict.get('start_time', None)
    matchSummary_match_seq_num = macth_detail_dict.get('match_seq_num', None)
    matchSummary_tower_status_radiant = macth_detail_dict.get('tower_status_radiant', None)
    matchSummary_tower_status_dire = macth_detail_dict.get('tower_status_dire', None)
    matchSummary_barracks_status_radiant = macth_detail_dict.get('barracks_status_radiant', None)
    matchSummary_barracks_status_dire = macth_detail_dict.get('barracks_status_dire', None)
    matchSummary_cluster = macth_detail_dict.get('cluster', None)
    matchSummary_cluster_name = macth_detail_dict.get('cluster_name', None)
    matchSummary_first_blood_time = macth_detail_dict.get('first_blood_time', None)
    matchSummary_lobby_type = macth_detail_dict.get('lobby_type', None)
    matchSummary_lobby_name = macth_detail_dict.get('lobby_name', None)
    matchSummary_human_players = macth_detail_dict.get('human_players', None)
    matchSummary_leagueid = macth_detail_dict.get('leagueid', None)
    matchSummary_positive_votes = macth_detail_dict.get('positive_votes', None)
    matchSummary_negative_votes = macth_detail_dict.get('negative_votes', None)
    matchSummary_game_mode = macth_detail_dict.get('game_mode', None)
    matchSummary_game_mode_name = macth_detail_dict.get('game_mode_name', None)
    matchSummary_radiant_captain = macth_detail_dict.get('radiant_captain', None)
    matchSummary_dire_captain = macth_detail_dict.get('dire_captain', None)

    # 链接数据库
    db = MySQLdb.connect("localhost", "root", "123", "dataSource")

    # 使用cursor 方法获取操作游标
    cursor = db.cursor()

    # --------------------------------------------------定义插入数据库的sql和value，插入matchSummary(比赛概况表)
    matchSummarySql = "insert into matchSummary(match_ID,radiant_win, duration, start_time, match_seq_num,tower_status_radiant,tower_status_dire,barracks_status_radiant,barracks_status_dire,cluster,cluster_name,first_blood_time,lobby_type,lobby_name,human_players,leagueid,positive_votes,negative_votes,game_mode,game_mode_name,radiant_captain,dire_captain) VALUES (%(match_ID)s,%(radiant_win)s,%(duration)s,%(start_time)s,%(match_seq_num)s,%(tower_status_radiant)s,%(tower_status_dire)s,%(barracks_status_radiant)s,%(barracks_status_dire)s,%(cluster)s,%(cluster_name)s,%(first_blood_time)s,%(lobby_type)s,%(lobby_name)s,%(human_players)s,%(leagueid)s,%(positive_votes)s,%(negative_votes)s,%(game_mode)s,%(game_mode_name)s,%(radiant_captain)s,%(dire_captain)s) "

    matchSummaryValue = {"match_ID": matchSummary_match_id, "radiant_win": matchSummary_radiant_win,
                         "duration": matchSummary_duration, "start_time": matchSummary_start_time,
                         "match_seq_num": matchSummary_match_seq_num,
                         "tower_status_radiant": matchSummary_tower_status_radiant,
                         "tower_status_dire": matchSummary_tower_status_dire,
                         "barracks_status_radiant": matchSummary_barracks_status_radiant,
                         "barracks_status_dire": matchSummary_barracks_status_dire, "cluster": matchSummary_cluster,
                         "cluster_name": matchSummary_cluster_name, "first_blood_time": matchSummary_first_blood_time,
                         "lobby_type": matchSummary_lobby_type, "lobby_name": matchSummary_lobby_name,
                         "human_players": matchSummary_human_players, "leagueid": matchSummary_leagueid,
                         "positive_votes": matchSummary_positive_votes, "negative_votes": matchSummary_negative_votes,
                         "game_mode": matchSummary_game_mode, "game_mode_name": matchSummary_game_mode_name,
                         "radiant_captain": matchSummary_radiant_captain, "dire_captain": matchSummary_dire_captain}

    try:
        # 执行sql语句
        cursor.execute(matchSummarySql, matchSummaryValue)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        print("插入比赛概况的sql执行失败了！")
        db.rollback()

    # -------------------------------------------------------------获取玩家数据、忽略技能和使用的武器
    players = macth_detail_dict['players']

    # d = {k: players.count(k) for k in set(players)}

    for p in players:
        matchPlayers_match_id = macth_detail_dict['match_id']
        matchPlayers_account_id = p['account_id']
        matchPlayers_player_slot = p['player_slot']
        matchPlayers_hero_id = p['hero_id']
        matchPlayers_hero_name = p['hero_name']
        matchPlayers_kills = p['kills']
        matchPlayers_deaths = p['deaths']
        matchPlayers_assists = p['assists']
        matchPlayers_leaver_status = p['leaver_status']
        matchPlayers_gold = p['gold']
        matchPlayers_last_hits = p['last_hits']
        matchPlayers_denies = p['denies']
        matchPlayers_gold_per_min = p['gold_per_min']
        matchPlayers_xp_per_min = p['xp_per_min']
        matchPlayers_gold_spent = p['gold_spent']
        matchPlayers_hero_damage = p['hero_damage']
        matchPlayers_tower_damage = p['tower_damage']
        matchPlayers_hero_healing = p['hero_healing']
        matchPlayers_level = p['level']
        matchPlayersSql = "insert into matchPlayers(match_ID,account_id,player_slot,hero_id, hero_name,kills,deaths,assists,leaver_status,gold,last_hits,denies,gold_per_min,xp_per_min,gold_spent,hero_damage,tower_damage,hero_healing,level) VALUES (%(match_ID)s,%(account_id)s,%(player_slot)s,%(hero_id)s,%(hero_name)s,%(kills)s,%(deaths)s,%(assists)s,%(leaver_status)s,%(gold)s,%(last_hits)s,%(denies)s,%(gold_per_min)s,%(xp_per_min)s,%(gold_spent)s,%(hero_damage)s,%(tower_damage)s,%(hero_healing)s,%(level)s) "
        matchPlayersValue = {"match_ID": matchPlayers_match_id, "account_id": matchPlayers_account_id,
                             "player_slot": matchPlayers_player_slot, "hero_id": matchPlayers_hero_id,
                             "hero_name": matchPlayers_hero_name, "kills": matchPlayers_kills,
                             "deaths": matchPlayers_deaths, "assists": matchPlayers_assists,
                             "leaver_status": matchPlayers_leaver_status,
                             "gold": matchPlayers_gold, "last_hits": matchPlayers_last_hits,
                             "denies": matchPlayers_denies, "gold_per_min": matchPlayers_gold_per_min,
                             "xp_per_min": matchPlayers_xp_per_min,
                             "gold_spent": matchPlayers_gold_spent, "hero_damage": matchPlayers_hero_damage,
                             "tower_damage": matchPlayers_tower_damage, "hero_healing": matchPlayers_hero_healing,
                             "level": matchPlayers_level}
        try:
            # 执行sql语句
            cursor.execute(matchPlayersSql, matchPlayersValue)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            print "插入比赛玩家信息的sql执行失败了！"
            db.rollback()

    # 关闭数据库连接
    db.close()
    pass


# 按照玩家的账户ID获取该玩家近100场的历史数据
def obtainMatchHistory(playerID):
    # 链接数据库
    db = MySQLdb.connect("localhost", "root", "123", "dataSource")

    # 使用cursor 方法获取操作游标
    cursor = db.cursor()

    # 获取history里的详细数据，并且插入数据库
    try:
        playerMatchHistory_dict = api.get_match_history(playerID)
        playAccountID = playerID
        matchHistory_num_results = playerMatchHistory_dict.get('num_results', None)
        matchSummary_total_results = playerMatchHistory_dict.get('total_results', None)
        matchSummary_results_remaining = playerMatchHistory_dict.get('results_remaining', None)
        matchHistory_matches = playerMatchHistory_dict['matches']
        for m in matchHistory_matches:
            match_id = m['match_id']
            match_seq_num = m['match_seq_num']
            start_time = m['start_time']
            lobby_type = m['lobby_type']
            matchHistory_players = m['players']

            '''
            print matchHistory_players
            for p in matchHistory_players:
                account_id=p['account_id']
                player_slot=p['player_slot']
                hero_id=p['hero_id']
                print "hello"
             '''

            matchHistorySql = "insert into matchHistory(search_account_ID,num_results,total_results,results_remaining,match_id,match_seq_num,start_time,lobby_type) VALUES (%(playAccountID)s,%(matchHistory_num_results)s,%(matchSummary_total_results)s,%(matchSummary_results_remaining)s,%(match_id)s,%(match_seq_num)s,%(start_time)s,%(lobby_type)s) "
            matchHistoryValue = {"playAccountID": playAccountID, "matchHistory_num_results": matchHistory_num_results,
                                 "matchSummary_total_results": matchSummary_total_results,
                                 "matchSummary_results_remaining": matchSummary_results_remaining, "match_id": match_id,
                                 "match_seq_num": match_seq_num, "start_time": start_time, "lobby_type": lobby_type}
            try:
                # 执行sql语句
                cursor.execute(matchHistorySql, matchHistoryValue)
                # 提交到数据库执行
                db.commit()
                print "已插入了玩家",playerID,"的比赛号为",match_id,"的","历史比赛数据到数据库matchHistory表"
            except:
                # Rollback in case there is any error
                print "在插入"+playerID+"比赛数据到matchHistory表的时候sql执行失败！"
                db.rollback()

    except:
        print "账号为",playerID,"的玩家可能不允许公开历史比赛数据，无法获取其近百场比赛ID"

    # 关闭数据库连接
    db.close()
    pass


# 获取正在直播的联赛
def obtainliveLeagueGamesData():
    # 链接数据库
    db = MySQLdb.connect("localhost", "root", "123", "dataSource")

    # 使用cursor 方法获取操作游标
    cursor = db.cursor()

    # 获取history里的详细数据，并且插入数据库
    live_league_game_dict = api.get_live_league_games()
    # print live_league_game_dict
    games = live_league_game_dict.get('games', None)
    for i in games:
        league_id = i['league_id']
        match_id = i['match_id']
        stream_delay_s = i['stream_delay_s']
        league_tier = i['league_tier']
        league_series_id = i['league_series_id']
        series_id = i['series_id']
        series_type = i['series_type']
        stage_name = i['stage_name']
        game_number = i['game_number']
        radiant_series_wins = i['radiant_series_wins']
        dire_series_wins = i['dire_series_wins']
        spectators = i['spectators']
        liveLeagueGamesSql = "insert into liveLeagueGames(league_id,match_id,league_tier,league_series_id,series_id,series_type,stage_name,game_number,radiant_series_wins,dire_series_wins,spectators,stream_delay_s) VALUES (%(league_id)s,%(match_id)s,%(league_tier)s,%(league_series_id)s,%(series_id)s,%(series_type)s,%(stage_name)s,%(game_number)s,%(radiant_series_wins)s,%(dire_series_wins)s,%(spectators)s,%(stream_delay_s)s) "
        liveLeagueGamesValue = {"league_id": league_id, "match_id": match_id, "league_tier": league_tier,
                                "league_series_id": league_series_id, "series_id": series_id,
                                "series_type": series_type, "stage_name": stage_name, "game_number": game_number,
                                "radiant_series_wins": radiant_series_wins, "dire_series_wins": dire_series_wins,
                                "spectators": spectators, "stream_delay_s": stream_delay_s}
        cursor.execute(liveLeagueGamesSql, liveLeagueGamesValue)
        db.commit()
    # 关闭数据库连接
    db.close()
    pass

def obtainplayerHistoryMatchSummary(playerID,mathchID):

    #数据库链接相关
    con=MySQLdb.connect('localhost','root','123','dataSource')
    cur=con.cursor()

    try:
        historyMatchData = api.get_match_details(mathchID)
        matchID=historyMatchData.get('match_id', None)
        playerID=playerID
        isRadiantWin=historyMatchData.get('radiant_win', None)
        players = historyMatchData['players']
        for p in players:
            if int(playerID)==p['account_id']: #p['account_id']为整型，playerID为str型，两者比配不对的话，很容易发生错误
                playerSlot=p['player_slot']
                playerHeroName = p['hero_name']
                playerKills = p['kills']
                playerDeaths = p['deaths']
                playerAssists = p['assists']
                playerLeaverStatus = p['leaver_status']
                playerGlod = p['gold']
                playerLastHits = p['last_hits']
                playerDenies = p['denies']
                playerGPM = p['gold_per_min']
                playerXPM = p['xp_per_min']
                playerGlodSpent = p['gold_spent']
                playerHeroDamage = p['hero_damage']
                playerTowerDamage = p['tower_damage']
                playerHeroHealing = p['hero_healing']
                playerTeam=1 if playerSlot>100 else 0 #大于100为Dire，小于100为夜魇，我们这里把Dire标注为1，radaint标注为0
                playerWin=0 if isRadiantWin==playerTeam else 1 #如果选手正好在Radaint，并且Radaint赢了，那么代表选手赢了
                sql='insert into ' \
                    'playerHistoryMatchSummary(matchID,playerID,playerSlot,playerHeroName,playerKills,playerDeaths,playerAssists,' \
                    'playerLeaveStatus,playerGlod,playerLastHits,playerDenies,playerGPM,playerXPM,' \
                    'playerGlodSpent,playerHeroDamage,playerTowerDamage,playerHeroHealing,playerWin) ' \
                    'VALUES (%(matchID)s,%(playerID)s,%(playerSlot)s,%(playerHeroName)s,%(playerKills)s,%(playerDeaths)s,%(playerAssists)s,' \
                    '%(playerLeaveStatus)s,%(playerGlod)s,%(playerLastHits)s,%(playerDenies)s,%(playerGPM)s,%(playerXPM)s,' \
                    '%(playerGlodSpent)s,%(playerHeroDamage)s,%(playerTowerDamage)s,%(playerHeroHealing)s,%(playerWin)s)'
                value={"matchID":mathchID,"playerID":playerID,"playerSlot":playerSlot,"playerHeroName":playerHeroName,"playerKills":playerKills,"playerDeaths":playerDeaths,
                       "playerAssists":playerAssists,"playerLeaveStatus":playerLeaverStatus,"playerGlod":playerGlod,"playerLastHits":playerLastHits,"playerDenies":playerDenies,
                       "playerGPM":playerGPM,"playerXPM":playerXPM,"playerGlodSpent":playerGlodSpent,"playerHeroDamage":playerHeroDamage,
                       "playerTowerDamage":playerTowerDamage,"playerHeroHealing":playerHeroHealing,"playerWin":playerWin}
                cur.execute(sql,value)
                con.commit()
                print "已经成功插入",playerID,"的比赛号为",mathchID,"的比赛数据到表playerHistoryMatchSummary"
                break #找到该队员算好数据即退出，没有必要再找其他队员的数据，提高效率
    except:
        print "插入",playerID,"的比赛号为",mathchID,"的比赛数据到表playerHistoryMatchSummary时发生错误，有可能是他比赛数据不公开"
    con.close
    pass

