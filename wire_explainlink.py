import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\graph\ExplainLink.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Make Source List item clickable
content = content.replace(
    "className=\"flex items-center justify-between p-3 bg-slate-800 rounded-lg border border-slate-700 hover:border-slate-500 cursor-pointer transition-colors\"",
    "onClick={() => alert(`Accessing secure source document: ${src.name}`)} className=\"flex items-center justify-between p-3 bg-slate-800 rounded-lg border border-slate-700 hover:border-slate-500 cursor-pointer transition-colors\""
)

# Make Evidence 'View Record' button clickable
content = content.replace(
    "<button className=\"text-blue-400 hover:text-blue-300 text-xs font-semibold\">View Record</button>",
    "<button onClick={() => alert(`Fetching classified record details for ${rec.type}...`)} className=\"text-blue-400 hover:text-blue-300 text-xs font-semibold\">View Record</button>"
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("ExplainLink buttons wired.")
