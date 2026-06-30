import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

signal_df = pd.read_csv("./brain_signal.csv")
# print(signal_df)
values_a = []
values_b = []

def calc_stats(df):
    time_mean = (df.loc[:, 'time']).mean()
    signal_mean = (df.loc[:, 'signal']).mean()
    time_max = max(df.loc[:, 'time'])
    signal_max = max(df.loc[:, 'signal'])
    time_min = min(df.loc[:, 'time'])
    signal_min = min(df.loc[:, 'signal'])
    time_std = np.std(df.loc[:,'time'])
    signal_std = np.std(df.loc[:,'signal'])
    return(f"Mean Time: {time_mean}\nSignal Mean: {signal_mean}\nMax Time: {time_max}\nMax Signal: {signal_max}\nMin Time: {time_min}\nMin Signal: {signal_min}\nTime Standard Deviation: {time_std}\nSignal Standard Deviation: {signal_std}")

def find_peaks(df, threshold):
    peaks = list((df[df.signal > threshold]).loc[:,'signal'])
    return(f"Values over {threshold}: {peaks}")

def plot_signal(df):
    df.plot()
    mpl.xlabel('x')
    mpl.ylabel('y')
    mpl.title("Brain Activity Over Time")
    mpl.show()

def moving_average(df, window):
    for i in range(window):
        values_a.append(df.iloc[i,0])
        # values_b.append(df.iloc[i,1])
    for i in range(window - (len(values_a))):
        values_a.append(df.iloc[(values_a[:-1].index + 1), 0])
        values_a.remove(values_a[0])
        print(values_a)
    

# print(calc_stats(signal_df))
# print(find_peaks(signal_df, 20))
# print(signal_df)
# plot_signal(signal_df)
moving_average(signal_df, 5)