import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add User to the import list
old_import = "import { Search, Network, Clock, Map as MapIcon, ShieldAlert, Users, FileText, History, ZoomIn, Maximize, Activity } from 'lucide-react';"
new_import = "import { Search, Network, Clock, Map as MapIcon, ShieldAlert, Users, User, FileText, History, ZoomIn, Maximize, Activity } from 'lucide-react';"

content = content.replace(old_import, new_import)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Imported User icon from lucide-react.")
