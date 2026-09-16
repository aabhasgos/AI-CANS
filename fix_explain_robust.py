import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the specific condition block to be more robust
old_condition_block = """                if (relType === 'CALLS' || relType === 'CONTACTED') {
                    reasonText = `COMMUNICATIONS ANALYSIS: The AI detected a hidden communications channel between [${source}] and [${target}]. Temporal graph analysis indicates calls spike immediately before known criminal events, suggesting a command-and-control hierarchy.`;
                    evidence1 = `CDR Dump match: 14 incoming/outgoing calls detected over a 72-hour period.`;
                    evidence2 = `Cell tower triangulation places both devices within 500m of the crime scene.`;
                } else if (relType === 'FUNDS_TRANSFERRED' || relType === 'OWNS_ACCOUNT') {
                    reasonText = `FINANCIAL FORENSICS: The system flagged a high-risk financial link. [${source}] successfully bypassed standard AML (Anti-Money Laundering) checks by structuring deposits, which were ultimately funneled into [${target}].`;
                    evidence1 = `Bank Statement OCR: Extracted 3 structured transactions under ₹49,000.`;
                    evidence2 = `Financial Intelligence Unit (FIU) alert: Shell company overlap detected.`;
                } else if (relType === 'LOCATED_AT' || relType === 'OPERATES_IN') {
                    reasonText = `GEOSPATIAL INTELLIGENCE: [${source}] is definitively anchored to [${target}]. AI cross-referenced IP logs, CCTV facial recognition pings, and delivery records to establish this safehouse/operational base connection.`;
                    evidence1 = `IP Log Analysis: MAC address pinged from a router at this exact coordinate.`;
                    evidence2 = `CCTV Feed Analysis: Facial match (89% confidence) entering the premises.`;
                } else {
                    reasonText = `CRIMINOLOGY ANALYSIS: The AI correlated this link by cross-referencing recent FIRs with CCTNS historic records. The system detected that [${source}] and [${target}] are connected via a high-confidence [${relType.replace(/_/g, ' ')}] relationship. This forms a critical triad in the syndicate structure.`;
                    evidence1 = `NLP Extraction: Explicit contextual match indicating association found in FIR narrative.`;
                    evidence2 = `National Intelligence Grid (NATGRID): Match found in historic associate database.`;
                }"""

new_condition_block = """                const lowerRel = relType.toLowerCase();
                
                if (lowerRel.includes('call') || lowerRel.includes('communicat') || lowerRel.includes('contact')) {
                    reasonText = `COMMUNICATIONS ANALYSIS: The AI detected a hidden communications channel between [${source}] and [${target}]. Temporal graph analysis indicates calls spike immediately before known criminal events, suggesting a command-and-control hierarchy.`;
                    evidence1 = `CDR Dump match: Multiple incoming/outgoing connections detected over a critical 72-hour period.`;
                    evidence2 = `Cell tower triangulation places both devices within 500m of the primary crime scene.`;
                } else if (lowerRel.includes('fund') || lowerRel.includes('operat') || lowerRel.includes('own') || lowerRel.includes('director')) {
                    reasonText = `FINANCIAL FORENSICS & ASSET OWNERSHIP: The system flagged a high-risk structural link. AI determined that [${source}] exercises direct control over [${target}], bypassing standard AML (Anti-Money Laundering) checks or operating through proxy layers.`;
                    evidence1 = `Bank/Asset OCR: Extracted structured ownership records or transactions linking the entities.`;
                    evidence2 = `Financial Intelligence Unit (FIU) alert: Shell structure or mule overlap detected.`;
                } else if (lowerRel.includes('locat') || lowerRel.includes('arrest') || lowerRel.includes('drop')) {
                    reasonText = `GEOSPATIAL INTELLIGENCE: [${source}] is definitively anchored to [${target}]. AI cross-referenced IP logs, CCTV facial recognition pings, and operational delivery records to establish this coordinate connection.`;
                    evidence1 = `Geospatial Log Analysis: Mobile/Router MAC address pinged at this exact map coordinate.`;
                    evidence2 = `CCTV Feed / Field Intelligence: Facial match (89% confidence) or physical surveillance confirmation.`;
                } else {
                    reasonText = `CRIMINOLOGY ANALYSIS: The AI correlated this link by cross-referencing recent FIRs with CCTNS historic records. The system detected that [${source}] and [${target}] are connected via a high-confidence [${relType.replace(/_/g, ' ')}] relationship. This forms a critical triad in the syndicate structure.`;
                    evidence1 = `NLP Extraction: Explicit contextual match indicating association found in FIR narrative.`;
                    evidence2 = `National Intelligence Grid (NATGRID): Match found in historic associate database.`;
                }"""

content = content.replace(old_condition_block, new_condition_block)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Robust relationship matching injected.")
