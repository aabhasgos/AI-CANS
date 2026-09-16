import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert Dossier Content
dossier_content = """
              {activeMainTab === 'dossier' && (
                <div className="h-full w-full bg-slate-900 overflow-y-auto p-6 text-slate-300">
                  <div className="max-w-5xl mx-auto space-y-8 pb-20">
                    
                    {/* Header */}
                    <div className="border-b border-slate-700 pb-4">
                      <div className="flex items-center gap-3 mb-2">
                        <span className="px-3 py-1 bg-blue-500/20 text-blue-400 text-xs font-bold uppercase rounded border border-blue-500/30">CCTNS Master File</span>
                        <h2 className="text-2xl font-bold text-white">{caseData.title}</h2>
                      </div>
                      <div className="flex gap-6 text-sm text-slate-400 mt-3">
                        <p><strong className="text-slate-300">Lead IO:</strong> {caseData.leadIO}</p>
                        <p><strong className="text-slate-300">Jurisdiction:</strong> {caseData.jurisdiction}</p>
                        <p><strong className="text-slate-300">Filed Under:</strong> {caseData.ipc}</p>
                      </div>
                    </div>

                    {/* Case Summary */}
                    <div className="bg-slate-800 border border-slate-700 rounded-lg p-5">
                      <h3 className="text-lg font-semibold text-white mb-3 flex items-center gap-2"><FileText className="w-5 h-5 text-blue-400"/> Detailed Case Summary</h3>
                      <p className="text-sm leading-relaxed text-slate-300">
                        {caseData.summary}
                      </p>
                    </div>

                    {/* Criminal History & Profile */}
                    <div>
                      <h3 className="text-lg font-semibold text-white mb-4 flex items-center gap-2"><Users className="w-5 h-5 text-red-400"/> Primary Target Profile & Criminal History</h3>
                      
                      <div className="bg-slate-800 border border-red-500/30 rounded-lg overflow-hidden flex flex-col md:flex-row">
                        {/* Mugshot/Bio area */}
                        <div className="bg-slate-900/50 p-6 md:w-1/3 border-r border-slate-700">
                          <div className="w-32 h-32 bg-slate-800 rounded-lg border-2 border-slate-700 mx-auto flex items-center justify-center mb-4 relative overflow-hidden">
                             <User className="w-16 h-16 text-slate-600" />
                             <div className="absolute bottom-0 left-0 right-0 bg-red-500 text-white text-[10px] text-center font-bold py-1">KNOWN OFFENDER</div>
                          </div>
                          <h4 className="text-xl font-bold text-center text-white mb-1">{caseData.suspect.name}</h4>
                          <p className="text-center text-xs text-slate-400 mb-4">Alias: {caseData.suspect.aliases}</p>
                          
                          <div className="space-y-2 text-xs">
                            <div className="flex justify-between border-b border-slate-700/50 pb-1">
                              <span className="text-slate-500">Aadhar Link</span>
                              <span className="text-amber-400 font-mono">XXXX-XXXX-9102</span>
                            </div>
                            <div className="flex justify-between border-b border-slate-700/50 pb-1">
                              <span className="text-slate-500">PAN</span>
                              <span className="text-amber-400 font-mono">BQPPS****F</span>
                            </div>
                            <div className="flex justify-between border-b border-slate-700/50 pb-1">
                              <span className="text-slate-500">AFIS Fingerprint</span>
                              <span className="text-green-400">Match Found (2018)</span>
                            </div>
                            <div className="flex justify-between pb-1">
                              <span className="text-slate-500">Risk Assessment</span>
                              <span className="text-red-400 font-bold">FLIGHT RISK</span>
                            </div>
                          </div>
                        </div>

                        {/* Criminal Record Table */}
                        <div className="p-6 md:w-2/3">
                          <h5 className="text-sm font-semibold text-slate-200 uppercase tracking-wider mb-3">Previous Criminal Record (CCTNS Database)</h5>
                          <div className="overflow-x-auto">
                            <table className="w-full text-left text-xs">
                              <thead className="bg-slate-900 text-slate-400">
                                <tr>
                                  <th className="p-2">Year</th>
                                  <th className="p-2">FIR No.</th>
                                  <th className="p-2">Charges / IPC</th>
                                  <th className="p-2">Status</th>
                                </tr>
                              </thead>
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
                            </table>
                          </div>
                          
                          <div className="mt-6 p-4 bg-red-500/10 border border-red-500/20 rounded text-sm">
                            <strong className="text-red-400 block mb-1">Criminology & Behavioral Note:</strong>
                            {caseData.suspect.notes}
                          </div>
                        </div>
                      </div>
                    </div>

                  </div>
                </div>
              )}
"""

# Insert right before the closing div of "absolute inset-0"
pattern_map = r"(<LocationMap locations=\{caseData\.map\.locations\} connections=\{caseData\.map\.connections\} \/>\s*<\/div>\s*)\)}"
content = re.sub(pattern_map, r"\1)}\n" + dossier_content.replace("\\", "\\\\"), content)

# 2. Insert Side Tab content
syndicates_evidence_content = """
            {activeSideTab === 'communities' && (
              <div className="space-y-4">
                <h3 className="text-sm font-semibold text-slate-300 uppercase tracking-wider mb-3">AI Identified Syndicates</h3>
                <div className="bg-slate-800 border border-slate-700 rounded-lg p-4">
                  <h4 className="font-bold text-slate-200 flex items-center gap-2"><Network className="w-4 h-4 text-emerald-400"/> Primary Operation Cell</h4>
                  <p className="text-xs text-slate-400 mt-1 mb-3">High density cluster indicating direct command structure.</p>
                  <div className="flex flex-wrap gap-2">
                    <span className="px-2 py-1 bg-slate-900 rounded text-xs text-slate-300 border border-slate-700">{caseData.suspect.name}</span>
                    <span className="px-2 py-1 bg-slate-900 rounded text-xs text-slate-300 border border-slate-700">+91 9876543210</span>
                  </div>
                </div>
                <div className="bg-slate-800 border border-slate-700 rounded-lg p-4">
                  <h4 className="font-bold text-slate-200 flex items-center gap-2"><Network className="w-4 h-4 text-emerald-400"/> Financial Sub-Cell</h4>
                  <p className="text-xs text-slate-400 mt-1 mb-3">Separated cluster handling money laundering.</p>
                  <div className="flex flex-wrap gap-2">
                    <span className="px-2 py-1 bg-slate-900 rounded text-xs text-slate-300 border border-slate-700">Shell Accounts</span>
                    <span className="px-2 py-1 bg-slate-900 rounded text-xs text-slate-300 border border-slate-700">Mule Network</span>
                  </div>
                </div>
              </div>
            )}
            
            {activeSideTab === 'evidence' && (
              <div className="space-y-4">
                <h3 className="text-sm font-semibold text-slate-300 uppercase tracking-wider mb-3">Processed Raw Files</h3>
                
                <div className="bg-slate-800 border border-slate-700 hover:border-slate-500 cursor-pointer rounded-lg p-3 transition-colors">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-blue-500/20 text-blue-400 rounded flex items-center justify-center shrink-0">
                      <FileText size={20} />
                    </div>
                    <div>
                      <h4 className="font-medium text-slate-200 text-sm">FIR_Report_Original.pdf</h4>
                      <p className="text-xs text-slate-500 mt-0.5">Uploaded 2 days ago</p>
                    </div>
                  </div>
                  <div className="mt-3 flex gap-2">
                    <span className="text-[10px] uppercase bg-slate-900 px-2 py-1 rounded border border-slate-700 text-emerald-400">12 Entities Found</span>
                  </div>
                </div>

                <div className="bg-slate-800 border border-slate-700 hover:border-slate-500 cursor-pointer rounded-lg p-3 transition-colors">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-amber-500/20 text-amber-400 rounded flex items-center justify-center shrink-0">
                      <Activity size={20} />
                    </div>
                    <div>
                      <h4 className="font-medium text-slate-200 text-sm">CDR_Dump_Aug26.csv</h4>
                      <p className="text-xs text-slate-500 mt-0.5">Uploaded 1 day ago</p>
                    </div>
                  </div>
                  <div className="mt-3 flex gap-2">
                    <span className="text-[10px] uppercase bg-slate-900 px-2 py-1 rounded border border-slate-700 text-emerald-400">84 Calls Mapped</span>
                  </div>
                </div>
                
                <button className="w-full py-2 bg-slate-800 hover:bg-slate-700 border border-slate-600 border-dashed rounded text-sm text-slate-300 font-medium transition-colors">
                  + Upload More Evidence
                </button>
              </div>
            )}
"""

pattern_anomalies = r"(<button className=\"mt-2 text-xs text-blue-400 hover:text-blue-300\">Highlight in Graph<\/button>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*)\)}"
content = re.sub(pattern_anomalies, r"\1)}\n" + syndicates_evidence_content.replace("\\", "\\\\"), content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("CasePage tabs fully injected.")
