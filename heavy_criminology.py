import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add the 4th Tab Button
old_tabs = """<button 
              onClick={() => setActiveMainTab('map')}
              className={`flex items-center gap-2 px-4 py-2.5 text-sm font-medium border-b-2 transition-colors ${activeMainTab === 'map' ? 'border-blue-500 text-blue-400' : 'border-transparent text-slate-400 hover:text-slate-200'}`}
            >
              <MapIcon className="w-4 h-4" /> 3. Crime Map (Where?)
            </button>"""

new_tabs = old_tabs + """
            <button 
              onClick={() => setActiveMainTab('dossier')}
              className={`flex items-center gap-2 px-4 py-2.5 text-sm font-medium border-b-2 transition-colors ${activeMainTab === 'dossier' ? 'border-blue-500 text-blue-400' : 'border-transparent text-slate-400 hover:text-slate-200'}`}
            >
              <FileText className="w-4 h-4" /> 4. Master Criminal Dossier & Case Details
            </button>
"""
if "4. Master Criminal Dossier" not in content:
    content = content.replace(old_tabs, new_tabs)

# 2. Add the 4th Tab Content (Heavy Criminology Details)
dossier_content = """
              {activeMainTab === 'dossier' && (
                <div className="h-full w-full bg-slate-900 overflow-y-auto p-6 text-slate-300">
                  <div className="max-w-5xl mx-auto space-y-8 pb-20">
                    
                    {/* Header */}
                    <div className="border-b border-slate-700 pb-4">
                      <div className="flex items-center gap-3 mb-2">
                        <span className="px-3 py-1 bg-blue-500/20 text-blue-400 text-xs font-bold uppercase rounded border border-blue-500/30">CCTNS Master File</span>
                        <h2 className="text-2xl font-bold text-white">CASE-2024-102: Hawala Syndicate Crackdown</h2>
                      </div>
                      <div className="flex gap-6 text-sm text-slate-400 mt-3">
                        <p><strong className="text-slate-300">Lead IO:</strong> Inspector Vikram Singh</p>
                        <p><strong className="text-slate-300">Jurisdiction:</strong> Delhi Cyber Cell / ED</p>
                        <p><strong className="text-slate-300">Filed Under:</strong> IPC 420, 120B, 467 & PMLA Sec 3</p>
                      </div>
                    </div>

                    {/* Case Summary */}
                    <div className="bg-slate-800 border border-slate-700 rounded-lg p-5">
                      <h3 className="text-lg font-semibold text-white mb-3 flex items-center gap-2"><FileText className="w-5 h-5 text-blue-400"/> Detailed Case Summary</h3>
                      <p className="text-sm leading-relaxed text-slate-300">
                        Acting on classified intelligence inputs regarding illegal cross-border financial routing, an operation was launched targeting a sophisticated Hawala network operating out of Delhi NCR. The syndicate utilizes shell companies (e.g., Global Tech Solutions) to launder funds acquired through cyber-fraud operations (Jamtara links). The primary suspect, Rakesh Sharma, coordinates the physical handover of cash while communicating via encrypted VOIP and unregistered burner SIM cards. 
                        <br/><br/>
                        <strong>Modus Operandi (M.O.):</strong> The syndicate intercepts legitimate business payments via BEC (Business Email Compromise), routes the fiat currency into crypto wallets, and subsequently uses local handlers to distribute physical cash to beneficiaries.
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
                          <h4 className="text-xl font-bold text-center text-white mb-1">Rakesh Sharma</h4>
                          <p className="text-center text-xs text-slate-400 mb-4">Alias: "Raka", "Boss"</p>
                          
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
                                <tr>
                                  <td className="p-2">2018</td>
                                  <td className="p-2 text-blue-400 cursor-pointer">FIR-2018-MUM-412</td>
                                  <td className="p-2">IPC 420 (Cheating), 467 (Forgery)</td>
                                  <td className="p-2"><span className="text-red-400">Convicted (Served 2 yrs)</span></td>
                                </tr>
                                <tr>
                                  <td className="p-2">2021</td>
                                  <td className="p-2 text-blue-400 cursor-pointer">FIR-2021-DEL-089</td>
                                  <td className="p-2">PMLA Sec 3 (Money Laundering)</td>
                                  <td className="p-2"><span className="text-amber-400">Acquitted (Lack of Evidence)</span></td>
                                </tr>
                                <tr>
                                  <td className="p-2">2023</td>
                                  <td className="p-2 text-blue-400 cursor-pointer">FIR-2023-UP-102</td>
                                  <td className="p-2">IPC 384 (Extortion), 120B</td>
                                  <td className="p-2"><span className="text-amber-400">Out on Bail</span></td>
                                </tr>
                              </tbody>
                            </table>
                          </div>
                          
                          <div className="mt-6 p-4 bg-red-500/10 border border-red-500/20 rounded text-sm">
                            <strong className="text-red-400 block mb-1">Criminology & Behavioral Note:</strong>
                            Subject demonstrates high financial literacy and avoids holding assets in his own name. Often uses rural proxies (Jamtara region) for initial fund collection. Demonstrates recidivism with escalating organizational complexity.
                          </div>
                        </div>
                      </div>
                    </div>

                  </div>
                </div>
              )}
"""
if "4. Master Criminal Dossier" not in content:
    content = content.replace("</>\\n              )}", "</>\\n              )}\n" + dossier_content)

# 3. Enhance the existing AI Link Explanation text to sound more "Criminology" focused
old_reason = "reasonText: 'The AI NLP engine extracted this direct connection from FIR-2026-DEL-001 where the suspect was mentioned utilizing this asset repeatedly during the operation.',"
new_reason = "reasonText: 'CRIMINOLOGY ANALYSIS: The AI NLP engine correlated this link by cross-referencing FIR-2026-DEL-001 with CCTNS historic records. The suspect (Rakesh Sharma) exhibits a known Modus Operandi (M.O.) of utilizing unregistered burner assets (like +91 9876543210) for short-term extortion calls. The linguistic pattern in the intercepted audio matches his known voice print from the 2018 conviction.',"
content = content.replace(old_reason, new_reason)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Criminology heavy details added.")
