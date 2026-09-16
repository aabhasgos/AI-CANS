import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace using regex to be robust
pattern = r"\{activeMainTab === 'dossier' && \(\s*<div className=\"h-full w-full bg-slate-900 overflow-y-auto p-6 text-slate-300\">"

new_render_logic = """{activeMainTab === 'surveillance' && (
                <LiveSurveillance />
              )}
              {activeMainTab === 'dossier' && (
                <div className="h-full w-full bg-slate-900 overflow-y-auto p-6 text-slate-300">"""

content = re.sub(pattern, new_render_logic, content, count=1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected LiveSurveillance render into CasePage.tsx.")
