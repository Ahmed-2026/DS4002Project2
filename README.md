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
- 📁 DATA Folder: contains data used throughout the pipeline
  - `METADATA.md`: Description of the data being used
  - `Crime_Data.csv`: Raw crime data from the City of Charlottesville
- 📁 OUTPUT Folder
  - `plot1_offense_types.png`: Bar chart of number of incidents of each type of offense
  - `plot2_temp_crime.png`: Line plot of average temperature and number of crimes per day
  - `plot3_temp_correlation.png`: Bar chart of Pearson correlation between temperature and daily count for top 12 offenses
  - `offense_correlation_table.csv`: CSV file of Pearson correlation results for each offense type
  - `pearson_total_result.txt`: Text file of Pearson correlation result for overall daily crime vs. temperature
  - `summary_results.txt`: Text file summarizing key findings from the analysis
  - `results.md`: Formatted Markdown file summarizing and interpreting the results of the analysis
- 📁 SCRIPTS Folder
  - `0_processing.py`: Initial processing script to generate exploratory plots
  - `1_correlation.py`: Correlation analysis script

## How to Reproduce Results
You can run the project in two steps:  
- `0_processing.py`: preprocessing and preliminary visualization of data
- `1_correlation.py`: calculates Pearson correlation of crime and average temperature
