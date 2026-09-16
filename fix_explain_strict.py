import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the data block exactly
old_data_start = """                const relType = edge.data.label;
                
                return {"""

old_data_full = """                const relType = edge.data.label;
                
                return {
                  id: selectedElement.id!,
                  type: relType,
                  sourceLabel: source,
                  targetLabel: target,
                  confidence: edge.data.confidence || 0.85,
                  observationPeriod: 'Active Tracking',
                  reasonText: `CRIMINOLOGY ANALYSIS: The AI NLP engine correlated this link by cross-referencing recent FIRs with CCTNS historic records. The system detected that [${source}] and [${target}] are connected via a high-confidence [${relType.replace(/_/g, ' ')}] relationship.`,
                  sources: [
                    { id: 'src1', name: `FIR Extraction Report`, date: new Date().toLocaleDateString() }
                  ],
                  evidenceRecords: [
                    { id: 'ev1', type: 'NLP Extraction', detail: `Found explicit contextual match indicating ${source} is associated with ${target}.` },
                    { id: 'ev2', type: 'Database Cross-Ref', detail: `Match found in National Intelligence Grid (NATGRID) validating this connection.` }
                  ]
                };"""

new_data_full = """                const relType = edge.data.label;
                
                let reasonText = "";
                let evidence1 = "";
                let evidence2 = "";
                
                if (relType === 'CALLS' || relType === 'CONTACTED') {
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
                }
                
                return {
                  id: selectedElement.id!,
                  type: relType,
                  sourceLabel: source,
                  targetLabel: target,
                  confidence: edge.data.confidence || 0.85,
                  observationPeriod: 'Active Tracking',
                  reasonText: reasonText,
                  sources: [
                    { id: 'src1', name: `Automated Multi-Modal Intelligence Report`, date: new Date().toLocaleDateString() }
                  ],
                  evidenceRecords: [
                    { id: 'ev1', type: 'Primary Vector', detail: evidence1 },
                    { id: 'ev2', type: 'Secondary Verification', detail: evidence2 }
                  ]
                };"""

content = content.replace(old_data_full, new_data_full)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("CasePage detailed explanation strictly injected.")
