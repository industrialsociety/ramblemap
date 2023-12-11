## RaMBLE Data Visualization Tool

### Overview
This tool is designed for visualizing signal strength and location data from the RaMBLE database. It filters data for a specific Bluetooth device based on its MAC address and generates visual outputs in CSV, KML, and heatmap formats. The heatmap shows signal strength variations, indicating the device's location over time.

### Prerequisites
- Python 3.x
- Libraries: pandas, sqlite3, simplekml, folium

### Installation
Ensure that you have Python installed on your system. You can then install the required libraries using pip:

```bash
pip install pandas simplekml folium
```

### Usage
1. **Set Up**
   - Update `specific_mac_address` with the target device's MAC address.
   - Update `sqlite_file` with the path to your RaMBLE SQLite database file.

2. **Run the Script**
   - Execute the script in your Python environment.
   - The script will generate three files: `locations.csv`, `locations.kml`, and `heatmap.html`.

3. **Output**
   - `locations.csv`: Contains raw data of locations and signal strength.
   - `locations.kml`: Can be opened with Google Earth or similar to see locations on a map.
   - `heatmap.html`: Visual heatmap of signal strength, viewable in a web browser.

### Code Structure
1. **Data Extraction**
   - Connects to the SQLite database.
   - Executes a SQL query to fetch latitude, longitude, and RSSI values for the specified MAC address.

2. **Data Export**
   - Exports data to a CSV file for further analysis.

3. **KML Generation**
   - Creates a KML file with geographical points, which can be used in mapping software.

4. **Heatmap Generation**
   - Generates an interactive heatmap showing signal strength, with cooler colors indicating weaker signals and warmer colors for stronger signals.

### Customization
- The SQL query can be modified to change the filtering criteria or data columns.
- The heatmap parameters (like `radius`, `blur`, and `gradient`) can be adjusted for different visual effects.

### Notes
- Ensure that the SQLite database file path is correct.
- The script assumes the presence of `locations` and `devices` tables with specific schema in the RaMBLE database.
