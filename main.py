import yfinance as yf
import pandas as pd
import numpy as np
import scipy.stats as stats

# Scarica i dati storici dello S&P 500
sp500 = yf.Ticker("^GSPC").history(start="1900-01-01", end="2020-01-01")

# Calcola i rendimenti giornalieri
returns = sp500['Close'].pct_change().dropna()

# Calcola la media e la deviazione standard dei rendimenti
mean = returns.mean()
std = returns.std()

# Calcola il numero di rendimenti che sono oltre le 4 sigma
num_4sigma = len(returns[returns > mean + 4*std]) + len(returns[returns < mean - 4*std])

# Calcola la probabilità teorica di rendimenti oltre le 4 sigma secondo la distribuzione normale
norm_prob_4sigma = 2 * (1 - stats.norm.cdf(4))*100

# Calcola la probabilità in percentuale di rendimenti oltre le 4 sigma
prob_4sigma = num_4sigma / len(returns) * 100

# Calcola il numero di rendimenti che sono oltre le 5 sigma
num_5sigma = len(returns[returns > mean + 5*std]) + len(returns[returns < mean - 5*std])

# Calcola la probabilità teorica di rendimenti oltre le 5 sigma secondo la distribuzione normale
norm_prob_5sigma = 2 * (1 - stats.norm.cdf(5))*100

# Calcola la probabilità in percentuale di rendimenti oltre le 5 sigma
prob_5sigma = num_5sigma / len(returns) * 100
# Stampa il numero di rendimenti oltre le 4 e le 5 sigma e le relative probabilità teoriche e in percentuale
print(f"Numero di rendimenti oltre le 4 sigma: {num_4sigma}")
print(f"Probabilità teorica di rendimenti oltre le 4 sigma (normale): {norm_prob_4sigma:.4f}%")
print(f"Probabilità di rendimenti oltre le 4 sigma: {prob_4sigma:.4f}%")
print(f"Numero di rendimenti oltre le 5 sigma: {num_5sigma}")
print(f"Probabilità teorica di rendimenti oltre le 5 sigma (normale): {norm_prob_5sigma:.4f}%")
print(f"Probabilità di rendimenti oltre le 5 sigma: {prob_5sigma:.4f}%")
