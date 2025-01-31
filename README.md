# Stock Market Sentiment Analyzer

A Python tool that analyzes investment sentiment for S&P 500 stocks using web scraping and AI-powered analysis.

## Features

- Validates stock symbols against S&P 500 company list
- Performs targeted Google searches for recent stock analysis articles
- Scrapes and processes article content while filtering out ads and irrelevant content
- Uses OpenAI's GPT model to generate investment sentiment analysis
- Provides clear Buy/Sell/Hold recommendations with supporting rationale

## Prerequisites

- Python 3.6+
- OpenAI API key set in environment variables
- Required Python packages:
    - `requests`
    - `beautifulsoup4`
    - `googlesearch-python`
    - `openai`
    - `tiktoken`

## Installation

1. Clone this repository
2. Install required packages:
     ```bash
     pip install requests beautifulsoup4 googlesearch-python openai tiktoken
     ```

## Usage

1. Run the program
2. Enter a valid S&P 500 stock symbol when prompted
3. Wait for the analysis to complete
4. Review the AI-generated sentiment analysis and investment recommendation

## How It Works

1. `validate()` checks if the input symbol exists in S&P 500
2. `scan()` performs Google searches for recent stock analysis
3. `scrape()` extracts relevant content from search results
4. `sentiment()` uses GPT to analyze the aggregated content
5. Results are presented with specific reasons for the recommendation

## Files

- `project.py` - Main program logic
- `stocks.csv` - S&P 500 company database
- `test_project.py` - Unit tests
- `URLs.txt` - Cached search results

## Testing

Run the test suite:
```bash
pytest test_project.py
```

## Limitations

- Depends on Google search results availability
- Requires active internet connection
- Analysis quality depends on OpenAI API availability
- Limited to S&P 500 stocks only
