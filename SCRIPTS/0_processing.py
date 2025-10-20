from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd
from meteostat import Point, Daily
from scipy  import stats
from pathlib import Path

# Load crime data
parent_path = Path(__file__).parent.parent
crime_df = pd.read_csv(parent_path / "DATA/Crime_Data.csv")

# Plot 1: Bar graph of offense types in Charlottesville
plt.figure(figsize=(30, 12))
offenses = crime_df.groupby("Offense").size().reset_index(name="Number of Incidents").sort_values(by="Number of Incidents", ascending=False)
sns.barplot(x="Offense", y="Number of Incidents", data=offenses)
plt.title("Offense Types of Crimes in Charlottesville")
plt.xlabel("Offense Type")
plt.ylabel("Number of Incidents")
plt.xticks(rotation=90)
plt.show()
# plt.savefig("plot1_offense_types.png")

# Retrieve weather data
# Set time period based on crime data
oldest_date = datetime.strptime(crime_df['DateReported'].min(), '%Y/%m/%d %H:%M:%S+00')
newest_date = datetime.strptime(crime_df['DateReported'].max(), '%Y/%m/%d %H:%M:%S+00')
# Get daily data
charlottesville = Point(38.03, -78.478889)
data = Daily(charlottesville, oldest_date, newest_date)
weather_data = data.fetch()

# Ensure the 'DateReported' column in crime data is in datetime format
crime_df['DateReported'] = pd.to_datetime(crime_df['DateReported'])

# Aggregate crime data by date
crime_by_date = crime_df.groupby(crime_df['DateReported'].dt.date).size().reset_index(name='Crime Count')
crime_by_date.rename(columns={'DateReported': 'Date'}, inplace=True)

# Ensure the 'time' column in weather data is in datetime format
weather_data = weather_data.reset_index()
weather_data['time'] = pd.to_datetime(weather_data['time'])

# Convert both 'Date' and 'time' columns to the same format (date only)
crime_by_date['Date'] = pd.to_datetime(crime_by_date['Date'])
weather_data['time'] = weather_data['time'].dt.date
weather_data['time'] = pd.to_datetime(weather_data['time'])

# Merge crime and weather data on the 'Date' column
merged_data = pd.merge(crime_by_date, weather_data, left_on='Date', right_on='time', how='inner')

# Plot 2: Line graph of average temperature and crime over time
plt.figure(figsize=(40, 15))
sns.lineplot(x='Date', y='Crime Count', data=merged_data, label='Crime Count', color='blue')
sns.lineplot(x='Date', y='tavg', data=merged_data, label='Average Temperature', color='red')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.title("Crime Count and Average Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Count / Temperature")
plt.legend()
plt.xticks(rotation=45)
plt.show()
# plt.savefig("plot2_temp_crime.png")