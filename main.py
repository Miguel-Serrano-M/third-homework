from matplotlib import pylab as plt
import pandas as pd


df1 = pd.read_csv("spotify.csv")
print(df1.head())
df1['Date'] = pd.to_datetime(df1.Date)


df2 = pd.read_csv("netflix.csv")
print(df2)
df2['Date'] = pd.to_datetime(df2.Date)

index2 = []
for date2 in df2.Date:
    if df1.index[df1.Date == date2].values.size:
        index2.append(int(df1.index[df1.Date == date2].values[0]))
print(index2)



mean = df1["Close"].mean()
mean2 = df2["Close"].mean()



plt.figure("Spotify and Netflix")
plt.plot(df1["Date"], df1["Close"], 'c-', linewidth=1.5, label="Spotify Stock price, mean="+str(mean), data=df1)
plt.plot(df2["Date"], df2["Close"], 'm-', linewidth=1.5, label="Netflix Stock price, mean="+str(mean2), data=df2)
plt.xlabel("Date")
plt.legend(loc="upper right")
plt.show()



