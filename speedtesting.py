#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instead of using web-based applications for testing internet speed, 
a code-based application would enable more robust tracking and logging. 
This script will monitor upload and download speeds, over a specified 
time (e.g., 1 hr) and at a specified freqency (e.g., 10 seconds between
each check). Data logged to file but also plotted at the end of the run.

@author: keshrao
"""

import speedtest
import time
import csv
import matplotlib.pyplot as plt

def test_internet_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        # Measure download and upload speeds
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps

        return download_speed, upload_speed

    except Exception as e:
        print(f"Speed test failed: {e}")
        return None, None

def log_speed_to_csv(file_name, interval_seconds, duration_hours):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Download Speed (Mbps)", "Upload Speed (Mbps)"])

        start_time = time.time()
        end_time = start_time + duration_hours * 3600

        while time.time() < end_time:
            download_speed, upload_speed = test_internet_speed()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            if download_speed is not None and upload_speed is not None:
                writer.writerow([current_time, download_speed, upload_speed])
                print(f"Logged at {current_time}: {download_speed:.2f} Mbps down, {upload_speed:.2f} Mbps up")
            else:
                print(f"Speed test failed at {current_time}, skipping this iteration.")

            time.sleep(interval_seconds)

def plot_speeds(file_name):
    times = []
    download_speeds = []
    upload_speeds = []

    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            times.append(row["Time"])
            download_speeds.append(float(row["Download Speed (Mbps)"]))
            upload_speeds.append(float(row["Upload Speed (Mbps)"]))

    plt.figure(figsize=(10, 6))
    plt.plot(times, download_speeds, label="Download Speed (Mbps)", color="blue", marker="o")
    plt.plot(times, upload_speeds, label="Upload Speed (Mbps)", color="red", marker="o")
    plt.xlabel("Time")
    plt.ylabel("Speed (Mbps)")
    plt.title("Internet Speed Over Time")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Define parameters
    file_name = "internet_speed_log.csv"
    interval_seconds = 10  # Wait time
    duration_hours = 1  # Track for XX hours
    isPlot = False

    # Log the speeds
    log_speed_to_csv(file_name, interval_seconds, duration_hours)

    if isPlot:
        # Plot the results
        plot_speeds(file_name)

