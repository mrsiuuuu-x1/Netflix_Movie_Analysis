# 🎬 Netflix Movie Analysis

A Python-based data analysis project that explores Netflix movie and TV show data, including durations, genres, and yearly trends.

## 📋 Project Overview

This project performs exploratory data analysis (EDA) on Netflix's catalog, examining movies and TV shows by release year, duration, and genre. It uses pandas for data manipulation, matplotlib and seaborn for visualization, and NumPy for filtering.

## 🎯 Objectives

- Analyze the duration distribution of Netflix movies from the 1990s
- Identify and examine short action films in the dataset
- Visualize patterns and trends in movie lengths
- Compare the total number of TV Shows and Movies on Netflix
- Visualize the amount of content produced each year (line graph)
- Display the most common genres on Netflix
- Visualize the distribution of movie durations in the 2010s
- Count and display short action movies (less than 90 minutes)
- Save all visualizations as PNG files for reporting/sharing
- Provide insights into content characteristics from different eras
- **NEW:** Visualize the top 10 directors with the most content on Netflix
- **NEW:** Ensure y-axis values in director and genre bar charts are shown as integers for clarity

## 🛠️ Technologies Used

- **Python** - Primary programming language
- **pandas** - Data manipulation and analysis
- **matplotlib.pyplot** - Data visualization and plotting
- **seaborn** - Advanced data visualization
- **NumPy** - Numerical computing and array operations

## 📊 Analysis Features

- **Data Loading**: Reads Netflix data from CSV file using pandas
- **1990s Movie Filtering**: Filters movies released between 1990-1999
- **2010s Movie Filtering**: Filters movies released between 2010-2019
- **Duration Analysis**: Histograms showing distribution of movie durations for all movies, 1990s, and 2010s
- **Action Genre Filtering**: Isolates action films for specific analysis
- **Short Movie Identification**: Finds and counts action movies under 90 minutes
- **Content Type Visualization**: Bar chart showing the count of Movies vs TV Shows on Netflix, with improved annotation
- **Yearly Content Trend**: Line graph showing the number of titles released each year
- **Genre Popularity**: Bar chart of the top 10 most common genres on Netflix
- **Automatic Saving**: All plots are saved as PNG files for easy sharing
- **NEW:** Bar chart of the top 10 directors with the most content on Netflix
- **NEW:** Integer-only y-axis ticks for genre and director bar charts for improved readability

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.7+
pandas
matplotlib
numpy
seaborn
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mrsiuuuu-x1/Netflix_Movie_Analysis.git
cd Netflix_Movie_Analysis
```

2. Install required packages:
```bash
pip install pandas matplotlib numpy seaborn
```

3. Run the analysis:
```bash
python netflix_project.py
```

## 📁 Project Structure

```
Netflix_Movie_Analysis/
│
├── netflix_project.py      # Main analysis script
├── netflix_data.csv        # Netflix dataset
└── README.md               # Project documentation
```

## 📈 Visualizations

The project includes:
- **Histogram**: Distribution of movie durations for all movies, 1990s, and 2010s
  - X-axis: Duration in minutes
  - Y-axis: Number of movies
  - Titles: "Distribution of Movie Durations on Netflix", "Distribution of Movie Durations in the 1990s", "Distribution of Movie Durations in the 2010s"
- **Bar Chart**: Number of Movies vs TV Shows on Netflix (with clear, non-overlapping annotations)
  - X-axis: Content Type (Movie or TV Show)
  - Y-axis: Count
  - Title: "Total Number of TV Shows and Movies on Netflix"
- **Line Graph**: Number of titles released each year
  - X-axis: Release Year
  - Y-axis: Amount of Content
  - Title: "Number of Titles Released Each Year on Netflix"
- **Bar Chart**: Top 10 most common genres on Netflix
  - X-axis: Genre
  - Y-axis: Number of Shows/Movies
  - Title: "Top 10 Most Common Genres on Netflix"
- **Bar Chart**: Top 10 directors with the most content on Netflix
  - X-axis: Director
  - Y-axis: Number of Shows/Movies (integer ticks)
  - Title: "Top 10 Directors with Most Content on Netflix"

## 💡 Insights

This analysis provides valuable insights into:
- How movie durations varied during the 1990s and 2010s
- The prevalence of different film lengths
- Patterns specific to action films and short movies
- Content characteristics in Netflix's historical catalog
- Trends in content production over the years
- Popular genres on Netflix
- **NEW:** Which directors have the most content available on Netflix

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this analysis:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add new analysis'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**Abdul Rafay**

- GitHub: [@mrsiuuuu-x1](https://github.com/mrsiuuuu-x1)
- LinkedIn: [Abdul Rafay](https://www.linkedin.com/in/abdul-rafay-104084352/)

## 🙏 Acknowledgments

- Netflix for providing rich content data
- The Python data science community for excellent tools and libraries
- Contributors and supporters of this project

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

---

⭐ If you found this project useful, please consider giving it a star!
