import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\AnalyticsPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Change the dataKey mapping to a friendly name for the tooltip
content = content.replace("dataKey=\"degree\"", "dataKey=\"degree\" name=\"Total Connections\"")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Tooltip fixed.")
