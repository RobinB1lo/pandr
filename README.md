# Analysis and Forecasting of Ottawa Rent and Population Trends

This project explores the relationship between Ottawa’s population growth and rental-market dynamics, and demonstrates a streamlined forecasting pipeline.

Objective: Test the hypothesis that rising population drives higher rent levels.

Dataset: Publicly available historical series of Ottawa’s population counts and median rental prices.

## Approach:

Data Wrangling – Load, clean, and align annual population and rent data.

Exploratory Analysis – Plot year-over-year percentage changes, compute rolling correlations.

Time-Series Modeling – Build an ARIMAX model treating percent change in population as an exogenous driver of rent.

Forecasting & Validation – Generate out-of-sample forecasts and visualize confidence intervals.

## Key Findings:

Historical rent–population correlation highlights a clear positive relationship.

Model accuracy is currently limited by data volume and granularity.

## Next Steps:

Incorporate higher-frequency or more granular (neighborhood-level) data.

Experiment with multivariate or machine-learning models to capture non-linear effects.

Extend the pipeline to include other drivers (e.g., mortgage rates, employment).

With more comprehensive data, this framework can deliver actionable insights for real-estate planning, pricing strategy, and risk management.