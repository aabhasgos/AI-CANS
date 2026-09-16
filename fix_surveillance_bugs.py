import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\case\LiveSurveillance.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Change overflow-hidden to overflow-y-auto
content = content.replace(
    'className="h-full w-full bg-slate-900 overflow-hidden flex flex-col p-6"',
    'className="h-full w-full bg-slate-900 overflow-y-auto flex flex-col p-6"'
)

# Fix 2: Change TileLayer to use standard OSM with invert filter to guarantee no API key warnings
old_tile = """<TileLayer
                      url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
                      attribution='&copy; <a href="https://carto.com/">CARTO</a>'
                    />"""

new_tile = """<TileLayer
                      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                      attribution='&copy; OpenStreetMap contributors'
                      className="map-tiles"
                    />"""

content = content.replace(old_tile, new_tile)

# Fix 3: Inject the CSS filter into the existing style block
old_style = """<style dangerouslySetInnerHTML={{__html: `
        @keyframes scan {"""

new_style = """<style dangerouslySetInnerHTML={{__html: `
        .map-tiles { filter: brightness(0.6) invert(1) contrast(3) hue-rotate(200deg) saturate(0.3) brightness(0.7); }
        @keyframes scan {"""

content = content.replace(old_style, new_style)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Overflow and Map API Key watermark issue.")
