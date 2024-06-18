import pandas as pd
import matplotlib.pyplot as plt


weather_data = pd.read_csv(r"C:\Users\dabhu\Downloads\weather.csv")

weather_data['Date'] = pd.to_datetime(weather_data['Date'])

weather_data['Month'] = weather_data['Date'].dt.month
weather_data['Year'] = weather_data['Date'].dt.year

def get_season(month):
    if month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Autumn'
    else:
        return 'Winter'

weather_data['Season'] = weather_data['Month'].apply(get_season)

average_temp_season = weather_data.groupby(['Year', 'Season'])['Temperature'].mean().unstack()

average_temp_season.plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Average Temperature Trends Over Different Seasons')
plt.xlabel('Year')
plt.ylabel('Average Temperature (°C)')
plt.xticks(average_temp_season.index)
plt.grid(True)
plt.legend(title='Season')
plt.show()
plt.figure(figsize=(10, 6))
plt.plot(weather_data['Date'], weather_data['Precipitation'], color='blue')
plt.title('Precipitation Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(weather_data['Temperature'], bins=20, color='orange', edgecolor='black')
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)

extreme_cold_threshold = -10
plt.axvline(x=extreme_cold_threshold, color='red', linestyle='--', label=f'Extreme Cold ({extreme_cold_threshold}°C)')
plt.legend()
plt.show()
