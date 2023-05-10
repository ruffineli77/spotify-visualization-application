
# Spotify Visualization Plan and Ideas

This project is straightforward. The user downloads their spotify data, uploads it to the website, and three visualizations are generated based on the user's streaming history and played artists.

Dash takes care of the user interface.

Charts and Graphs-
~ Bar chart
~ Pie chart
~ Scatterplot
~ Line charts

Topic 1 Steaming history- This viz could potentially tell us:
~ Top 15 most played songs
~ Top 10 most played artists
~ ms played/runtime (not total song runtime)
~ Favorite genre (requires api)

## Insights

Most streamed songs - Learn
Most played artists-
Favorite artists

## Project Creation Steps

1. Authorize access to a users a data.
3. Get a list/tuple of all streamed songs and all artists and convert it to a dataframe? array?
We get date and time played, artist name, song name and total play time from one
record in StreamingHistory.json. We only need artist name and song name for this viz.
4. Convert records/tuples into data that can be used by a visualization tool.
5. a

## Project Usage Steps

Version 1
Im sure theres an official API users can sign in to so I can directly access thier activity on Spotify.

Option 2. This might be better for people who have concerns about sharing their username and password online.

1. Download spotify data.
2. Upload the zip folder to the website.
3. Look at visualizations and explanations.


## Authorization

Spotify uses The OAuth framework.