import numpy as np

np.random.seed(42)

# Simulated EEG data (electrodes × time)
eeg = np.random.normal(0, 20, (32, 5000))

# Inject some noisy electrodes
eeg[4] += 80
eeg[17] -= 60

# Part 1 - Basic Statistics
mean_signal = np.mean(eeg, axis=1)
# print(mean_signal)
std_signal = np.std(eeg, axis=1)
# print(std_signal)
min_recorded = [np.min(eeg[i]) for i in range(len(eeg))]
# print(min_recorded)
max_recorded = [np.max(eeg[i] for i in range(len(eeg)))]
# print(max_recorded)


# Part 2 - Find Noisy Electrodes
noisy_electrodes = []
for i in range(len(eeg)):
    if std_signal[i] > 25:
        noisy_electrodes.append(i)

print(noisy_electrodes)
print(len(noisy_electrodes))


# Part 3 - Normalize
# eeg[4] = ((eeg[4] - mean_signal[4])/std_signal[4])
# print(np.mean(eeg[4]))
# print(np.std(eeg[4]))
normalized_values = (eeg - mean_signal[:, None])/std_signal[:, None]


z_mean_signal = np.mean(normalized_values, axis=1)
print(abs(np.round(z_mean_signal)))
z_std_signal = np.std(normalized_values, axis=1)
print(np.round(z_std_signal))

# assert z_mean_signal.round()[:, None] == 0
# assert z_std_signal.round()[:, None] == 1

# Part 4 - Remove Outliers
nanned_norm_eeg = normalized_values.copy()
nanned_norm_eeg[abs(normalized_values) > 3] = np.nan
print(nanned_norm_eeg)