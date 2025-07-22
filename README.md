# Path-Efficiency-Ratio (PER)

A custom risk-adjusted return metric that evaluates how efficiently a trade captured profit relative to the worst drawdown and maximum unrealized gain during the trade.

PER penalizes trades that endure large heat or give back significant float, helping identify clean vs. sloppy trade executions.
Positive values indicate profitable trades, while negative values reflect losses or poor efficiency.

This is intended as a modification of John Netto's (Netto Number) Return per unit of risk metric: also taking into account round-tripping profitable trades.
