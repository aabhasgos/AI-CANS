import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """                          <div className="mt-6 p-4 bg-red-500/10 border border-red-500/20 rounded text-sm">
                            <strong className="text-red-400 block mb-1">Criminology & Behavioral Note:</strong>
                            {caseData.suspect.notes}
                          </div>
                        </div>
                      </div>
                    </div>

                  </div>
                </div>"""

new_block = """                          <div className="mt-6 p-4 bg-red-500/10 border border-red-500/20 rounded text-sm">
                            <strong className="text-red-400 block mb-1">Criminology & Behavioral Note:</strong>
                            {caseData.suspect.notes}
                          </div>
                        </div>
                      </div>
                    </div>
                    
                    {/* Legal Actions */}
                    <div className="mt-8 pt-6 border-t border-slate-700/50">
                       <h3 className="text-lg font-semibold text-white mb-4 flex items-center gap-2"><ShieldAlert className="w-5 h-5 text-amber-400"/> Automated Legal Actions</h3>
                       <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                           <button 
                             onClick={(e) => {
                               e.stopPropagation();
                               const docContent = `CONFIDENTIAL - LAW ENFORCEMENT ONLY\\n\\nSUBPOENA DUCES TECUM (CDR REQUEST)\\n\\nTO: Telecom Nodal Officer\\nRE: Case ${caseData.title}\\nDATE: ${new Date().toLocaleDateString()}\\n\\nPursuant to Section 91 of the Code of Criminal Procedure, 1973, you are hereby directed to produce the Call Detail Records (CDR), Tower Location Data, and Customer Acquisition Form (CAF) for the following cellular target:\\n\\nTARGET MSISDN: ${caseData.suspect.imei}\\nSUSPECT NAME: ${caseData.suspect.name}\\nPERIOD: Last 90 Days\\n\\nThis information is strictly required for the ongoing investigation of the aforementioned cyber-crime FIR.\\n\\nAuthorized By:\\nInvestigating Officer (Cyber Cell)\\nAI-CNAS Automated Request Generator`;
                               const blob = new Blob([docContent], { type: 'text/plain' });
                               const url = URL.createObjectURL(blob);
                               const a = document.createElement('a');
                               a.href = url;
                               a.download = `Subpoena_CDR_${caseData.suspect.name.replace(/\s+/g, '_')}.txt`;
                               document.body.appendChild(a);
                               a.click();
                               document.body.removeChild(a);
                               URL.revokeObjectURL(url);
                               alert("Official Subpoena Document generated and downloaded successfully!");
                             }}
                             className="bg-slate-800 hover:bg-slate-700 border border-blue-500/30 hover:border-blue-500 text-slate-200 p-4 rounded-lg flex flex-col items-center justify-center text-center transition-all group"
                           >
                             <FileText className="w-8 h-8 text-blue-400 mb-2 group-hover:scale-110 transition-transform" />
                             <span className="font-bold mb-1">1-Click CDR Subpoena</span>
                             <span className="text-xs text-slate-400">Generates official Sec 91 CrPC Request</span>
                           </button>

                           <button 
                             onClick={(e) => {
                               e.stopPropagation();
                               const docContent = `ARREST WARRANT MEMORANDUM\\n\\nTARGET: ${caseData.suspect.name}\\nALIASES: ${caseData.suspect.aliases}\\nLAST KNOWN LOCATION: ${caseData.suspect.location}\\nTHREAT LEVEL: ${caseData.suspect.threat}\\nCENTRALITY SCORE: ${caseData.suspect.centrality}\\n\\nJUSTIFICATION:\\n${caseData.suspect.notes}\\n\\nAI-CNAS SYSTEM GENERATED - CONFIDENTIAL`;
                               const blob = new Blob([docContent], { type: 'text/plain' });
                               const url = URL.createObjectURL(blob);
                               const a = document.createElement('a');
                               a.href = url;
                               a.download = `Warrant_Memo_${caseData.suspect.name.replace(/\s+/g, '_')}.txt`;
                               document.body.appendChild(a);
                               a.click();
                               document.body.removeChild(a);
                               URL.revokeObjectURL(url);
                               alert("Warrant Memorandum generated and downloaded successfully!");
                             }}
                             className="bg-slate-800 hover:bg-slate-700 border border-red-500/30 hover:border-red-500 text-slate-200 p-4 rounded-lg flex flex-col items-center justify-center text-center transition-all group"
                           >
                             <ShieldAlert className="w-8 h-8 text-red-400 mb-2 group-hover:scale-110 transition-transform" />
                             <span className="font-bold mb-1">Arrest Warrant Memo</span>
                             <span className="text-xs text-slate-400">Generates Judicial Execution Request</span>
                           </button>
                       </div>
                    </div>

                  </div>
                </div>"""

content = content.replace(old_block, new_block)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected automated legal actions into main dossier view.")
