filepath = r'c:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\timeline\InvestigationTimeline.tsx'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Specifically fix line 63 which has an escaped backtick before the template literal
content = content.replace("active ? \\`${config.bg}", "active ? `${config.bg}")
content = content.replace("${config.border}\\` :", "${config.border}` :")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
