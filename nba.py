#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:02:31 2019

@author: ansonchristo
"""

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import PlayerVsPlayer, TeamVsPlayer, PlayByPlay, leaguegamefinder
import pandas as pd 
import numpy as np
import json

#Players Info
steph_id = players.find_players_by_full_name('Steph')[1]
nba_players_info = pd.concat([pd.DataFrame.from_dict(players.get_players()[i], orient='index').transpose() for i in range(30)],ignore_index=True)

#NBA Teams 
nba_teams_info = pd.concat([pd.DataFrame.from_dict(teams.get_teams()[i], orient='index').transpose() for i in range(30)],ignore_index=True)


#PlayByPlay

#params = PlayByPlay(game_id=start_period=1,end_period=4)
 

leaguegamefinder()





