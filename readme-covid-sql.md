# Covid Global Impact Analysis

A **SQL-driven exploration** of worldwide Covid-19 data — examining mortality rates, infection spread, and vaccination progress across countries and continents. Key findings are presented through an **interactive Tableau dashboard**.

[![Tableau Dashboard](https://img.shields.io/badge/Tableau-View%20Dashboard-blue?logo=tableau&logoColor=white)](https://public.tableau.com/views/CovidGlobalStatistics/Dashboard1?:language=en-GB&:display_count=n&:origin=viz_share_link)

## Dashboard Preview

The interactive Tableau dashboard allows filtering by country, date range, and metric type — providing at-a-glance views of infection rates, death percentages, and vaccination timelines.

> **[View the live dashboard on Tableau Public](https://public.tableau.com/views/CovidGlobalStatistics/Dashboard1?:language=en-GB&:display_count=n&:origin=viz_share_link)**

## SQL Techniques Used

- **Common Table Expressions (CTEs)** for readable, modular queries
- **Window functions** for running totals and rolling averages
- **Temporary tables** for multi-step transformations
- **Aggregate functions** for country- and continent-level summaries
- **JOINs** across deaths, cases, and vaccination datasets

## Analysis Highlights

- Global case and death counts with death-to-case percentage
- Continent-level mortality comparisons
- Country-level infection rates as a percentage of population
- Vaccination rollout progress over time
- Percent population infected per country (choropleth map)

## Project Structure

```
CovidSQL/
├── CovidAnalysis          # SQL queries for data exploration and analysis
├── CovidForTableau.sql    # SQL used to prepare data for Tableau visualisation
└── README.md
```

## Data Source

Data sourced from [Our World in Data](https://ourworldindata.org/covid-deaths), which compiles figures from Johns Hopkins University, national health agencies, and the WHO.

## Tech Stack

| Tool | Purpose |
|------|---------|
| SQL (MS SQL Server) | Data exploration and analysis |
| Tableau Public | Interactive dashboard and visualisation |

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/MalvinCY/CovidSQL.git
   ```

2. Import the SQL files into your preferred SQL environment (SQL Server, PostgreSQL, etc.).

3. Run the queries in `CovidAnalysis` to explore the data, then use `CovidForTableau.sql` to generate the aggregated views used in the dashboard.

## Author

**Malvin Siew** — [GitHub](https://github.com/MalvinCY) · [LinkedIn](https://www.linkedin.com/in/malvin-siew/)
