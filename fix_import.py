import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add Camera to the lucide-react import
pattern = r"import \{ (.*?) \} from 'lucide-react';"
replacement = r"import { \1, Camera } from 'lucide-react';"

content = re.sub(pattern, replacement, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Imported Camera from lucide-react")
