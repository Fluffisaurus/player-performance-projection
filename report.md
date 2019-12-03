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

Stephen Curry is the best shooter that has ever graced the NBA and is soley responsible for the rennaissance of the three-point era. His marksmanship lead him to his first MVP in 2014-15 and subsequently becoming the first unanimous MVP in 2015-16 the year after. Given his unparalled skillset, we wonder how much of his shooting performance (shots made) is influenced by the opposing defense.

For a decent measure of a team's defensive potency, we will be using ESPN John Hollinger's *defensive efficiency* or more commonly *defensive rating* stat that estimates the number of points a team allows per 100 possessions. We will be ranking and binning the teams into three categories based on their [defensive ratings](#team-defensive-data-for-the-past-decade) - top, middle, and bottom defensive ratings.

We are primarily interested in the number of shots Curry makes as time passes in a game, specifically the cumulative number of shots`cum_shot_made`.



<!-- Stephen Curry from the Golden State Warriors had some spectacular seasons and managed to win his first MVP award and the first player in NBA history to be elected MVP unanimously. We are interested in Stephen Curry's performance against top, middle, and bottom defensive rank teams based on each teams defensive ratings from 2009-2019. We are curious to observe how many shots were made against certain tiers.   -->

## Idea Refinement



## Data Collection, Cleaning, and Preprocessing Process

A majority of our data was collected from [basketball-reference.com](https://www.basketball-reference.com/), [pbpstats.com](http://www.pbpstats.com/), and [stats.nba.com](https://stats.nba.com/). We obtained data from

### Webscrape

We were unable to access play-by-play data online without being met by a pay wall. Luckily enough, we found [shooting chart data](https://www.basketball-reference.com/players/c/curryst01/shooting/2018) on basketball-reference. Each of marks on the chart represents a shot Curry took in that respective season and was embedded as data in an html element. Given that it is an HTML element, we realized that we could scrape the data online and format it into our own dataset.

The webscrape parses data points in the form

```python
<div class="tooltip make" style="top:292px;left:335px;" tip="Oct 17, 2017, GSW vs HOU&lt;br&gt;1st Qtr, 8:09 remaining&lt;br&gt;Made 3-pointer from 25 ft&lt;br&gt;GSW now leads 15-7">●</div>
```

and cleans / transforms it into a dataframe with this sample row

| date | home | vs | quarter | time_left | shot_made | shot_value | shot_distance | x | y | shot_description | game_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2017-10-17 | True | HOU | 1 | 08:09 | True | 3 | 25 | 335 | 292 | Made 3-pointer from 25 ft | GSW now leads 15-7 |

We ran `shot_webscrape.py` 10 times for each of the seasons Curry played since his rookie year of 2009 to last season 2019. We collected 13,905 rows which should represnet the total number of shots Curry took in his career up until the end of the 2019 season. The results of our data collected can be seen in the `/data/shooting/curry-2009-2019/` in the projecte directory.

For more information about our webscrape script, refer to our `README.md` on how to use it and `/scripts/shot_webscrape.py` to see the code.

<!-- - Scraped shotchart data and parsed into dataframe with columns since Curry's rookie season 2009-10 to 2018-19
- script generates dataframe with 10 columns
  - [insert example of dataframe row 1 here]
- in total over the 10 years, yielded around 14k rows of data -->

### Team Defensive Rating Data from 2009-2019

Given that our shot data for Curry spans over 10 years, we decided it would be appropriate to take team defensive data over 10 years as well. Our goal was to come up with a decisive list of the decade's best defensive teams and rank them accordingly.

We gathered each team's historical defensive ratings data from 2009-2019 through [stats.nba.com](https://stats.nba.com/). During this period, three teams underwent rebrandings. We cleaned our collected files in `/data/defensive-rating/` and matched the *old team names* with their current team names.

- *Charlotte Bobcats* == Charlotte Hornets
- *New Jersey Nets* == Brooklyn Nets
- *New Orleans Hornets* == New Orleans Pelicans

We then aggregated the defensive rating data for each team and averaged it to get a 10 year average defensive rating. We then re-ranked the teams accordingly and added acronyms for each team for use in [preprocessing](#preprocessing). Finally we exported it as `tm-defrtg-avg-2009-2019.csv`. The graph below shows our resulting aggregated defensive ratings.

![Defensive Rating](/figures/plot-nba-def-rating.png)

The steps in this process were done in the jupyter notebook found in `/scripts/DefensiveRatings_teams.ipynb`.

### Preprocessing

After collecting the data, our main preprocessing work was to combine all the webscraping data into one dataframe that was exported as the csv file, `/data/shot-data-all.csv`. We added a column for cumulative shots made, cumulative attempts, and cumulative field goal percentage (made / attempts).

With the aggregated defensive ratings from the previous [section](#team-defensive-rating-data-from-2009-2019), we split teams into three tiers based on their 10 year defensive rankings - top, middle, and bottom. We subsetted Curry's shooting data from `shot-data-all.csv` into individual csv's `/data/top-def.csv`, `/data/mid-def.csv`, and `/data/bot-def.csv`. By separating out Curry's shooting data by tier, we can then analyze and check whether there is a stasitical significance in his shooting performances against each tier.

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


## Project Experience
