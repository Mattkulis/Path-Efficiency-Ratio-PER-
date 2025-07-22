# Path-Efficiency-Ratio (PER)

A custom risk-adjusted return metric that evaluates how efficiently a trade captured profit relative to the max unrealized drawdown (AKA heat) and maximum unrealized gain (AKA float) during the trade.
*Note* This is intended as a modification of John Netto's (Netto Number) Return per unit of risk metric: also taking into account round-tripping profitable trades.

PER penalizes trades that endure large heat or give back significant float, helping identify clean vs. sloppy trade executions.
Positive values indicate profitable trades, while negative values reflect losses. the greater the absolute value of the output the more efficient the trade: for better or worse.

EX:
You can have a  -0.99 indicating it was incredibly efficient at losing as much money as possibly on the trade without very much upside, on the flip side a +0.99 means incredibly efficient at retaining unrealized profits.
a score of +2.0 means that the trade retained 100% of unrealized profits while only incurring an unrealized loss of 1/2 the retained unrealized gain. 



<img width="794" height="310" alt="image" src="https://github.com/user-attachments/assets/d55b4f3f-6f1c-4b38-8db8-04bd08e350dd" /> <img width="299" height="136" alt="image" src="https://github.com/user-attachments/assets/f414a2bc-60db-4804-89af-b9e0c1874b9e" />

