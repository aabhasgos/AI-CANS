import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\case\LiveSurveillance.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the flex-1 with an explicit minimum height
old_wrapper = 'className="flex-1 rounded-lg border border-red-500/30 overflow-hidden relative z-0"'
new_wrapper = 'className="min-h-[250px] flex-1 rounded-lg border border-red-500/30 overflow-hidden relative z-0"'

content = content.replace(old_wrapper, new_wrapper)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Leaflet Map collapse issue by adding min-height.")
