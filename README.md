Investors interested in an aggressive trading strategy would prefer to have at least 100% exposure in equity positions.

The simplest way to achieve this is to trade on margin, or in other words, borrowing money for the purposes of investing it in the stock market. However, current margin rates are around 11-12%, which can absorb or outright outpace any gains from stock market investments made using the additional capital.

An alternative is to create synthetic leverage using long-dated, in-the-money (ITM) call options on a core position. This analysis will focus on SPY, the ETF which tracks the S&P500, as the core position and underlying security. We will consider call options which are deep ITM all the way to close to ATM, with maturities at least 1 or 2 years into the future. We will see if we can create synthetic leverage--that is--an equity exposure in a portfolio which is in effect greater than 100%, by mixing in these long-dated ITM calls along with a core position in an investment portfolio.

We will craft an arsenal of analysis tools to determine if such a strategy would work in creating leverage, and whether the cost of this leverage is more or less than the cost of capital of opening a standard margin account. We will use our analysis tools to consider various investment strategies involving long-dated ITM calls, with choices in maturity and roll schedule, and benchmark their performance against a strategy which simply invests 100% in the core position, as well a strategy which involves investing in the core position with leverage from a margin account.

TODO:
1. Data imports for SPY options chain
2. Simple homemade implementations for Black-Scholes d1, d2, delta, and call price
3. A suite of performance metrics for a given strategy template
4. A set of reasonable strategy templates
5. Benchmark performance metrics (100% equity, 100+25% equity w/ margin)
6. Identify the best combination of strike, maturity, and roll schedule
7. Historical data and back-testing

Tentative directory structure:
./
./pricing: homemade options pricing utils
./performance: functions to evaluate payoff given a strategy template, using pricing functions
./strategies: various strategy templates and their corresponding analysis, using performance functions
./strategies/benchmark: benchmark performance
./trade: import current financial data and make a strategy selectoin
./trade/backtest: input strategy parameters and backtest as far as data allows