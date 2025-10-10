# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

import numpy as np


# Filter for movies released in the 1990s
mov_rel_1990s = np.logical_and(netflix_df['release_year'] >= 1990, netflix_df['release_year'] < 2000)
movies_1990s = netflix_df['type'] == 'Movie'
movies_90s_filter = netflix_df[np.logical_and(mov_rel_1990s, movies_1990s)]

# Visualize the duration column to see the distribution
plt.hist(movies_90s_filter['duration'])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

# Store the duration column for later use
duration = movies_90s_filter['duration']

# Filter again to keep only Action movies
sa_movies = movies_90s_filter[movies_90s_filter['genre'] == 'Action']

# Find short Action movies (less than 90 minutes)
short_movies = sa_movies['duration'] < 90

# Count the number of short Action movies
short_movies_count = short_movies.sum()

print(short_movies_count)
