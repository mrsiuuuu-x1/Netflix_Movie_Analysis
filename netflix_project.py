# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

import numpy as np
import seaborn as sns

# Filter for movies released in the 1990s
mov_rel_1990s = np.logical_and(netflix_df['release_year'] >= 1990, netflix_df['release_year'] < 2000)
movies_1990s = netflix_df['type'] == 'Movie'
movies_90s_filter = netflix_df[np.logical_and(mov_rel_1990s, movies_1990s)]

# Visualizing the distribution of movie durations
plt.figure(figsize=(10, 6))
plt.hist(netflix_df[netflix_df['type'] == 'Movie']['duration'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Movie Durations on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('movie_duration_distribution.png')
plt.show()

# Visualize the duration column to see the distribution of the 1990s decade
plt.figure(figsize=(10, 6))
plt.hist(movies_90s_filter['duration'],color='skyblue', edgecolor='black')
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('movie_duration_distribution_1990s.png')
plt.show()

#Visualizing the duration column to see the distribution of the 2010s decade
mov_rel_2010s = np.logical_and(netflix_df['release_year'] >= 2010, netflix_df['release_year'] < 2020)
movies_2010s_filter = netflix_df[np.logical_and(mov_rel_2010s, movies_1990s)]
plt.figure(figsize=(10, 6))
plt.hist(movies_2010s_filter['duration'],color='skyblue', edgecolor='black')
plt.title('Distribution of Movie Durations in the 2010s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('movie_duration_distribution_2010s.png')
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

# visualizing the total number of TV Shows and Movies
plt.figure(figsize=(8, 6))
ax = sns.countplot(x='type', data=netflix_df, color='skyblue', edgecolor='black')
plt.title('Total Number of TV Shows and Movies on Netflix')
plt.xlabel('Content Type')
plt.ylabel('Count')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate each bar with its count
for p in ax.patches:
    ax.annotate(
        str(p.get_height()),
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center', va='bottom', fontsize=12, color='black', fontweight='bold'
    )
plt.savefig('total_tv_shows_movies.png')
plt.show()


# Visualizing amount of content produced each year as a line graph
plt.figure(figsize=(12, 6))
year_counts = netflix_df['release_year'].value_counts().sort_index()
plt.plot(year_counts.index, year_counts.values, marker='o', color='blue')
plt.title('Number of Movies/Shows Released Each Year on Netflix')
plt.xlabel('Release Year')
plt.ylabel('Amount of Content')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('content_per_year.png')
plt.show()

# Visualizing most common genres on Netflix
plt.figure(figsize=(12, 6))
genre_counts = netflix_df['genre'].value_counts().head(10)
sns.barplot(x=genre_counts.index, y=genre_counts.values, palette='viridis')
plt.title('Top 10 Most Common Genres on Netflix')
plt.xlabel('Genre')
plt.ylabel('Number of Shows/Movies')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('top_10_genres.png')
plt.show()

# Visualizing best directors on Netflix
plt.figure(figsize=(12, 6))
director_counts = netflix_df['director'].value_counts().head(10)
ax = sns.barplot(x=director_counts.index, y=director_counts.values, palette='magma')
plt.title('Top 10 Directors with Most Content on Netflix')
plt.xlabel('Director')
plt.ylabel('Number of Shows/Movies')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))  # <-- Add this line
plt.savefig('top_10_directors.png')
plt.show()