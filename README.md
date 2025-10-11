# 🎬 Netflix Movie Analysis

A Python-based data analysis project that explores Netflix movie durations from the 1990s, with a focus on identifying patterns in film length and discovering short action movies.

## 📋 Project Overview

This project performs an exploratory data analysis (EDA) on Netflix's movie catalog, specifically examining films released during the 1990s. Using pandas for data manipulation and matplotlib for visualization, the analysis investigates the distribution of movie durations and identifies trends in action films.

## 🎯 Objectives

- Analyze the duration distribution of Netflix movies from the 1990s
- Identify and examine short action films in the dataset
- Visualize patterns and trends in movie lengths
- Provide insights into content characteristics from this era

## 🛠️ Technologies Used

- **Python** - Primary programming language
- **pandas** - Data manipulation and analysis
- **matplotlib.pyplot** - Data visualization and plotting
- **NumPy** - Numerical computing and array operations
- **VS Code** - Development environment

## 📊 Analysis Features

- **Data Loading**: Reads Netflix data from CSV file using pandas
- **1990s Movie Filtering**: Filters movies released between 1990-1999
- **Duration Analysis**: Statistical examination of movie lengths
- **Action Genre Filtering**: Isolates action films for specific analysis
- **Short Movie Identification**: Finds action movies under 90 minutes
- **Data Visualization**: Histogram showing duration distribution with labeled axes
- **Content Type Visualization**: Bar chart showing the count of Movies vs TV Shows on Netflix using matplotlib/seaborn

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.7+
pandas
matplotlib
numpy
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mrsiuuuu-x1/Netflix_Movie_Analysis.git
cd Netflix_Movie_Analysis
```

2. Install required packages:
```bash
pip install pandas matplotlib numpy
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

## 🔍 Key Findings

The analysis explores:
- Movies released during the 1990s (1990-1999) from the Netflix catalog
- Distribution patterns of movie durations through histogram visualization
- Action movies specifically and their duration characteristics
- Short action films (those under 90 minutes in length)
- Data filtering techniques using pandas and NumPy

## 📈 Visualizations

The project includes:
- **Histogram**: Distribution of movie durations in the 1990s
  - X-axis: Duration in minutes
  - Y-axis: Number of movies
  - Title: "Distribution of Movie Durations in the 1990's"
  - **Bar Chart**: Shows the number of Movies vs TV Shows on Netflix
  - X-axis: Content Type (Movie or TV Show)
  - Y-axis: Count
  - Title: "Movies vs TV Shows on Netflix"

## 💡 Insights

This analysis provides valuable insights into:
- How movie durations varied during the 1990s
- The prevalence of different film lengths
- Patterns specific to action films
- Content characteristics in Netflix's historical catalog

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
