# Stock Correlation Analysis

## Project Overview
The **Stock Correlation Analysis** project analyzes the historical price data of various stocks to:
- Determine correlations between stock price movements.
- Visualize correlations using heatmaps and network graphs.
- Perform Principal Component Analysis (PCA) to understand market trends and sector trends.
- Cluster stocks based on their correlation patterns.

The project includes two components:
1. **`stock_correlation_analysis.ipynb`**: A Jupyter Notebook that provides detailed analysis and visualizations.
2. **`stock_analysis.py`**: A Streamlit-based web application for interactive exploration of stock data.

## Features
### `stock_correlation_analysis.ipynb`
1. **Fetch Stock Data**
   - Downloads historical stock prices using the Yahoo Finance API.
   - Accepts a list of stock tickers, start date, end date, and interval.

2. **Correlation Heatmap**
   - Displays a heatmap of stock price correlations.

3. **Network Graph**
   - Creates a graph to visualize relationships between stocks with high correlations (>0.8).

4. **Volatility Analysis**
   - Calculates the volatility of each stock based on percentage changes in closing prices.

5. **Principal Component Analysis (PCA)**
   - Reduces the dimensionality of stock returns to identify market and sector trends.
   - Visualizes explained variance and stock projections in PCA space.
   - Calculates the cumulative explained variance (R² value).

6. **Clustering**
   - Uses K-Means clustering to group stocks based on their correlation patterns.

### `stock_analysis.py`
1. **Interactive Streamlit App**
   - Upload a CSV file containing stock tickers.
   - Automatically fetches historical stock data and calculates correlations.

2. **Heatmap Visualization**
   - Displays an interactive heatmap of stock correlations using Matplotlib and Seaborn.

## Requirements
### Python Libraries
- `yfinance`: Fetch stock data from Yahoo Finance.
- `pandas`: Handle and manipulate data.
- `seaborn`: Generate heatmaps.
- `matplotlib`: Create plots and visualizations.
- `networkx`: Create network graphs for stock relationships.
- `numpy`: Perform numerical computations.
- `scikit-learn`: Perform PCA and clustering.
- `streamlit`: Build an interactive web application.

### Installation
Install the required libraries using the following command:
```bash
pip install yfinance pandas seaborn matplotlib networkx scikit-learn streamlit
```

## How to Use
### Jupyter Notebook
1. Open `stock_correlation_analysis.ipynb` in a Jupyter Notebook environment.
2. Run each cell to:
   - Fetch stock data.
   - Visualize correlations and trends.
   - Perform clustering and PCA.
3. Save analysis results to CSV or view visualizations directly.

### Streamlit Application
1. Run the Streamlit app using the following command:
   ```bash
   streamlit run stock_analysis.py
   ```
2. Upload a CSV file containing stock tickers in the following format:
   ```csv
   ,Ticker
   0,AAPL
   1,MSFT
   2,GOOGL
   ```
3. View the correlation heatmap directly in the web interface.

## Example Usage
### Input
- **Tickers**: `AAPL`, `MSFT`, `GOOGL`, `AMZN`, `TSLA`
- **Date Range**: `2020-01-01` to `2023-01-01`

### Output
1. **Correlation Heatmap**: Visual representation of stock price correlations.
2. **Network Graph**: Graph showing relationships between highly correlated stocks.
3. **PCA Results**: Variance explained and stock projections.
4. **Clustered Stocks**: Stocks grouped by similarity in price movements.

## Files
1. **`stock_correlation_analysis.ipynb`**
   - Jupyter Notebook containing detailed analysis and visualizations.
2. **`stock_analysis.py`**
   - Streamlit app for interactive analysis.

## Outputs
- **Visualizations**: Heatmaps, network graphs, and PCA scatter plots.
- **CSV File**: `stock_data.csv` containing historical stock prices.

## Results
- The correlation heatmap and network graph reveal relationships between stock price movements.
- PCA identifies major market and sector trends.
- Clustering groups stocks with similar price behaviors.

## Future Enhancements
- Add support for additional financial metrics (e.g., volume, P/E ratio).
- Incorporate additional clustering algorithms.
- Extend the Streamlit app with more visualization options.

## License
This project is licensed under the MIT License.

## Author
Nagarjunan Saravanan

