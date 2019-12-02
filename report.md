# Player Performance Prediction Report

<!-- 
The problem you are addressing, particularly how you refined the provided idea.

The data that you used: how it was gathered, cleaned, etc.

Techniques you used to analyse the data.

Your results/findings/conclusions.

Some appropriate visualization of your data/results.

Limitations: problems you encountered, things you would do if you had more time, things you should have done in retrospect, etc. 
-->

## Problem Identification

We are interested in Stephen Curry's performance

## Data Collection Process

A majority of our data was collected from [basketball-reference.com](https://www.basketball-reference.com/), [pbpstats.com](http://www.pbpstats.com/), and [stats.nba.com](https://stats.nba.com/).

### Webscrape

- 

### Team Defensive Data for the Past Decade

- 

## Techniques

- aggregated 10 years of data for defensive rating among all teams
- all features we have are dependent (sicne they all relate or have an influence on the success rate of the shot)
  - used stadardscaler to make all comparable
  - used PCA to transform features to become independent (link article that mentions how the process of PCA turns anyting into independent cus... math)
  - given that the features are now independent of each other, satisfies the condition to use linear regression
  - use linear regression on our features to find
- want to predict number of shots made given historical data from 2009-2019

## Results

curry vs top def, mid, bott --> results found that curry is remarkably consistent in the number of shots he makes regardless of the defensive potency of the other team. THIS or that defensive rating is a bad metric that doesn't fully represent how a team is on defense.

though we found that curry seems to have a tendency to make a lot more shots, or in basketball lingo *explode*, in the first quarter against teams in the lower defensive ratings

## Limitations

initial question to answer: wanted to know curry's performance against other teams given the people guarding him

trouble along the way

- had trouble finding data for his matchup against opponents
- thought [nba_api](https://github.com/swar/nba_api) was promising since it had offered play-by-play stats
  - was under documented
  - connections would time out frequently regardless of size of request
  - found it to be very unreliable
  - slodged through api and managed to get matchup data
    - but data came aggregated and there were very few points
- found data on curry's shooting chart from [basketball-reference.com](https://www.basketball-reference.com/) with data points and information of each point embedded in html
  - realized that these data points were essentially play-by-play data of every shot he took
  - couldnt find a reliable source, so wrote `shot_webscrape.py` to scrape data

redefined our question to: wanted to know curry's performance against other teams given the people guarding him
