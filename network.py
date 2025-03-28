import pandas as pd
import numpy as np


df = pd.read_csv('finalData.csv')

# Target Variables to include in the model
targetVariables = ['race_lap_len', 'race_track_surface', 'race_track_name', 'race_track_name', 
                   'finish_position', 'starting_position', 'driver_id', 'driver_name', 'driver_nationality', 'driver_number', 'race_laps_lead', 'points_earned', 'playoff_points_earned',
                   'race_laps_run', 'race_status', 'race_cautions', 'race_speed', 'race_lead_changes', 'race_date', 'race_car_count', 'race_pole_time', 'race_miles_completed', 'race_purse_completed',
                   'car', 'owner_id', 'sponsor', 'race_winner_name', 'race_winner_real_id', 'race_winner_starting_pos', 'race_winner_make']


# Filter the DataFrame to only include the target variables
df['winner'] = df['finish_position'].apply(lambda x: 1 if x == 1 else 0)


# Define the X and y variables
X = df[targetVariables]
y = df['winner']


