import pandas as pd
import sqlite3
import simplekml
import folium
from folium.plugins import HeatMap

# Specify the MAC address of the device you want to filter
specific_mac_address = 'your_mac_address_here'

# 1. Import SQLite file
sqlite_file = "/path/to/your/RaMBLE_playstore_v40.15_xxxxxx.sqlite"
conn = sqlite3.connect(sqlite_file)

# 2. Extract data for the specific device
query = f"""
SELECT l.latitude, l.longitude, l.rssi 
FROM locations l
INNER JOIN devices d ON l.device_id = d.id
WHERE d.address = '{specific_mac_address}'
"""
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# 3. Generate CSV
df.to_csv('locations.csv', index=False)  # Saving data as CSV

# 4. Generate KML
kml = simplekml.Kml()
for index, row in df.iterrows():
    kml.newpoint(name=f"Point {index}", coords=[(row['longitude'], row['latitude'])])
kml.save("locations.kml")  # Saving data as KML

# 5. Generate Heatmap
map_center = [df['latitude'].mean(), df['longitude'].mean()] if not df.empty else [0, 0]
map = folium.Map(location=map_center, zoom_start=18, max_zoom=50)

# Using 'rssi' column as intensity for heatmap
heatmap_data = df[['latitude', 'longitude', 'rssi']].values.tolist() if not df.empty else []

# Define the gradient for heatmap colors
# Lower rssi values will be blue, higher values will be red
gradient = {
    0.2: 'blue',
    0.4: 'cyan',
    0.6: 'lime',
    0.8: 'yellow',
    1.0: 'red'
}

# Create and add a heatmap layer with custom parameters
heatmap = HeatMap(
    heatmap_data, 
    radius=8,  
    blur=3,    
    max_zoom=50,
    min_opacity=0.5,
    gradient=gradient
)
map.add_child(heatmap)

# Save the map as an HTML file
map.save('heatmap.html')

print("CSV, KML, and heatmap have been generated.")
