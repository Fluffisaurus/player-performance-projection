#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 00:10:53 2019

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


def season_team(season,player_id,nba_team_info):
    new_df = pd.DataFrame(columns=nba_team_info['full_name'],index = [season])
    for (i,j) in zip(nba_team_info['full_name'],nba_team_info['id']):
        dict_team = TeamVsPlayer(team_id=j,season=season,vs_player_id=player_id, headers=headers).get_normalized_dict()
        dict_to_df = pd.DataFrame.from_dict(dict_team, orient = 'index').transpose()
        filtered_col = filter_col_team(dict_to_df)
        new_df.loc[season][i] = filtered_col
    return new_df




def main():
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
    
    season_2018_19 = season_team("2018-19",steph_id,nba_teams_info)
    season_2017_18 = season_team("2017-18",steph_id,nba_teams_info)
    season_2016_17 = season_team("2016-17",steph_id,nba_teams_info)
    season_2015_16 = season_team("2015-16",steph_id,nba_teams_info)
    season_2014_15 = season_team("2014-15",steph_id,nba_teams_info)
    season_2013_14 = season_team("2013-14",steph_id,nba_teams_info)
    season_2012_13 = season_team("2012-13",steph_id,nba_teams_info)
    season_2011_12 = season_team("2011-12",steph_id,nba_teams_info)
    season_2010_11 = season_team("2010-11",steph_id,nba_teams_info)
    season_2009_10 = season_team("2009-10",steph_id,nba_teams_info)


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