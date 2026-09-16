import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\case\LiveSurveillance.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add scrollWheelZoom={false} and a custom class to the MapContainer
old_map = "<MapContainer center={coords as [number, number]} zoom={13} style={{ height: '100%', width: '100%', background: '#0f172a' }}>"
new_map = "<MapContainer center={coords as [number, number]} zoom={13} scrollWheelZoom={false} className=\"map-dark-mode\" style={{ height: '100%', width: '100%', background: '#0f172a' }}>"
content = content.replace(old_map, new_map)

# 2. Fix the CSS filter so it actually targets the Leaflet tiles correctly
old_style = ".map-tiles { filter: brightness(0.6) invert(1) contrast(3) hue-rotate(200deg) saturate(0.3) brightness(0.7); }"
new_style = ".map-dark-mode .leaflet-tile-pane { filter: invert(100%) hue-rotate(180deg) brightness(95%) contrast(90%); }"
content = content.replace(old_style, new_style)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Leaflet scrolling and Dark Mode CSS.")
