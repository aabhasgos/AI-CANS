import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add import
if "getCaseData" not in content:
    content = content.replace("import { LocationMap, MapLocation } from '../components/map/LocationMap';", "import { LocationMap, MapLocation } from '../components/map/LocationMap';\nimport { getCaseData } from '../data/mockDatabase';\nimport { useParams } from 'react-router-dom';")

# 2. Extract useParams and caseData
hook_str = """const CasePage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const caseData = getCaseData(id || '1');"""
content = content.replace("const CasePage: React.FC = () => {", hook_str)

# 3. Remove old hardcoded consts
content = re.sub(r"const mockGraphData: GraphData = \{.*?\};", "", content, flags=re.DOTALL)
content = re.sub(r"const mockTimelineEvents: TimelineEvent\[\] = \[.*?\];", "", content, flags=re.DOTALL)
content = re.sub(r"const mockLocations: MapLocation\[\] = \[.*?\];", "", content, flags=re.DOTALL)

# 4. Replace hardcoded references with caseData
content = content.replace("CASE-2024-102", "CASE-2024-{id || '102'}")
content = content.replace("Hawala Syndicate Crackdown", "{caseData.title}")
content = content.replace("Inspector Vikram Singh", "{caseData.leadIO}")
content = content.replace("Delhi Cyber Cell / ED", "{caseData.jurisdiction}")
content = content.replace("IPC 420, 120B, 467 & PMLA Sec 3", "{caseData.ipc}")
content = content.replace("Acting on classified intelligence inputs regarding illegal cross-border financial routing, an operation was launched targeting a sophisticated Hawala network operating out of Delhi NCR. The syndicate utilizes shell companies (e.g., Global Tech Solutions) to launder funds acquired through cyber-fraud operations (Jamtara links). The primary suspect, Rakesh Sharma, coordinates the physical handover of cash while communicating via encrypted VOIP and unregistered burner SIM cards. \n                        <br/><br/>\n                        <strong>Modus Operandi (M.O.):</strong> The syndicate intercepts legitimate business payments via BEC (Business Email Compromise), routes the fiat currency into crypto wallets, and subsequently uses local handlers to distribute physical cash to beneficiaries.", "{caseData.summary}")

# Suspect Details
content = content.replace("Rakesh Sharma", "{caseData.suspect.name}")
content = content.replace("\"Raka\", \"Boss\"", "{caseData.suspect.aliases}")
content = content.replace("THREAT: HIGH", "THREAT: {caseData.suspect.threat}")
content = content.replace("Connaught Place, Delhi", "{caseData.suspect.location}")
content = content.replace("0.89 (Top 1%)", "{caseData.suspect.centrality}")
content = content.replace("Jio / Airtel (India)", "{caseData.suspect.carrier}")
content = content.replace("Fake ID (Flagged)", "{caseData.suspect.kyc}")
content = content.replace("35102930192301", "{caseData.suspect.imei}")
content = content.replace("Subject demonstrates high financial literacy and avoids holding assets in his own name. Often uses rural proxies (Jamtara region) for initial fund collection. Demonstrates recidivism with escalating organizational complexity.", "{caseData.suspect.notes}")

# Criminal History Table
history_table = """
                              <tbody className="divide-y divide-slate-700 text-slate-300">
                                {caseData.suspect.history.map((h: any, i: number) => (
                                  <tr key={i}>
                                    <td className="p-2">{h.year}</td>
                                    <td className="p-2 text-blue-400 cursor-pointer">{h.fir}</td>
                                    <td className="p-2">{h.charges}</td>
                                    <td className="p-2"><span className={h.color}>{h.status}</span></td>
                                  </tr>
                                ))}
                              </tbody>
"""
content = re.sub(r"<tbody className=\"divide-y divide-slate-700 text-slate-300\">.*?<\/tbody>", history_table.strip(), content, flags=re.DOTALL)


# Variables for graph, timeline, map
content = content.replace("elements={mockGraphData}", "elements={caseData.graph}")
content = content.replace("events={mockTimelineEvents}", "events={caseData.timeline}")
content = content.replace("locations={mockLocations}", "locations={caseData.map.locations}")
content = content.replace("connections={[{from: 'l1', to: 'l2'}]}", "connections={caseData.map.connections}")

# ExplainLink
content = content.replace("mockGraphData.edges", "caseData.graph.edges")
content = content.replace("mockGraphData.nodes", "caseData.graph.nodes")
content = content.replace("CRIMINOLOGY ANALYSIS: The AI NLP engine correlated this link by cross-referencing FIR-2026-DEL-001 with CCTNS historic records. The suspect ({caseData.suspect.name}) exhibits a known Modus Operandi (M.O.) of utilizing unregistered burner assets (like +91 9876543210) for short-term extortion calls. The linguistic pattern in the intercepted audio matches his known voice print from the 2018 conviction.", "{caseData.reason}")
content = content.replace("CRIMINOLOGY ANALYSIS: The AI NLP engine correlated this link by cross-referencing FIR-2026-DEL-001 with CCTNS historic records. The suspect (Rakesh Sharma) exhibits a known Modus Operandi (M.O.) of utilizing unregistered burner assets (like +91 9876543210) for short-term extortion calls. The linguistic pattern in the intercepted audio matches his known voice print from the 2018 conviction.", "{caseData.reason}")


# Wait, what if {caseData.suspect.name} got replaced wrong? Let's just catch the whole reason block
import re
reason_pattern = r"CRIMINOLOGY ANALYSIS: The AI NLP engine correlated this link by cross-referencing FIR-2026-DEL-001 with CCTNS historic records\..*?conviction\."
content = re.sub(reason_pattern, "{caseData.reason}", content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dynamic Case Page wired.")
