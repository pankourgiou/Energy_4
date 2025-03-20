import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Function to prepare the dataset (equivalent to 'prepare_dataset.R')
def prepare_dataset(file_path):
    dset = pd.read_csv(file_path, sep=';', na_values=['?'])
    dset['Date_time'] = pd.to_datetime(dset['Date'] + ' ' + dset['Time'], format='%d/%m/%Y %H:%M:%S')
    dset = dset[(dset['Date'] == '1/2/2007') | (dset['Date'] == '2/2/2007')]
    return dset[['Date_time', 'Global_active_power', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3', 'Voltage', 'Global_reactive_power']]

# Load and prepare the dataset
dataset = prepare_dataset('household_power_consumption.txt')

# Plot 1: Histogram for Global Active Power
plt.figure(figsize=(10,6))
plt.hist(dataset['Global_active_power'], color='orangered', edgecolor='black')
plt.xlabel('Global Active Power (kilowatts)')
plt.ylabel('Frequency')
plt.title('Global Active Power')
plt.savefig('plot1.png', bbox_inches='tight')
plt.close()

# Plot 2: Global Active Power as a function of date/time
plt.figure(figsize=(12,6))
plt.plot(dataset['Date_time'], dataset['Global_active_power'], marker='')
plt.xlabel('')
plt.ylabel('Global Active Power (kilowatts)')
plt.title('Global Active Power Over Time')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate()
plt.savefig('plot2.png', bbox_inches='tight')
plt.close()

# Plot 3: Energy sub metering variables as functions of date/time
plt.figure(figsize=(12,6))
plt.plot(dataset['Date_time'], dataset['Sub_metering_1'], label='Sub_metering_1', color='black')
plt.plot(dataset['Date_time'], dataset['Sub_metering_2'], label='Sub_metering_2', color='orangered')
plt.plot(dataset['Date_time'], dataset['Sub_metering_3'], label='Sub_metering_3', color='blue')
plt.xlabel('')
plt.ylabel('Energy sub metering')
plt.title('Energy Sub Metering Over Time')
plt.legend(loc='upper right')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate()
plt.savefig('plot3.png', bbox_inches='tight')
plt.close()

# Plot 4: Multi-plot with various power metrics over time
fig, axs = plt.subplots(2, 2, figsize=(15, 12))

axs[0, 0].plot(dataset['Date_time'], dataset['Global_active_power'])
axs[0, 0].set_title('Global Active Power')
axs[0, 0].set_ylabel('Global Active Power (kilowatts)')
axs[0, 0].tick_params(axis='x', labelrotation=45)

axs[1, 0].plot(dataset['Date_time'], dataset['Sub_metering_1'], label='Sub_metering_1', color='black')
axs[1, 0].plot(dataset['Date_time'], dataset['Sub_metering_2'], label='Sub_metering_2', color='orangered')
axs[1, 0].plot(dataset['Date_time'], dataset['Sub_metering_3'], label='Sub_metering_3', color='blue')
axs[1, 0].set_title('Energy Sub Metering')
axs[1, 0].set_ylabel('Energy sub metering')
axs[1, 0].legend(loc='upper right')
axs[1, 0].tick_params(axis='x', labelrotation=45)

axs[0, 1].plot(dataset['Date_time'], dataset['Voltage'])
axs[0, 1].set_title('Voltage')
axs[0, 1].set_ylabel('Voltage')
axs[0, 1].tick_params(axis='x', labelrotation=45)

axs[1, 1].plot(dataset['Date_time'], dataset['Global_reactive_power'])
axs[1, 1].set_title('Global Reactive Power')
