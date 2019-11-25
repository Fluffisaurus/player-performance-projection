import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import pandas as pd
from datetime import datetime, time
import re


def getShotMake(string):
    if(string == '●'):
        return True
    else:
        return False


# pre: takes param of a list of elements 
# post: returns pandas df of parsed data
def parseDataFromList(list):
    parsed = [];
    
    for elem in list:
        # format:
        # [DATE_OPPONENT, QUARTER_TIME_REMAINING, DESCRIPTION, GAME_SCORE]
        #
        # example:
        # ['Oct 17, 2017, GSW vs HOU', '1st Qtr, 8:09 remaining', 'Made 3-pointer from 25 ft', 'GSW now leads 15-7']
        tip = elem['tip'].split('<br>')

        # make string
        make_string = elem.get_text()
        made_shot = getShotMake(make_string)

        # date & opponent
        date_vs = tip[0].split(', ')
        date = datetime.strptime((date_vs[0]+ ", "+ date_vs[1]), '%b %d, %Y')

        match = re.search(r'(?<=((vs\s)|(at\s)))\w*', date_vs[2])
        if(match):
            vs = match.group(0)
        else:
            vs = None

        # home or away
        home_away_match = re.search(r'(vs)|(at)', date_vs[2])
        if(home_away_match):
            if(home_away_match.group(0) == 'vs'):
                at_home = True
            else:
                at_home = False
        else:
            at_home = None

        # game time - quarter and time remaining in quarter
        # print(tip[1])
        game_time = tip[1].split(', ')
        q = re.search('\d', game_time[0])
        if(q):
            quarter = int(q.group(0))
        else:
            quarter = None

        t = re.search('\d{,2}:\d{2}', game_time[1])
        if(t):
            time_string = t.group(0)
            time_string = time_string.split(':')
            time_left = time(minute = int(time_string[0]), second = int(time_string[1])).strftime('%M:%S')
        else:
            time_string = None
    
        
        # shot location
        xy_match = re.findall('(?<=:)(?:-?)\d*', elem['style']) # (?:-?) optionally take a negative sign 
        if(xy_match):
            y_pos = int(xy_match[0])
            x_pos = int(xy_match[1])
        else:
            y_pos = None
            x_pos = None



        row_info = {
            'date': date,
            'home': at_home,
            'vs': vs,
            'shot_made': made_shot,
            'x': x_pos,
            'y': y_pos,
            'quarter': quarter,
            'time_left': time_left,
            'shot_description': tip[2],
            'game_score': tip[3],
        }
        
        parsed.append(row_info)
    
    df = pd.DataFrame(parsed)
    return df


def main(urlToParse, outFileName):
    driver = webdriver.Chrome(executable_path='/mnt/c/Windows/chromedriver.exe')
    driver.get(urlToParse)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    shot_area = soup.find(class_='shot-area')
    shots = shot_area.find_all('div') # list of all divs

    data = parseDataFromList(shots)
    data.to_csv(outFileName, index=False)

    # end chromedriver process
    driver.quit()


if __name__=='__main__':
    urlToParse = sys.argv[1]
    outFileName = sys.argv[2]
    main(urlToParse, outFileName)