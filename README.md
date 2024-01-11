# Twitter Data Analysis Project

This project is focused on analyzing a dataset of tweets using various Python libraries such as `pickle`, `pandas`, `nltk`, `collections`, `matplotlib`, `geopandas`, and more.

## Dataset

The dataset used for this project consists of approximately 10,000 tweets from January 2020. The tweets are stored in a `.jsonl` file and loaded into a Python list using the `pickle` library.

## Project Overview

The project involves the following analyses:

1. **Word Frequency Analysis**: This analysis involves tokenizing the text of the tweets, removing stopwords, and counting the frequency of the remaining words. The top 15 most frequent words are then plotted in a bar chart.

2. **Tweet Source Analysis**: This analysis involves extracting the source field from each tweet, which indicates the device or platform used to post the tweet. The frequency of each source is counted and the top 10 most common sources are plotted in a bar chart.

3. **Tweet Timing Analysis**: This analysis involves extracting the time of each tweet and plotting the frequency of tweets by hour of the day. This analysis is specifically focused on users with a high number of followers or friends.

4. **Hashtag Analysis**: This analysis involves extracting the hashtags used in each tweet. The frequency of each hashtag is counted and the top hashtags are printed to the console.

5. **Entities Analysis**: This analysis involves calculating the average length of the fields in the 'entities' object of each tweet. The average lengths are then plotted in a bar chart.

6. **User Boolean Field Analysis**: This analysis involves counting the frequency of `True` and `False` values for each boolean field in the 'user' object of each tweet. The frequencies are then plotted in a pie chart.

7. **Username Analysis**: This analysis involves extracting the first character of each username and counting the frequency of each character. The frequencies are then plotted in a line chart.

8. **Location Analysis**: This analysis involves counting the frequency of each location in the 'user' object of each tweet. The frequencies are then plotted on a world map using the `geopandas` library.

## Techniques and Tools Used

The project employed various data collection and preprocessing techniques. The Python libraries used include `pickle` for loading the dataset, `pandas` for data manipulation, `nltk` for text processing, `collections` for counting frequencies, `matplotlib` for plotting charts, and `geopandas` for plotting the world map.

## Results and Findings

The results of each analysis are visualized in various charts, including bar charts, pie charts, a line chart, and a world map. The project demonstrates the potential of Python for data analysis and provides detailed insights into the dataset of tweets.
