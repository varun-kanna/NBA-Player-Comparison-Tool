# NBA-Player-Comparison-Script

Varun Kanna

* [Introduction](#Introduction)
* [How I got the Data](#how-i-got-the-data)
* [Formatting the Data](#Formatting-the-data)
* [Valid-Example](#Valid-Example)
* [Conclusion](#Conclusion)

## Introduction
* In this project, I use Python to help me "scrape" NBA.com stats for every player in the NBA. Specifically, I used the NBA Offical Leaders API to get the statistics of any player from any season. 
* I will go through how I got and used the API to get specific statistics for any player.
* As an example, I will show the usage of the Individual Player Efficiency on two players.

## How I got the Data
We will first look at how I was able to gather the data. If we go to https://www.nba.com/stats/leaders, it should look something similar to this.:
![NBA_players_webpage](https://user-images.githubusercontent.com/73306137/236642078-4f6a69d9-be15-4305-870d-9e1a7c87e3e0.png)
Here we can see each player and their statistics. This seems like it could work. Now go to the **Season** drop down and pick any arbitrary season. For this example, I will continue with the 2022-23 season. Afterwards, go to the **Season Type** any pick the season type. For this project, I will only use the Regular Season and Playoffs Stats. Nonetheless, for this example I will use the Regular Season. Now how can we get the specific stats from each player. Lets look at the network activity of the page. To do this, first inspect element the page by pressing F12 or by right-clicking then selecting inspect. Afterwards, head towards the Network tab and refresh the page. After you reload the page, you should see something like this. 

![image](https://user-images.githubusercontent.com/73306137/236642398-4a6c31d4-a5f2-4c2e-885e-c226d1adc764.png)
![image](https://user-images.githubusercontent.com/73306137/236642462-a8714894-caa0-447d-882a-c14511db8b8e.png)

Then double click the **leagueLeaders** tab. This should then show something like this

![image](https://user-images.githubusercontent.com/73306137/236642473-c5549df8-1769-459d-a195-95b9ba784698.png)
This is exactly what we want. This page gives us the statistics of each player that played in the 2022-23 Regular Season. 

## Formatting the Data
To get the specific stats like Points, Rebounds, and Assists, we need to get the specific header that will give us this information. If we use `["resultSet"]["headers"]` then we will get the headers that correlate to these statistics.

## Getting any Player's NBA statistics
Now we can go to the fun part. To get any player's statistics, we manipulate the request link to get statistics from any season (ex, 2022-23), and from any season type (Regular Season or Playoffs).

### Valid Example
This example is a valid comparison of LeBron James' and Steph Curry's Individual Player Efficiency in the 2020-2021 Season. The images are split for convenience.
![valid_example1](https://github.com/varun-kanna/NBA-Player-Comparison-Script/assets/73306137/28bb9c97-d794-4954-a9bb-1e9f2b98f5f2)
![valid_example2](https://github.com/varun-kanna/NBA-Player-Comparison-Script/assets/73306137/18f876c6-ca7a-4b41-9d09-fc8199326e6b)


## Conclusion
* Here, I used Python to scrape NBA.com for statistics on all the players in the NBA using the `requests` library. I then used the `numpy` and `time` libraries to make sure that I wasn't making too many requests. 
* Then, I used `pandas` to make a dataframe for the statistics of a specific player.
* I was then able to use dataframes of players to compute statistics.
* With these dataframes, I was able to compare these statistics between players.
* This project was fun to complete because I can easily get the statistics of any NBA player from either the Regular Season or Postseason without having to lookup their statistics.

