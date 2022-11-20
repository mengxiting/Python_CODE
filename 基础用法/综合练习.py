name = "梦系统"
stock_price = 19.99
stock_code = "001230"
stock_price_daily_grown_factor = 1.2
grown_days = 7
stock_price2 = stock_price * stock_price_daily_grown_factor ** grown_days
print(f"公司:{name}, 股票代码：{stock_code}, 当前股价：{stock_price}")
print("每日增长系数：%.1f, 经过%d天的增长后， 股价达到了：%.2f" % (stock_price_daily_grown_factor, grown_days, stock_price2))