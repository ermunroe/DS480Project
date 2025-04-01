import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer



df = pd.read_csv('finalData.csv')

#Filter out data from 2014-2017 since the data is not complete for those years
df_filtered = df[(df['season_x'] > 2017)]

#Filter by the 10 drivers to include in the network
drivers_to_include = [
    "Joey_Logano", "Denny_Hamlin", "Kyle_Busch", "Martin_Truex_Jr",
    "Brad_Keselowski", "Kyle_Larson", "Ryan_Blaney", "William_Byron",
    "Christopher_Bell", "Tyler_Reddick"
]

df_filtered = df_filtered[df_filtered['driver_id'].isin(drivers_to_include)]

#print(df_filtered)

# Target Variables to include in the model
targetVariables = ['race_lap_len', 'race_track_surface', 'race_track_name', 
                   'finish_position', 'starting_position', 'driver_id', 'driver_name', 'driver_nationality', 'driver_number', 'race_laps_lead', 'points_earned', 'playoff_points_earned',
                   'race_laps_run', 'race_status', 'race_cautions', 'race_speed', 'race_lead_changes', 'race_date', 'number_of_leaders', 'race_car_count', 'race_pole_time', 'race_miles_completed', 'race_purse_completed',
                   'car', 'owner_id', 'sponsor', 'race_winner_name', 'race_winner_real_id', 'race_winner_starting_pos', 'race_winner_make', 'restrictor_plate', 'pole_winner_speed', 'race_speed', 'race_lap_len', 'number_of_caution_laps']


# Filter the DataFrame to only include the target variables
df_filtered['winner'] = df_filtered['finish_position'].apply(lambda x: 1 if x == 1 else 0)

#Filter out NTT, DFP, and MQ from 'race_pole_time' column
df_filtered['race_pole_time'] = df_filtered['race_pole_time'].replace(['NTT', 'DFP', 'MQ'], np.nan)
print(df_filtered)
df_filtered = df_filtered.dropna(subset='race_pole_time')
print(df_filtered)

# Define the X and y variables
X_target = df_filtered[targetVariables]
y = df_filtered['winner']

print(X_target.shape, y.shape)


# Categorical variables to include in the model
X_categorical = X_target[['driver_nationality', 'driver_id', 'driver_name', 'sponsor', 'owner_id', 'car', 'race_track_surface', 'race_track_name']]
encoder = OneHotEncoder(sparse_output=False)
X_categorical = encoder.fit_transform(X_categorical)

# Continuous variables to include in the model
X_continuous = X_target[['race_pole_time', 'race_speed', 'race_speed', 'pole_winner_speed', 'race_lap_len']]
scaler = StandardScaler()
X_continuous = scaler.fit_transform(X_continuous)

# Discrete variables to include in the model
X_discrete = X_target[['finish_position', 'starting_position', 'driver_number', 'race_laps_run', 'points_earned', 'playoff_points_earned', 'race_cautions', 'race_lead_changes', 'number_of_leaders', 'number_of_caution_laps', 'race_laps_lead']]
X_discrete = scaler.fit_transform(X_discrete)

# Combine the categorical, continuous, and discrete variables into a single DataFrame
X_stacked = np.concatenate((X_categorical, X_continuous, X_discrete), axis=1)
X_stacked = np.array(X_stacked)


print(X_stacked.shape, y.shape)
#df_stacked = X_stacked.dropna()
#print(df_stacked.shape, y.shape)

###
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_stacked, y, test_size=0.2, random_state=42)

# Use SMOTE to handle class imbalance in the training set
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)


# Number of Nodes to have in the network
print(X_stacked.shape[1])
#591 with these specific features

from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from tensorflow.python.keras import backend
from tensorflow.python.keras.engine import sequential
from tensorflow.python.keras.layers import Dense
from scikeras.wrappers import KerasClassifier, KerasRegressor
from sklearn.model_selection import GridSearchCV
from tensorflow.python.keras.optimizer_v2 import adam as adam_v2
from tensorflow.python.keras.losses import categorical_crossentropy

#Define the model
def create_model(learningRate = 0.01, numHiddenLayers = 1):
    model = sequential()
    model.add(Dense(64, input_dim = 478, activation = 'relu'))
    for _ in range(numHiddenLayers):
        model.add(Dense(64, activation = 'relu'))
    model.add(Dense(1, activation = 'softmax'))
    model.compile(loss = categorical_crossentropy, optimizer = adam_v2, metrics = 'accuracy')
    return model

model = KerasClassifier(build_fn = create_model, verbose=0)

paramGrid = {
    'learningRate' : [0.01, 0.05, 0.1],
    'epochs' : [50, 100, 150],
    'numHiddenLayers' : [1, 2, 3] 
}

print(X_train_resampled.shape, y_train_resampled.shape)

kf = KFold(n_splits=5, shuffle=True, random_state=42)
grid = GridSearchCV(estimator=model, param_grid=paramGrid, cv=kf)
grid_result = grid.fit(X_train_resampled, y_train_resampled)