


Create table StockDailyPrice
(
YearID int,
MonthID int,
DayID int,
StockID nvarchar(4),
StockName nvarchar(100),
OpenPrice money,
ClosePrice money,
HighPrice money,
LowPrice money
)


Create table StockFinanceInformation
(
YearID int,
QuarterID int,
StockID nvarchar(4),
StockName nvarchar(100),
Revenue money,
GrossProfit money,
OperatingIncome money,
NetValuePerShare money,
EPS money
)


Create table StockPerformanceIndicators
(
YearID int,
QuarterID int,
StockID nvarchar(4),
StockName nvarchar(100),
DividendYield money,
DividendYear int,
PE money,
PB money,
FiscalYear int,
FiscalQuarter int 
)

 