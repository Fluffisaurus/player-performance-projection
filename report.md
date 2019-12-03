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

In order to effectively predict Stephen Curry's shot made performance, we decided to separate teams based on their defensive ratings and ranked them from lowest to highest. We gathered historical data from 2009-2019 through [stats.nba.com](https://stats.nba.com/). We cleaned up three teams that went through rebrandings since 2009. 
- *Charlotte Bobcats* --> Charlotte Hornets
- *New Jersey Nets* --> Brooklyn Nets
- *New Orleans Hornets* --> New Orleans Pelicans

We aggregated and changed it to match present team. The next step was to average defensive rating across the decade and ranked them based on lowest to highest. 

![Defensive Rating](/data/defensive-rating/plot-nba-def-rating.png)

Furthermore, added acronyms for each team in order to merge with our play-by-play dataset. 


## Techniques
Through our play by play data, we were fully aware that we needed to use StandardScaler() in order to make it comparable, this is because we have features that scales differently such as our *shot_value*, *shot_distance*, and *cum_fg_percent*. Additionally, our feautures were all dependent of each other since each feauture has an influence on the success rate of the shot. Through [PCA article](https://towardsdatascience.com/a-one-stop-shop-for-principal-component-analysis-5582fb7e0a9c), we learned that one of the strengths PCA possess would be transforming our  feautures in order to become independent. Therefore, we applied PCA with n_components as 8 to fit and transform all of our X features. Eventually, with all the pre-processing and variable creation complete, we implemented GradientBoostRegressor with n_estimators as 100 and learning_rate as 0.1 to help predict Stephen Curry's cumulative shot made. Although we tried using linear regression on our data, we feel that having n_estimators was much more efficient to learn the data better based on the number of trees in the forest. We chose 100 because we realized that adding more trees can slow down the training process considerably. Furthermore, we see that using a high learning rate results in overfitting and we concluded that learning rate of 0.1 would be the optimal choice.
<!-- aggregated and averaged 10 years of data for defensive rating among all teams and ranked them in descending order.
- all features we have are dependent (sicne they are all relate or have an influence on the success rate of the shot)
  - Used make_pipeline to assemble several of our steps so that it can be cross-validated together while setting different parameters.
  - used stadardscaler to make all comparable
  - used PCA to transform features to become independent (link article that mentions how the process of PCA turns anyting into independent cus... math)
  - given that the features are now independent of each other, satisfies the condition to use linear regression
  - use linear regression on our features to find
- want to predict number of shots made given historical data from 2009-2019
- We decided to implement a GradientBoostRegressor model that is used to *predict* our cumulative shot made.
-->
## Results

Initially, we were questioning on Curry's performances against top, middle, and bottom defensive teams. Based on our outcome, we found that Curry is remarkably consistent in the number of shots he makes regardless of the defensive potency of the other team. 

 **This** or that defensive rating is a bad metric that doesn't fully represent how a team is on defense. This may be because of Defense Rating represents the whole team. The results may perhaps be different if a certain player guards him? However, we found that Curry seems to have a tendency to make a lot more shots, or in basketball lingo *explode*, in the first quarter against teams in the lower defensive ratings. ![Image](/curry-shots-made-by-minutes.png)


- Based on our training and validation score, we managed to achieve (*insert the 3 models with training and valid score*)
  - concludes that we arent over fitting
  - Talk about our accuracy using *r2_score*, using 2017-2018 and 2018-2019 as our input. (He mentioned to include 2 or more inputs)

## Limitations

Our initial question was to answer Curry's performance against other teams given a certain matchup. Though, we had some difficulties finding his performances for his matchup against opponents. We discovered [nba_api](https://github.com/swar/nba_api) and thought we could utilize their api and it has provided us play-by-play stats. From their api, the documentation were not clear and that there were many bugs that we discovered while using it. Furthermore, connections would time out frequently regardless of the size request. In the end, we managed to obtain matchup data except that the data came aggregated and that there were very few points for us to use. 

We also found data on Curry's shooting chart from [basketball-reference.com](https://www.basketball-reference.com/) with data points and information of each point embedded in HTML. We noticed that each of these data points were essentially play-by-play data of every shot he took. We decided to write a script `shot_webscrape.py` that scrapes all the data from the HTML. This results in redefining our question to: Stephen Curry's shot made performace against top, middle, and defensive teams. 

Things we would do if we had more time would be get an understanding of [nba_api](https://github.com/swar/nba_api). We could potentially make use of its aggregated data to find something useful such as ? Moreover, we were interested in creating a model to predict other statistical performances from Curry such as assists, rebounds, and turnovers. Since we know that shots made does not fully reflect on players overall performance. We were also interested in predicting his performance against one team instead of defensive rank teams. This is because we want to create an application to gain insight on his performance against one team instead of all ten teams. Additionally, we are looking forward to add certain matchups against Curry based on the team he's facing. 

Things we could have done better would be ensuring we had the correct dataset for our problem. Although we thought of many ideas and algorithms on how to implement, it is crucial to understand that data is significant in order to answer our question. 
