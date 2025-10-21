# DS 4002 Project 2

## Software and Platform
We ran the scripts using VSCode using Windows on an NVIDIA GPU. We also used the following Python packages that can be installed using pip:
- datetime
- matplotlib
- meteostat
- pandas
- pathlib
- scipy
- seaborn

## Documentation Map
DS4002PROJECT2
- `README.md`: This file
- `LICENSE`: Description of the license for this project
- 📁 Data Folder: contains data used throughout the pipeline
  - `METADATA.md`: Description of the data being used
  - `Crime_Data.csv`: Raw crime data from the City of Charlottesville
- 📁 Output Folder
  - `plot1_offense_types.png`: Bar chart of number of incidents of each type of offense
  - `plot2_temp_crime.png`: Line plot of average temperature and number of crimes per day
  - `plot3_temp_correlation.png`: Bar chart of Pearson correlation between temperature and daily count for top 12 offenses
- 📁 Scripts Folder
  - `0_processing.py`: Initial processing script to generate exploratory plots
  - `1_correlation.py`: Correlation analysis script

## Results Interpretation
- r (Pearson correlation) measures the strenght and direction of a linear relationship between temperature and crime
  - r > 0 → as temperature increases, crime tends to increase
  - r < 0 → as temperature increases, crime tends to decrease
  - |r| close to 1 → strong relationship; |r| close to 0 → weak relationship
- p-value shows whether that relationship is statistically significant
  - p < 0.05 → statistically significant relationship (unlikely due to chance)
 
## Summary of Findings:
- Total daily crime vs. temperature: r = 0.182, p < 0.001 → weak but statistically significant positive relationship
- Top correlation offenses:
  - Motor Vehicle Theft (r = 0.112)
  - Vandalism (r = 0.098)
  - Simple Assault (r = 0.079)
- Other offenses such as Burglary and Suspicious Activity showed little to no correlation
Overall, warmer days correspond to slightly higher crime counts, but the effect is modest and below our hypothesized threshold (r ≥ 0.5). Temperature alone is therefore not a strong predictor of daily crime in Charlottesville.

## How to Reproduce Results
You can run the project in two modes:  
- `0_processing.py`: preprocessing and preliminary visualization of data
- `1_correlation.py`: calculates Pearson correlation of crime and average temperature
