import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\IngestionPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix missing import by changing useEffect to React.useEffect
if "useEffect(() => {" in content:
    content = content.replace("useEffect(() => {", "React.useEffect(() => {")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed useEffect reference.")
