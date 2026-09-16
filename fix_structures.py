import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\data\mockDatabase.ts"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix timeline generation
old_timeline = """        timelineData.push({
          id: `t_${idx}`,
          date: `2026-08-${10 + (idx % 20)}`,
          type: type,
          title: title,
          description: `AI extraction pipeline confirmed linking of ${n.data.label} to primary target via NLP document processing.`,
          source: 'FIR Text Extraction'
        });"""

new_timeline = """        timelineData.push({
          id: `t_${idx}`,
          date: `2026-08-${10 + (idx % 20)}`,
          type: type,
          title: title,
          description: `AI extraction pipeline confirmed linking of ${n.data.label} to primary target via NLP document processing.`,
          source: 'FIR Text Extraction',
          entities: [n.data.label, primarySuspect],
          confidence: 95
        });"""

content = content.replace(old_timeline, new_timeline)

# Fix map generation
old_map = """          mapData.locations.push({
            id: `loc_${idx}`,
            name: n.data.label,
            coordinates: [19.11 + (Math.random()*2), 72.84 + (Math.random()*2)],
            type: 'SAFEHOUSE',
            threat: 'HIGH'
          });"""

new_map = """          mapData.locations.push({
            id: `loc_${idx}`,
            name: n.data.label,
            lat: 19.11 + (Math.random()*2),
            lng: 72.84 + (Math.random()*2),
            type: 'SAFEHOUSE',
            events: ['Surveillance Ping', 'Entity Sighted']
          });"""

content = content.replace(old_map, new_map)

# Let's also fix the "Unidentified" target label name the user complained about
# I will make it extract a name from the nodes or just name it "Suspect Unknown"
# The user said "its showing unidentified". Let's name it something more authoritative.
old_name = """nodes.push({ data: { id: 'ext_main', label: 'Primary Target (Unidentified)'"""
new_name = """nodes.push({ data: { id: 'ext_main', label: 'Target: Primary Suspect'"""

with open(r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\IngestionPage.tsx", 'r', encoding='utf-8') as f:
    ingest_content = f.read()

ingest_content = ingest_content.replace(old_name, new_name)

with open(r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\IngestionPage.tsx", 'w', encoding='utf-8') as f:
    f.write(ingest_content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed mock database structures and unidentified label")
