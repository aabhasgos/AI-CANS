import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\data\mockDatabase.ts"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add evidence array to Case 1
if "evidence: [" not in content:
    content = content.replace("reason: 'The AI NLP engine correlated", """evidence: [
        { id: 'e1', name: 'FIR_Report_Original.pdf', date: '2 days ago', type: 'doc', entities: 12 },
        { id: 'e2', name: 'CDR_Dump_Aug26.csv', date: '1 day ago', type: 'cdr', entities: 84 }
      ],
      reason: 'The AI NLP engine correlated""")

    # Add evidence array to Case 2
    content = content.replace("reason: 'The AI correlated this link by cross-referencing cell tower", """evidence: [
        { id: 'e3', name: 'Jamtara_Tower_Ping_Logs.xlsx', date: '5 hours ago', type: 'cdr', entities: 412 },
        { id: 'e4', name: 'SBI_ATM_CCTV_Footage.mp4', date: '12 hours ago', type: 'media', entities: 3 }
      ],
      reason: 'The AI correlated this link by cross-referencing cell tower""")

    # Add evidence array to Case 3
    content = content.replace("reason: 'AI detected a pattern of satellite", """evidence: [
        { id: 'e5', name: 'BSF_Drone_Sighting_Report.pdf', date: '4 days ago', type: 'doc', entities: 8 },
        { id: 'e6', name: 'SatPhone_Intercepts.txt', date: '1 day ago', type: 'cdr', entities: 45 },
        { id: 'e7', name: 'Safehouse_Raid_Inventory.pdf', date: 'Just now', type: 'doc', entities: 112 }
      ],
      reason: 'AI detected a pattern of satellite""")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added evidence arrays to mockDatabase.")
