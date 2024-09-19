import pandas as pd
import matplotlib.pyplot as plt
# We read in a stock data data file into a data frame and see what it looks like
df = pd.read_csv(r'C:\Users\HP\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\rough\google.csv')

# We load the Google stock data into a DataFrame
google_stock = pd.read_csv('google.csv', index_col = ['Date'],  parse_dates = True, usecols = ['Date', 'Adj Close'])

# We load the Apple stock data into a DataFrame
apple_stock = pd.read_csv('aapl.csv',  index_col = ['Date'],  parse_dates = True, usecols = ['Date', 'Adj Close'])
                       
# We load the Amazon stock data into a DataFrame
amazon_stock = pd.read_csv('amzn.csv', index_col = ['Date'],  parse_dates = True, usecols = ['Date', 'Adj Close'])


# We create calendar dates between '2000-01-01' and  '2016-12-31'
dates = pd.date_range('2000-01-01', '2016-12-31')

# We create and empty DataFrame that uses the above dates as indices
all_stocks = pd.DataFrame(index = dates)

# Change the Adj Close column label to Google
google_stock = google_stock.rename(columns = {'Adj Close' : 'Google'})

# Change the Adj Close column label to Apple
apple_stock = apple_stock.rename(columns = {'Adj Close' : 'Apple'})

# Change the Adj Close column label to Amazon
amazon_stock = amazon_stock.rename(columns = {'Adj Close' : 'Amazon'})


# We join the Google stock to all_stocks
all_stocks = all_stocks.join(google_stock)

# We join the Apple stock to all_stocks
all_stocks = all_stocks.join(apple_stock)

# We join the Amazon stock to all_stocks
all_stocks = all_stocks.join(amazon_stock)


# Remove any rows that contain NaN values. Do this operation inplace. 
all_stocks.dropna(axis=0, inplace = True)

# Print the average stock price for each stock
print('The average stock price for each stock is: \n', all_stocks.mean(), '\n')
# Note: You can get the same result by printing it individually one-by-one as `all_stocks['Google'].mean()`

# Print the median stock price for each stock
print('The median stock price for each stock is: \n', all_stocks.median(), '\n')

# Print the standard deviation of the stock price for each stock  
print('The standard deviation of the stock price for each stock  is: \n', all_stocks.std(), '\n')

# Print the correlation between stocks
print('The correlation between stocks is: \n', all_stocks.corr(), '\n')

# We compute the rolling mean using a 150-Day window for Google stock
rollingMean = all_stocks['Google'].rolling(150).mean()

# We plot the Google stock data
plt.plot(all_stocks['Google'])

# We plot the rolling mean ontop of our Google stock data
plt.plot(rollingMean)
plt.legend(['Google Stock Price', 'Rolling Mean'])
plt.show() # type: ignore