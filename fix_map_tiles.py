import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\map\LocationMap.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_tile = """<TileLayer
          url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OSM</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
        />"""

new_tile = """<TileLayer
          url="https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}"
          attribution='Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ'
        />"""

content = content.replace(old_tile, new_tile)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Map tile layer swapped to ESRI Dark Gray.")
