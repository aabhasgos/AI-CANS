import os

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("<Users className=\"w-4 h-4\" /> Entities", "<Users className=\"w-4 h-4\" /> Key Suspects")
content = content.replace("<ShieldAlert className=\"w-4 h-4\" /> Alerts", "<ShieldAlert className=\"w-4 h-4\" /> AI Warnings")
content = content.replace("<Network className=\"w-4 h-4\" /> Clusters", "<Network className=\"w-4 h-4\" /> Syndicates")
content = content.replace("Key Entities (By Centrality)", "Top Suspects & Targets (AI Ranked)")
content = content.replace("AI Link Explanation", "🤖 AI Explanation (Why are they connected?)")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Side tabs simplified.")
