#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:02:31 2019

@author: ansonchristo
"""
from nba_api.stats.static import players,teams
from nba_api.stats.endpoints import PlayerVsPlayer, TeamVsPlayer, PlayByPlay, leaguegamefinder,teamvsplayer
import pandas as pd 
import numpy as np
import json

#USE HEADER TO ACCESS API!!!!`

def filter_col_team(df):
    return df.drop(['Overall','vsPlayerOverall','ShotDistanceOverall','ShotDistanceOffCourt','ShotAreaOverall','ShotAreaOffCourt'],axis=1)

def insert_PlayerVsTeam(StephVsTeam_df,player_id,team_info):
    seasons = ['2018-19','2017-18','2016-17','2015-16','2014-15','2013-14','2012-13','2011-12','2010-11','2009-10']
    for i in seasons:
        team_id = team_info['id'][0]
        team_name = team_info['full_name'][0]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][1]
        team_name = team_info['full_name'][1]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][2]
        team_name = team_info['full_name'][2]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][3]
        team_name = team_info['full_name'][3]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][4]
        team_name = team_info['full_name'][4]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][5]
        team_name = team_info['full_name'][5]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][6]
        team_name = team_info['full_name'][6]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][7]
        team_name = team_info['full_name'][7]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][8]
        team_name = team_info['full_name'][8]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][9]
        team_name = team_info['full_name'][9]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][10]
        team_name = team_info['full_name'][10]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][11]
        team_name = team_info['full_name'][11]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][12]
        team_name = team_info['full_name'][12]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][13]
        team_name = team_info['full_name'][13]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][14]
        team_name = team_info['full_name'][14]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][15]
        team_name = team_info['full_name'][15]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][16]
        team_name = team_info['full_name'][16]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][17]
        team_name = team_info['full_name'][17]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][18]
        team_name = team_info['full_name'][18]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][19]
        team_name = team_info['full_name'][19]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][20]
        team_name = team_info['full_name'][20]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][21]
        team_name = team_info['full_name'][21]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][22]
        team_name = team_info['full_name'][22]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][23]
        team_name = team_info['full_name'][23]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][24]
        team_name = team_info['full_name'][24]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][25]
        team_name = team_info['full_name'][25]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][26]
        team_name = team_info['full_name'][26]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][27]
        team_name = team_info['full_name'][27]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][28]
        team_name = team_info['full_name'][28]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    for i in seasons:
        team_id = team_info['id'][29]
        team_name = team_info['full_name'][29]
        dict_team = TeamVsPlayer(vs_player_id=player_id,team_id=team_id,season=i,headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        StephVsTeam_df.loc[i][team_name] = filtered_col
    return StephVsTeam_df
    
        

def main():
#    headers = {
#    'Host': 'stats.nba.com',
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
#    'Accept': 'application/json, text/plain, */*',
#    'Accept-Language': 'en-US,en;q=0.5',
#    'Referer': 'https://stats.nba.com/',
#    'Accept-Encoding': 'gzip, deflate, br',
#    'Connection': 'keep-alive',
#    }
    #All NBA Players Information in DataFrame
    nba_players_info = pd.concat([pd.DataFrame.from_dict(players.get_players()[i], orient='index').transpose() for i in range(len(players.get_players()))],ignore_index=True)
    
    #All NBA Teams Information in DataFrame
    nba_teams_info = pd.concat([pd.DataFrame.from_dict(teams.get_teams()[i], orient='index').transpose() for i in range(30)],ignore_index=True)
    
    #Players that are active right now
    players_active = nba_players_info[nba_players_info['is_active'] == True].reset_index(drop=True)
    
    #Players Active in Array
    players_active_array = players_active['full_name'].values
   
    #Teams in Array 
    teams_array = nba_teams_info['full_name'].values
    
    #Seasons in Array
    seasons = ['2018-19','2017-18','2016-17','2015-16','2014-15','2013-14','2012-13','2011-12','2010-11','2009-10']
    
    #Stephs ID
    steph_id = players.find_players_by_full_name('Steph')[1]

    #Steph's Dataframe Against Teams
    StephVsTeam_df = pd.DataFrame(columns = nba_teams_info['full_name'], index=['2018-19','2017-18','2016-17','2015-16','2014-15','2013-14','2012-13','2011-12','2010-11','2009-10'])
    StephStatsVsTeams = insert_PlayerVsTeam(StephVsTeam_df,steph_id,nba_teams_info)
    
    
    #Steph's Dataframe Against Players
    #StephVsPlayers_df = pd.DataFrame(columns = players_active['full_name'], index=['2018-19','2017-18','2016-17','2015-16','2014-15','2013-14','2012-13','2011-12','2010-11','2009-10'])
    
    
    
    

if __name__=='__main__':
    headers = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    }
    main()