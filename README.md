# Spotify Optimal Musical Flow Reordering: Project Overview 
* Data mined 100 tracks from "Top Songs 2020" playlist, each song's audio features, artist ids, and genre of each artist and exported to .csv to do future analysis. 
* Wrangled streaming history dataset and audio feature dataset using python.
* Explored over 7,000 rows of streaming history to see what days and what time of day I stream the most and to see how Spotify orders their "Top Songs 2020" playlist. 
* Analyzed audio features of "Top Songs 2020" to see distribution and correlation of each to subsequently apply to our criteria of reodering songs.

## Conclusion
I found that I tend to like happier songs through analyzing valence and mode. By creating correlation graphs, I discovered that energy is highly correlated with other features. Furthermore, my own analysis shows an affinity for streaming music on Wednesdays at Noon.

Most importantly, this analysis has made my life easier by reordering songs to my preference and saved me time from manually locating each song to relocate. I believe that this analysis can be used in conjunction with Spotify's own "Wrapped". This solution to reordering songs can also be adapted for users to order by their own preference, not just by what has been analyzed in this EDA. 

## Code and Resources Used 
**Packages:** base64, requests, spotipy, json, pandas, numpy, seaborn, matplotlib.pyplot, sklearn (preprocessing)

**Data Mining Video:** https://www.youtube.com/watch?v=xdq6Gz33khQ&t=4345s

**Playlist Automation:** https://github.com/TheComeUpCode/SpotifyGeneratePlaylist/blob/master/create_playlist.py

## Data Mining
Mined audio features of 100 of my top songs of 2020. 

Features:
* energy
* liveness
* tempo
* speechiness
* acousticness
* instrumentalness
* time signature
* danceability 
* key
* duration (miliseconds)
* loudness
* valence
* mode
* type
* uri

As well as Artist ID from the playlist and Genre from Artist ID.

## Data Cleaning
After data mining and discovering the data I had, I made the following changes:
* Top Songs 2020
  * Removed the genre columns following the first
  * Removed time_signature, duration, and type
  * Replaced NaN values of genre to the mode
  * Mapped keys number into real letter keys
  * Added track name and artist to .csv file with audio features
    * Separated track name and artist into different cells in excel
    * Removed "{,}" from the cells after separating in excel
* Streaming History
  * Created new column for Seconds Played called sPlayed in Excel
  * Removed msPlayed 
  * Filtered endTime column so that we only have dates in 2020 and songs played 30 seconds or more
  * Created a weekdays column and hour time column that shows what hour AM/PM that I streamed
  * Remapped hour data after seeing it did not correctly represent the hours I streamed
  
## EDA
Below are a few graphs from my EDA.
![alt text](https://github.com/kodingwithkelly/OptimalFlowPlaylist/blob/main/Read%20me%20pngs/Correlation%20of%20Features.png "Correlation of Features")

![alt text](https://github.com/kodingwithkelly/OptimalFlowPlaylist/blob/main/Read%20me%20pngs/Correlation%20Between%20Energy%20%26%20Valence.png "Correlation Between Energy and Valence")

![alt text](https://github.com/kodingwithkelly/OptimalFlowPlaylist/blob/main/Read%20me%20pngs/Radar%20Chart.png "Radar Chart")

![alt text](https://github.com/kodingwithkelly/OptimalFlowPlaylist/blob/main/Read%20me%20pngs/Barchart%20of%20Streaming%20Hour.png "Barchart of Streaming Hour")


## Future Work
* Revisit to add another map that details when specific songs were streamed and create functions to map instead of having a cell for each map
* Create a website using streamlit for others to use and explore how they would like to reorder their own playlist :) 
