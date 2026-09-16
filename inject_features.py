import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add AiCopilot import
if "import { AiCopilot }" not in content:
    content = content.replace(
        "import { LocationMap, MapLocation } from '../components/map/LocationMap';",
        "import { LocationMap, MapLocation } from '../components/map/LocationMap';\nimport { AiCopilot } from '../components/chat/AiCopilot';"
    )

# 2. Add AiCopilot to the end of the CasePage render
if "<AiCopilot caseData={caseData} />" not in content:
    content = content.replace(
        "    </div>\n  );\n};\n\nexport default CasePage;",
        "      <AiCopilot caseData={caseData} />\n    </div>\n  );\n};\n\nexport default CasePage;"
    )

# 3. Update the Request CDR Subpoena button to download a real file
old_subpoena_btn = """<button className="w-full mt-4 bg-slate-800 hover:bg-slate-700 border border-slate-600 text-slate-200 text-xs py-1.5 rounded transition-colors">
                          Request CDR Subpoena
                        </button>"""

new_subpoena_btn = """<button 
                          onClick={(e) => {
                             e.stopPropagation();
                             const docContent = `CONFIDENTIAL - LAW ENFORCEMENT ONLY\\n\\nSUBPOENA DUCES TECUM (CDR REQUEST)\\n\\nTO: Telecom Nodal Officer\\nRE: Case ${caseData.title}\\nDATE: ${new Date().toLocaleDateString()}\\n\\nPursuant to Section 91 of the Code of Criminal Procedure, 1973, you are hereby directed to produce the Call Detail Records (CDR), Tower Location Data, and Customer Acquisition Form (CAF) for the following cellular target:\\n\\nTARGET MSISDN: ${caseData.suspect.imei}\\nSUSPECT NAME: ${caseData.suspect.name}\\nPERIOD: Last 90 Days\\n\\nThis information is strictly required for the ongoing investigation of the aforementioned cyber-crime FIR.\\n\\nAuthorized By:\\nInvestigating Officer (Cyber Cell)\\nAI-CNAS Automated Request Generator`;
                             const blob = new Blob([docContent], { type: 'text/plain' });
                             const url = URL.createObjectURL(blob);
                             const a = document.createElement('a');
                             a.href = url;
                             a.download = `Subpoena_CDR_${caseData.suspect.name.replace(/\\s+/g, '_')}.txt`;
                             document.body.appendChild(a);
                             a.click();
                             document.body.removeChild(a);
                             URL.revokeObjectURL(url);
                             alert("Official Subpoena Document generated and downloaded successfully!");
                          }}
                          className="w-full mt-4 bg-blue-600 hover:bg-blue-500 border border-blue-500 shadow-[0_0_10px_rgba(37,99,235,0.3)] text-white font-bold tracking-wide text-xs py-1.5 rounded transition-colors flex items-center justify-center gap-2"
                        >
                          <FileText size={14} /> 1-Click Generate Subpoena
                        </button>"""

content = content.replace(old_subpoena_btn, new_subpoena_btn)

# Make sure to import FileText in AiCopilot if not already, but it's used in CasePage so it's fine.
# We also have "View Full Intelligence Profile" button which we can turn into an arrest warrant generator
old_profile_btn = """<button className="w-full mt-4 bg-slate-800 hover:bg-slate-700 border border-slate-600 text-slate-200 text-xs py-1.5 rounded transition-colors">
                          View Full Intelligence Profile
                        </button>"""

new_profile_btn = """<button 
                          onClick={(e) => {
                             e.stopPropagation();
                             const docContent = `ARREST WARRANT MEMORANDUM\\n\\nTARGET: ${caseData.suspect.name}\\nALIASES: ${caseData.suspect.aliases}\\nLAST KNOWN LOCATION: ${caseData.suspect.location}\\nTHREAT LEVEL: ${caseData.suspect.threat}\\nCENTRALITY SCORE: ${caseData.suspect.centrality}\\n\\nJUSTIFICATION:\\n${caseData.suspect.notes}\\n\\nAI-CNAS SYSTEM GENERATED - CONFIDENTIAL`;
                             const blob = new Blob([docContent], { type: 'text/plain' });
                             const url = URL.createObjectURL(blob);
                             const a = document.createElement('a');
                             a.href = url;
                             a.download = `Warrant_Memo_${caseData.suspect.name.replace(/\\s+/g, '_')}.txt`;
                             document.body.appendChild(a);
                             a.click();
                             document.body.removeChild(a);
                             URL.revokeObjectURL(url);
                             alert("Warrant Memorandum generated and downloaded successfully!");
                          }}
                          className="w-full mt-4 bg-red-600/80 hover:bg-red-500 border border-red-500 shadow-[0_0_10px_rgba(239,68,68,0.2)] text-white font-bold tracking-wide text-xs py-1.5 rounded transition-colors flex items-center justify-center gap-2"
                        >
                          <ShieldAlert size={14} /> Generate Arrest Warrant Memo
                        </button>"""

content = content.replace(old_profile_btn, new_profile_btn)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected AiCopilot and Subpoena generator into CasePage.tsx.")
