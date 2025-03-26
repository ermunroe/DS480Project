import pandas as pd
import numpy as np

#2014
# Load the data
Results2014 = pd.read_csv('2014_race_results.csv')
Schedule2014 = pd.read_csv('2014_schedule.csv')

#Merge the data
merged2014 = pd.merge(Results2014, Schedule2014, on='race_id_short', how='inner')

merged2014.to_csv('2014_merged.csv', index=False)

#2015
#Load the data
Results2015 = pd.read_csv('2015_race_results.csv')
Schedule2015 = pd.read_csv('2015_schedule.csv')

#Merge the data
merged2015 = pd.merge(Results2015, Schedule2015, on= 'race_id_short', how='inner')

merged2015.to_csv('2015_merged.csv', index=False)

#2016
#Load the data
Results2016 = pd.read_csv('2016_race_results.csv')
Schedule2016 = pd.read_csv('2016_schedule.csv')

#merge the data
merged2016 = pd.merge(Results2016, Schedule2016, on='race_id_short', how='inner')

merged2016.to_csv('2016_merged.csv', index=False)

#2017
#Load the data
Results2017 = pd.read_csv('2017_race_results.csv')
Schedule2017 = pd.read_csv('2017_schedule.csv')

#merge the data
merged2017 = pd.merge(Results2017, Schedule2017, on='race_id_short', how='inner')

merged2017.to_csv('2017_merged.csv', index=False)


#This is where we start to have 3 files we need to merge for each year of data.

#2018
#Load the data

##Missing 30, 24, 25, 19, 16, 17, 7, 4####

Results2018 = pd.read_csv('2018_race_results.csv')
Schedule2018 = pd.read_csv('2018_schedule.csv')
Info2018 = pd.read_csv('2018_race_info.csv')

Info2018['track_name'] = Info2018['track_name'].str.replace(' ', '_')

#Filter out the series_id's that are not 1
Info2018Filtered = Info2018[Info2018['series_id'] != 2]
Info2018Filtered = Info2018Filtered[Info2018Filtered['series_id'] != 3]

#Drop the first 3 rows of the data
Info2018Filtered = Info2018Filtered.drop(index=0)
Info2018Filtered = Info2018Filtered.drop(index=1)
Info2018Filtered = Info2018Filtered.drop(index=2)

#Create a new variable in Info2018Filtered that is the YEAR_RACE_NAME in all caps
Info2018Filtered['race_id'] = Info2018Filtered['race_season'].astype(str) + '_' + Info2018Filtered['race_name'].str.replace(' ', '_').str.upper()

#Change Results 'race_id' to all caps
Results2018['race_id'] = Results2018['race_id'].str.upper()

#Merge the data
merged2018 = pd.merge(Results2018, Schedule2018, on='race_id_short', how='inner')
final2018 = merged2018.merge(Info2018Filtered, on= 'race_id' , how ="inner")

final2018.to_csv('2018_merged.csv', index=False)




# 2019

### Missing 4, 7, 16, 19, 21, 24, 25, 26###

# Load the data
Results2019 = pd.read_csv('2019_race_results.csv')
Schedule2019 = pd.read_csv('2019_schedule.csv')
Info2019 = pd.read_csv('2019_race_info.csv')

Info2019['track_name'] = Info2019['track_name'].str.replace(' ', '_')

# Filter out the series_id's that are not 1
Info2019Filtered = Info2019[Info2019['series_id'] != 2]
Info2019Filtered = Info2019Filtered[Info2019Filtered['series_id'] != 3]

# Drop the first 3 rows of the data
Info2019Filtered = Info2019Filtered.drop(index=0)
Info2019Filtered = Info2019Filtered.drop(index=1)
Info2019Filtered = Info2019Filtered.drop(index=2)

# Create a new variable in Info2019Filtered that is the YEAR_RACE_NAME in all caps
Info2019Filtered['race_id'] = Info2019Filtered['race_season'].astype(str) + '_' + Info2019Filtered['race_name'].str.replace(' ', '_').str.upper()

# Change Results 'race_id' to all caps
Results2019['race_id'] = Results2019['race_id'].str.upper()

# Merge the data
merged2019 = pd.merge(Results2019, Schedule2019, on='race_id_short', how='inner')
final2019 = merged2019.merge(Info2019Filtered, on='race_id', how="inner")

final2019.to_csv('2019_merged.csv', index=False)




# 2020

### Missing 4, 11, 14, 16, 18, 19, 23, 24, 25, 


# Load the data
Results2020 = pd.read_csv('2020_race_results.csv')
Schedule2020 = pd.read_csv('2020_schedule.csv')
Info2020 = pd.read_csv('2020_race_info.csv')

Info2020['track_name'] = Info2020['track_name'].str.replace(' ', '_')

# Filter out the series_id's that are not 1
Info2020Filtered = Info2020[Info2020['series_id'] != 2]
Info2020Filtered = Info2020Filtered[Info2020Filtered['series_id'] != 3]

# Drop the first 3 rows of the data
Info2020Filtered = Info2020Filtered.drop(index=0)
Info2020Filtered = Info2020Filtered.drop(index=1)
Info2020Filtered = Info2020Filtered.drop(index=2)

# Create a new variable in Info2020Filtered that is the YEAR_RACE_NAME in all caps
Info2020Filtered['race_id'] = Info2020Filtered['race_season'].astype(str) + '_' + Info2020Filtered['race_name'].str.replace(' ', '_').str.upper()

# Change Results 'race_id' to all caps
Results2020['race_id'] = Results2020['race_id'].str.upper()

# Merge the data
merged2020 = pd.merge(Results2020, Schedule2020, on='race_id_short', how='inner')
final2020 = merged2020.merge(Info2020Filtered, on='race_id', how="inner")

final2020.to_csv('2020_merged.csv', index=False)

# 2021

### Missing 24, 28, 29, 33, 36 ###

# Load the data
Results2021 = pd.read_csv('2021_race_results.csv')
Schedule2021 = pd.read_csv('2021_schedule.csv')
Info2021 = pd.read_csv('2021_race_info.csv')

Info2021['track_name'] = Info2021['track_name'].str.replace(' ', '_')

# Filter out the series_id's that are not 1
Info2021Filtered = Info2021[Info2021['series_id'] != 2]
Info2021Filtered = Info2021Filtered[Info2021Filtered['series_id'] != 3]

# Drop the first 3 rows of the data
Info2021Filtered = Info2021Filtered.drop(index=0)
Info2021Filtered = Info2021Filtered.drop(index=1)
Info2021Filtered = Info2021Filtered.drop(index=2)

# Create a new variable in Info2021Filtered that is the YEAR_RACE_NAME in all caps
Info2021Filtered['race_id'] = Info2021Filtered['race_season'].astype(str) + '_' + Info2021Filtered['race_name'].str.replace(' ', '_').str.upper()

# Change Results 'race_id' to all caps
Results2021['race_id'] = Results2021['race_id'].str.upper()

# Merge the data
merged2021 = pd.merge(Results2021, Schedule2021, on='race_id_short', how='inner')
final2021 = merged2021.merge(Info2021Filtered, on='race_id', how="inner")

final2021.to_csv('2021_merged.csv', index=False)

# 2022

## Missing 3, 6, 8, 11, 13, 15, 16, 18, 21, 28, 29, 30, 36 ##

# Load the data
Results2022 = pd.read_csv('2022_race_results.csv')
Schedule2022 = pd.read_csv('2022_schedule.csv')
Info2022 = pd.read_csv('2022_race_info.csv')

Info2022['track_name'] = Info2022['track_name'].str.replace(' ', '_')

# Filter out the series_id's that are not 1
Info2022Filtered = Info2022[Info2022['series_id'] != 2]
Info2022Filtered = Info2022Filtered[Info2022Filtered['series_id'] != 3]

# Drop the first 3 rows of the data
Info2022Filtered = Info2022Filtered.drop(index=0)
Info2022Filtered = Info2022Filtered.drop(index=1)
Info2022Filtered = Info2022Filtered.drop(index=2)

# Create a new variable in Info2022Filtered that is the YEAR_RACE_NAME in all caps
Info2022Filtered['race_id'] = Info2022Filtered['race_season'].astype(str) + '_' + Info2022Filtered['race_name'].str.replace(' ', '_').str.upper()

# Change Results 'race_id' to all caps
Results2022['race_id'] = Results2022['race_id'].str.upper()

# Merge the data
merged2022 = pd.merge(Results2022, Schedule2022, on='race_id_short', how='inner')
final2022 = merged2022.merge(Info2022Filtered, on='race_id', how="inner")

final2022.to_csv('2022_merged.csv', index=False)

# 2023

## Missing 3, 11, 12, 15, 16, 21, 30, 34, 36 ##

# Load the data
Results2023 = pd.read_csv('2023_race_results.csv')
Schedule2023 = pd.read_csv('2023_schedule.csv')
Info2023 = pd.read_csv('2023_race_info.csv')

Info2023['track_name'] = Info2023['track_name'].str.replace(' ', '_')

# Filter out the series_id's that are not 1
Info2023Filtered = Info2023[Info2023['series_id'] != 2]
Info2023Filtered = Info2023Filtered[Info2023Filtered['series_id'] != 3]

# Drop the first 3 rows of the data
Info2023Filtered = Info2023Filtered.drop(index=0)
Info2023Filtered = Info2023Filtered.drop(index=1)
Info2023Filtered = Info2023Filtered.drop(index=2)

# Create a new variable in Info2023Filtered that is the YEAR_RACE_NAME in all caps
Info2023Filtered['race_id'] = Info2023Filtered['race_season'].astype(str) + '_' + Info2023Filtered['race_name'].str.replace(' ', '_').str.upper()

# Change Results 'race_id' to all caps
Results2023['race_id'] = Results2023['race_id'].str.upper()

# Merge the data
merged2023 = pd.merge(Results2023, Schedule2023, on='race_id_short', how='inner')
final2023 = merged2023.merge(Info2023Filtered, on='race_id', how="inner")

final2023.to_csv('2023_merged.csv', index=False)

# 2024

## Missing 4, 8, 11, 12, 15, 16, 21, 22, 36##
## Make sure CookOut400 Richmond, and Darlington are seperated#

# Load the data
Results2024 = pd.read_csv('2024_race_results.csv')
Schedule2024 = pd.read_csv('2024_schedule.csv')
Info2024 = pd.read_csv('2024_race_info.csv')

Info2024['track_name'] = Info2024['track_name'].str.replace(' ', '_')

# Filter out the series_id's that are not 1
Info2024Filtered = Info2024[Info2024['series_id'] != 2]
Info2024Filtered = Info2024Filtered[Info2024Filtered['series_id'] != 3]

# Drop the first 3 rows of the data
Info2024Filtered = Info2024Filtered.drop(index=0)
Info2024Filtered = Info2024Filtered.drop(index=1)
Info2024Filtered = Info2024Filtered.drop(index=2)

# Create a new variable in Info2024Filtered that is the YEAR_RACE_NAME in all caps
Info2024Filtered['race_id'] = Info2024Filtered['race_season'].astype(str) + '_' + Info2024Filtered['race_name'].str.replace(' ', '_').str.upper()

# Change Results 'race_id' to all caps
Results2024['race_id'] = Results2024['race_id'].str.upper()

# Merge the data
merged2024 = pd.merge(Results2024, Schedule2024, on='race_id_short', how='inner')
final2024 = merged2024.merge(Info2024Filtered, on='race_id', how="inner")

final2024.to_csv('2024_merged.csv', index=False)