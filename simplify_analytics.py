import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\AnalyticsPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Page Title & Subtitle
content = content.replace("National Intelligence Analytics Dashboard", "State Police Intelligence Overview")
content = content.replace("Cross-case intelligence and macro network metrics.", "AI summary of criminal syndicates, repeat offenders, and gang structures across all FIRs.")

# 2. Update Graph Title
content = content.replace("Top Entities (Global Centrality)", "Most Connected Masterminds (By Total Links)")

# 3. Update the 4 Stat Cards
# Card 1: Density -> Activity Level
content = content.replace("Global Graph Density", "Overall Syndicate Activity")
content = content.replace("0.042", "Low (Cell-based)")
content = content.replace("Sparse network", "Suspects are hiding in isolated cells")

# Card 2: Communities -> Gangs
content = content.replace("Identified Communities", "Distinct Gangs / Sleeper Cells")
content = content.replace("Modularity: 0.68", "AI isolated 14 separate criminal groups")

# Card 3: Cross-Case Links
content = content.replace("Cross-Case Links", "Repeat Offenders Across FIRs")
content = content.replace("+12 this week", "12 new links between different police stations")

# Card 4: Path Length -> Chain of Command
content = content.replace("Average Path Length", "Chain of Command Depth")
content = content.replace("Degrees of separation", "Middle-men between street worker & boss")

# 4. Update the Alert Section
content = content.replace("Cross-Modal Correlation Alerts", "🚨 Urgent AI Detective Alerts")
content = content.replace("Identity Resolution Match", "Alias Detected: Same Person Using Fake Names")
content = content.replace("High confidence match between \"R. Sharma\" (CASE 102) and \"Rahul S.\" (CASE 085) based on shared phone and location markers.", "AI caught a criminal lying: 'R. Sharma' in Case 102 and 'Rahul S.' in Case 085 are the exact same person sharing a burner phone.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Analytics terminology simplified for police officers.")
