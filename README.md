# Internet Speed Logger and Visualizer

This Python script allows you to measure and track your internet speed (download and upload) over a specified duration, saving the results to a CSV file and visualizing the data with a plot.

## Features

- Measures download and upload speeds using the `speedtest-cli` library.
- Logs the speeds at regular intervals over a specified duration to a CSV file.
- Includes error handling for speed test failures, skipping failed tests.
- Visualizes the logged data using `matplotlib`, plotting the download and upload speeds over time.

## Requirements

Before running the script, make sure you have the following Python packages installed:

- `speedtest-cli`: Used to perform speed tests.
- `matplotlib`: Used to generate plots of the speed data.
  
You can install them using pip:

```bash
pip install speedtest-cli matplotlib
```

## Usage

1. **Clone the Repository:**
   
   Clone this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/internet-speed-logger.git
   ```

2. **Modify Parameters:**

   In the script, you can modify the following parameters:

   - `interval_seconds`: The interval (in seconds) between each speed test. Default is `3600` seconds (1 hour).
   - `duration_hours`: The total duration (in hours) for tracking the speed. Default is `24` hours.

   Example:
   
   ```python
   interval_seconds = 3600  # Test every hour
   duration_hours = 24      # Run the tests for 24 hours
   ```

3. **Run the Script:**

   Run the script using Python.

   ```bash
   python speedtesting.py
   ```

   The script will log download and upload speeds to a CSV file named `internet_speed_log.csv`. The time, download speed, and upload speed are recorded for each interval.

4. **Plot the Results:**

   After the speed logging completes, the script will automatically generate a plot showing the download and upload speeds over time.

## Output

- **CSV File:**
  - The CSV file `internet_speed_log.csv` will contain three columns: `Time`, `Download Speed (Mbps)`, and `Upload Speed (Mbps)`.

- **Plot:**
  - The script generates a time series plot of the recorded download and upload speeds.

## Error Handling

If a speed test fails due to network or server issues, the script will skip the failed test and proceed with the next one at the next scheduled interval. The failure will be logged in the terminal, but no data for that test will be written to the CSV file.