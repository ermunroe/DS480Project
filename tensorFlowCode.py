print(X_imputed.shape[1])

train_pct = 0.8

train_size = int(X_imputed.size * train_pct)
print(train_size)


logdir = "logs/scalars/" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = keras.callbacks.TensorBoard(log_dir=logdir)

# Initialize the Neural Network
model = keras.models.Sequential([
    keras.layers.Dense(3119, input_dim=X_train_resampled.shape[1]),
    keras.layers.Dense(1500),
    keras.layers.Dense(1240),
    keras.layers.Dense(1)
])

model.compile(
    loss='mse', # keras.losses.mean_squared_error
    optimizer=keras.optimizers.SGD(learning_rate=0.05),
)

print("Training ... With default parameters, this takes less than 10 seconds.")
# Define TensorBoard callback
log_dir = "logs/fit/" + pd.Timestamp.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

training_history = model.fit(
    X_train_resampled, # input
    y_train_resampled, # output
    batch_size=train_size,
    verbose=0, # Suppress chatty output; use Tensorboard instead
    epochs=100,
    validation_data=(X_test, y_test),
    callbacks=[tensorboard_callback],
)

print("Average test loss: ", np.average(training_history.history['loss']))