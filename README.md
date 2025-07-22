# Path-Efficiency-Ratio (PER)

A custom risk-adjusted return metric that evaluates how efficiently a trade captured profit relative to the max unrealized drawdown (AKA heat) and maximum unrealized gain (AKA float) during the trade.

PER penalizes trades that endure large heat or give back significant float, helping identify clean vs. sloppy trade executions.
Positive values indicate profitable trades, while negative values reflect losses or poor efficiency.

This is intended as a modification of John Netto's (Netto Number) Return per unit of risk metric: also taking into account round-tripping profitable trades.

<img width="794" height="310" alt="image" src="https://github.com/user-attachments/assets/d55b4f3f-6f1c-4b38-8db8-04bd08e350dd" /> <img width="299" height="136" alt="image" src="https://github.com/user-attachments/assets/f414a2bc-60db-4804-89af-b9e0c1874b9e" />

