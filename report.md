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

Stephen Curry from the Golden State Warriors had some spectacular seasons and managed to win his first MVP award and the first player in NBA history to be elected MVP unanimously. We are interested in Stephen Curry's performance against top, middle, and bottom defensive rank teams based on each teams defensive ratings from 2009-2019. We are curious to observe how many shots were made against certain tiers.  

## Data Collection Process

A majority of our data was collected from [basketball-reference.com](https://www.basketball-reference.com/), [pbpstats.com](http://www.pbpstats.com/), and [stats.nba.com](https://stats.nba.com/).

### Webscrape

- Scraped shotchart data and parsed into dataframe with columns since Curry's rookie season 2009-10 to 2018-19
- script generates dataframe with 10 columns
  - [insert example of dataframe row 1 here]
- in total over the 10 years, yielded around 14k rows of data

### Team Defensive Data for the Past Decade

- Gathered historical data for team's defensive ratings from 2009-2019 through [stats.nba.com](https://stats.nba.com/).
- three teams went through rebrandings since 2009
  - *Charlotte Bobcats* --> Charlotte Hornets
  - *New Jersey Nets* --> Brooklyn Nets
  - *New Orleans Hornets* --> New Orleans Pelicans
  - aggregated and changed to match present team.
- Added acronyms for each team in order to merge with webscrape dataset
- Averaged defensive rating across the decade / datasets and ranked them based on lowest to highest.

## Techniques
Through our play by play data, we were fully aware that we needed to use StandardScaler() in order to make it comparable, this is because we have features that scales differently such as our *shot_value*, *shot_distance*, and *cum_fg_percent*. Additionally, our feautures were all dependent of each other since each feauture has an influence on the success rate of the shot. Through [PCA article](https://towardsdatascience.com/a-one-stop-shop-for-principal-component-analysis-5582fb7e0a9c), we learned that one of the strengths PCA possess would be transforming our  feautures in order to become independent. Therefore, we applied PCA with n_components as 8 to fit and transform all of our X features. Eventually, with all the pre-processing and variable creation complete, we implemented GradientBoostRegressor with n_estimators as 100 and learning_rate as 0.1 to help predict Stephen Curry's cumulative shot made. Although we tried using linear regression on our data, we feel that having n_estimators was much more efficient to learn the data better based on the number of trees in the forest. We chose 100 because we realized that adding more trees can slow down the training process considerably. Furthermore, we see that using a high learning rate results in overfitting and we concluded that learning rate of 0.1 would be the optimal choice.
<!-- aggregated and averaged 10 years of data for defensive rating among all teams and ranked them in descending order.-->
- all features we have are dependent (sicne they are all relate or have an influence on the success rate of the shot)
  - Used make_pipeline to assemble several of our steps so that it can be cross-validated together while setting different parameters.
  - used stadardscaler to make all comparable
  - used PCA to transform features to become independent (link article that mentions how the process of PCA turns anyting into independent cus... math)
  - given that the features are now independent of each other, satisfies the condition to use linear regression
  - use linear regression on our features to find
- want to predict number of shots made given historical data from 2009-2019
- We decided to implement a GradientBoostRegressor model that is used to *predict* our cumulative shot made.

## Results

Initially, we were questioning on Curry's performances against top, middle, and bottom defensive teams. Based on our outcome, we found that Curry is remarkably consistent in the number of shots he makes regardless of the defensive potency of the other team. 

 **This** or that defensive rating is a bad metric that doesn't fully represent how a team is on defense. This may be because of Defense Rating represents the whole team. The results may perhaps be different if a certain player guards him? However, we found that Curry seems to have a tendency to make a lot more shots, or in basketball lingo *explode*, in the first quarter against teams in the lower defensive ratings. ![Test](/curry-shots-made-by-minutes.png)


- Based on our training and validation score, we managed to achieve (*insert the 3 models with training and valid score*)
  - concludes that we arent over fitting
  - Talk about our accuracy using *r2_score*, using 2017-2018 and 2018-2019 as our input. (He mentioned to include 2 or more inputs)

## Limitations

Our initial question was to answer Curry's performance against other teams given a certain matchup. Though, we had some difficulties finding his performances for his matchup against opponents. We discovered [nba_api](https://github.com/swar/nba_api) and thought we could utilize their api and it had provided play-by-play stats. 

  - was under documented
  - connections would time out frequently regardless of size of request
  - found it to be very unreliable
  - slodged through api and managed to get matchup data
    - but data came aggregated and there were very few points
- found data on curry's shooting chart from [basketball-reference.com](https://www.basketball-reference.com/) with data points and information of each point embedded in html
  - realized that these data points were essentially play-by-play data of every shot he took
  - couldnt find a reliable source, so wrote `shot_webscrape.py` to scrape data

redefined our question to: Stephen Curry's shot made performance against top,mid,def teams.

### Things we would do if more time

- Definitely try to get an understanding of [nba_api](https://github.com/swar/nba_api). We could potentially make use of its aggregated data to find smth useful...
  - Interested in creating a model to predict other statistical performances such as assists, rebounds, and turnovers.
  - We would like to also predict his performance against X team instead of defensive ranks.
  - Would like to predict his performance against certain teams based on his matchups.

### Things we could have done better

-Although we thought of many ideas and algorithms on how to implement it.. we needede to make sure that we had the correct dataset.

