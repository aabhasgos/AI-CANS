import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\AnalyticsPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Make the buttons actually do something (alert or navigate)
content = content.replace(
    "<button className=\"px-3 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-sm transition-colors\">Review Match</button>",
    "<button onClick={() => window.location.href='/cases/1'} className=\"px-3 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-sm transition-colors\">Review Match</button>"
)

content = content.replace(
    "<button className=\"px-3 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-sm transition-colors\">View Pattern</button>",
    "<button onClick={() => window.location.href='/cases/2'} className=\"px-3 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-sm transition-colors\">View Pattern</button>"
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Analytics buttons wired.")
