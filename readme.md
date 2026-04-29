# Binance Trading Bot CLI

## Overview
A Python-based CLI trading bot that simulates placing BUY/SELL orders using real-time market data from Binance.  
It supports both MARKET and LIMIT orders and demonstrates trading logic with structured logging.


## Features
- Place BUY/SELL orders
- Supports MARKET & LIMIT orders
- Real-time price fetching from Binance
- Order execution simulation
- Logging system


## Tech Stack
- Python 3
- python-binance library


## How to Run
- Install dependencies:
  pip install -r requirements.txt

- Run the program:
  python cli.py


## Example Use Case
Simulate placing a LIMIT BUY order and check whether it executes based on the current market price.


## What I Learned
- Working with APIs (Binance)
- CLI application design
- Input validation & error handling
- Implementing trading logic
- Structuring Python projects


## Sample Output (Optional)
Example of placing LIMIT and MARKET orders :
![CLI output](image.png)


## Note
This project simulates trading and does NOT place real orders.