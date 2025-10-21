from datetime import datetime
import pandas as pd
from meteostat import Point, Daily
from pathlib import Path
from scipy import stats

# Load crime data
parent_path = Path(__file__).parent.parent
crime_df = pd.read_csv(parent_path / "DATA/Crime_Data.csv")

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

corr_df = merged_data[['Crime Count', 'tavg']].dropna()
r, p_two_sided = stats.pearsonr(corr_df['tavg'], corr_df['Crime Count'])
p_one_sided = p_two_sided / 2 if r > 0 else 1.0

print(f"[TOTAL] Pearson r = {r:.3f}")
print(f"[TOTAL] Two-sdied p-value = {p_two_sided:.4g}")
print(f"[TOTAL] One-sided p (H1: r > 0) = {p_one_sided:.4g}")

crime_df['DateReported'] = pd.to_datetime(crime_df['DateReported'], errors='coerce')
daily_counts = (
    crime_df
    .assign(Date=crime_df['DateReported'].dt.date)
    .groupby(['Date', 'Offense'])
    .size()
    .unstack(fill_value=0)
    .reset_index()
)
daily_counts['Date'] = pd.to_datetime(daily_counts['Date'])

total_offense_counts = crime_df['Offense'].value_counts()
top12 = total_offense_counts.head(12).index
daily_top12 = daily_counts[['Date'] + list(top12)].copy()

wx_cols = weather_data[['time', 'tavg']].rename(columns={'time': 'Date'})
wx_cols['Date'] = pd.to_datetime(wx_cols['Date'])
merged_top12 = pd.merge(daily_top12, wx_cols, on='Date', how='inner').dropna(subset = ['tavg'])

rows = []
for offense in top12:
  x = merged_top12['tavg']
  y = merged_top12[offense]
  if y.nunique() < 2:
    rows.append((offense, np.nan, np.nan))
    continue
  r_off, p2 = stats.pearsonr(x,y)
  p1 = p2 / 2 if r_off > 0 else 1.0
  rows.append((offense, r_off, p1))

offense_corr = pd.DataFrame(rows, columns=['Offense', 'Pearson_r', 'OneSided_p'])
offense_corr = offense_corr.sort_values(by='Pearson_r', ascending=False)
print("\n[TOP 12 OFFENSES] Pearson correlation with temperature (one-sided p for r>0):")
print(offense_corr.to_string(index=False))