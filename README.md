# Player Performance Prediction

ML algorithm to predict Stephen Curry's performance statistics. Please read `report.md` for information about each script.

## How to run `shot_webscrape.py`

`shot_webscrape.py` takes two parameters, a `url` and a `file output name`

If you are in the root of the directory, you can run the script with the following generalized command

```{python}
python3 ./scripts/shot_webscrape.py [URL_OF_PLAYER_SHOOTING] [./PATH/TO/FOLDER/DATA.csv]
```

where `URL_OF_PLAYER_SHOOTING` is a URL from [basketball-reference](https://www.basketball-reference.com/) and is the page on the specified player's shooting history.

Here is an example of grabbing [Stephen Curry's shooting splits in 2010](https://www.basketball-reference.com/players/c/curryst01/shooting/2010) and saving it in the folder sub-structure `./data/shooting/curry-2009-2019/`.

```{python}
python3 ./scripts/shot_webscrape.py https://www.basketball-reference.com/players/c/curryst01/shooting/2010 ./data/shooting/curry-2009-2019/curry-2010.csv
```
Required Libraries: Pandas, Numpy, Matplotlib, sklearn, scipy, and seaborn. 

In order to run our scripted files, hardcoded datasets must be in the specified folder structure. 


