import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <LiveSurveillance /> with <LiveSurveillance caseData={caseData} />
content = content.replace("<LiveSurveillance />", "<LiveSurveillance caseData={caseData} />")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Passed caseData to LiveSurveillance in CasePage.tsx.")
