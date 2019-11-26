#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:02:31 2019

@author: ansonchristo
"""

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import PlayerVsPlayer, TeamVsPlayer, PlayByPlay, leaguegamefinder,teamvsplayer
import pandas as pd 
import numpy as np
import json
headers = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}
#USE HEADER TO ACCESS API

#Players Info
steph_id = players.find_players_by_full_name('Steph')[1]
nba_players_info = pd.concat([pd.DataFrame.from_dict(players.get_players()[i], orient='index').transpose() for i in range(len(players.get_players()))],ignore_index=True)

#NBA Teams 
nba_teams_info = pd.concat([pd.DataFrame.from_dict(teams.get_teams()[i], orient='index').transpose() for i in range(30)],ignore_index=True)

#PlayByPlay

#params = PlayByPlay(game_id=start_period=1,end_period=4)
 


#Steph Curry DataFrame Stats Against all 30 Teams

StephVsTeam_df = pd.DataFrame(columns = nba_teams_info['full_name'], index=['2018-2019','2017-2018','2016-2017','2015-2014','2014-2013','2013-2012','2012-2011','2011-2012','2010-2011','2009-2010'])


#Teams in Array 
teams = nba_teams_info['full_name'].values

#Seasons in Array
seasons = ['2018-2019','2017-2018','2016-2017','2015-2014','2014-2013','2013-2012','2012-2011','2011-2012','2010-2011','2009-2010']


#Testing Code

#trial = PlayerVsPlayer(vs_player_id=1629027, player_id=steph_id['id'])

trial = TeamVsPlayer(vs_player_id=steph_id['id'],team_id='1610612737',season='2016-17',headers=headers).get_normalized_dict()

df = pd.DataFrame.from_dict(trial, orient = 'index').transpose()

