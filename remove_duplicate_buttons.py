import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for the View Full Intelligence Profile button
pattern_profile = r'<button className="w-full mt-4 bg-slate-800 hover:bg-slate-700 border border-slate-600 text-slate-200 text-xs py-1\.5 rounded transition-colors">\s*View Full Intelligence Profile\s*</button>'

# Pattern for the Request CDR Subpoena button
pattern_subpoena = r'<button className="w-full mt-4 bg-slate-800 hover:bg-slate-700 border border-slate-600 text-slate-200 text-xs py-1\.5 rounded transition-colors">\s*Request CDR Subpoena\s*</button>'

content = re.sub(pattern_profile, '', content)
content = re.sub(pattern_subpoena, '', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed duplicate broken buttons from side panel.")
