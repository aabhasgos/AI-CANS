import os
import glob

replacements = {
    "Officer Smith": "Inspector Vikram Singh",
    "#49281": "UP-49281",
    "Operation Silk Road 2.0": "Hawala Syndicate Crackdown",
    "Downtown Syndicate": "Jamtara Phishing Ring",
    "Node A": "Rakesh Sharma",
    "Node B": "Mohit Kumar",
    "Node C": "Sanjay Khan",
    "Node D": "Priya Singh",
    "Node E": "Global Tech Solutions",
    "Global Search (Entities, Cases, Phone Numbers...)": "CCTNS/ICJS Global Search (Entities, FIRs, Phone Numbers...)",
    "Global Analytics Dashboard": "National Intelligence Analytics Dashboard"
}

for filepath in glob.glob('frontend/src/**/*.tsx', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            modified = True
            
    if modified:
        print(f'Updated {filepath}')
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
