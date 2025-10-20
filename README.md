# DS 4002 Project 2

## Software and Platform
We ran the scripts using VSCode using Windows on an NVIDIA GPU. We also used the following Python packages that can be installed using pip:
- meteostat

## Documentation Map
DS4002PROJECT2
- `README.md`: This file
- `LICENSE`: Description of the license for this project
- 📁 Data Folder: contains data used throughout the pipeline
  - `METADATA.md`: Description of the data being used
  - `Crime_Data.csv`: Raw crime data from the City of Charlottesville
- 📁 Output Folder
  - `plot1_all_reviews.png`: Number of reviews per star rating
  - `plot2_avg_length.png`: Average review length by star rating
  - `plot4_length_distribution.png`: Distribution of review lengths
  - `decision_tree_results.md`: Accuracy and precision by class from `3_classify.py`
- 📁 Scripts Folder
  - `0_processing.py`: Initial processing script to generate exploratory plots
  - `1_sentiment.py`: Sentiment analysis script, taking in raw Yelp reviews and outputting the reviews with their associated sentiments
  - `2_mergechunks.py`: Utility script to combine full-dataset sentiment chunks into one dataset  
  - `3_classify.py`: Classification script, taking in reviews with associated sentiments and training/testing a decision tree based on that data

## How to Reproduce Results
You can run the project in two modes:  
### 1. Sample pipeline (fast, 250k reviews)  
This version runs quickly and produces `yelp_with_sentiment.csv`:  
- `0_processing.py`: preprocessing on sample
- `1_sentiment.py`: sentiment analysis on sample
- `3_classify.py`: classification on sample
- Note: Some scripts default to using the **full dataset** (`yelp_part*.feather` and `yelp_with_sentiment.feather`).  
For the sample pipeline, you may need to change file paths in the scripts to instead use:  
  - Input: `yelp_sample_250k.csv`  
  - Output: `yelp_with_sentiment.csv`  

### 2. Full pipeline (all reviews, split into feather parts)  
This version processes the entire dataset in chunks. 
- `0_processing.py`: preprocessing on feather parts
- `1_sentiment.py`: runs sentiment in chunks, produces sentiment_chunk_*.feather
- `2_mergechunks.py`: merges chunks into a single dataset (not committed due to size)
- `3_classify.py`: classification on full dataset