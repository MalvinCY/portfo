# TFL Bus Safety Dashboard

An **interactive Tableau dashboard** visualising Transport for London (TFL) bus safety incident data from January 2015 to September 2018. The dashboard enables exploration of accident reports across all London boroughs with drill-down by area, time period, incident type, and severity.

[![Tableau Dashboard](https://img.shields.io/badge/Tableau-View%20Dashboard-blue?logo=tableau&logoColor=white)](https://public.tableau.com/views/TFLBusincidents/Dashboard1?:language=en-GB&:display_count=n&:origin=viz_share_link)

## Dashboard Preview

> **[View the live dashboard on Tableau Public](https://public.tableau.com/views/TFLBusincidents/Dashboard1?:language=en-GB&:display_count=n&:origin=viz_share_link)**

### Features

- **Incidents by Borough** — Horizontal bar chart ranking boroughs by total incident count, with click-to-filter functionality
- **Incidents by Borough & Type** — Stacked breakdown of incident categories per borough
- **Incidents over Time** — Time-series trend line showing seasonal patterns and year-on-year changes
- **Incidents by Route** — Identification of the highest-risk bus routes
- **Incidents by Season** — Seasonal analysis revealing peak periods for bus safety incidents
- **Incident Treemap** — Hierarchical visualisation of incident distribution

## Key Insights

- Westminster, Lambeth, and Southwark consistently report the highest number of incidents
- Incident rates show seasonal variation, with certain periods experiencing notable spikes
- Specific routes account for a disproportionate share of total incidents
- The dashboard supports data-driven decision-making for urban transport safety improvements

## Project Structure

```
TFL-Bus-Safety/
├── TFL Bus Safety.xlsx    # Raw incident data from Transport for London
├── HTMLscript             # HTML embed code for the Tableau dashboard
└── README.md
```

## Data Source

Bus safety incident data published by **Transport for London (TFL)**, covering reported accidents across all London boroughs from January 2015 to September 2018.

## Tech Stack

| Tool | Purpose |
|------|---------|
| Tableau Public | Interactive dashboard and data visualisation |
| Excel | Data storage and initial exploration |

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/MalvinCY/TFL-Bus-Safety.git
   ```

2. Open `TFL Bus Safety.xlsx` to explore the raw data.

3. Visit the [live Tableau dashboard](https://public.tableau.com/views/TFLBusincidents/Dashboard1?:language=en-GB&:display_count=n&:origin=viz_share_link) to interact with the visualisations.

## Author

**Malvin Siew** — [GitHub](https://github.com/MalvinCY) · [LinkedIn](https://www.linkedin.com/in/malvin-siew/)
