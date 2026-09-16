import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\case\LiveSurveillance.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Lock the Map interaction so the user can't drag it out from under the red ping
old_map = 'scrollWheelZoom={false} className="map-dark-mode" style={{ height: \'100%\', width: \'100%\', background: \'#0f172a\' }}>'
new_map = 'scrollWheelZoom={false} dragging={false} zoomControl={false} doubleClickZoom={false} touchZoom={false} className="map-dark-mode" style={{ height: \'100%\', width: \'100%\', background: \'#0f172a\' }}>'

content = content.replace(old_map, new_map)

# 2. Fix the scroll layout by making the root container explicitly absolute so it doesn't get clipped by its parent's flex rules
old_root = 'className="h-full w-full bg-slate-900 overflow-y-auto flex flex-col p-6"'
new_root = 'className="absolute inset-0 bg-slate-900 overflow-y-auto flex flex-col p-6"'

content = content.replace(old_root, new_root)

# 3. Increase padding at the bottom so they can scroll fully past the map
old_grid = 'className="flex-1 grid grid-cols-1 md:grid-cols-2 gap-6 h-full pb-10"'
new_grid = 'className="flex-none grid grid-cols-1 md:grid-cols-2 gap-6 pb-32"'

content = content.replace(old_grid, new_grid)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Map Dragging and Scrolling.")
