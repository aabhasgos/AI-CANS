import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\map\LocationMap.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

if "leaflet/dist/leaflet.css" not in content:
    content = "import 'leaflet/dist/leaflet.css';\n" + content

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Map CSS added.")
