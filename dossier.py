import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add state for expanding entity cards
if "expandedEntity" not in content:
    content = content.replace("const [activeSideTab", "const [expandedEntity, setExpandedEntity] = useState<string | null>('e1');\n  const [activeSideTab")

# 2. Replace the entities block with a rich police dossier block
old_entities_pattern = r"\{activeSideTab === 'entities' && \(\s*<div className=\"space-y-4\">.*?<\/div>\s*\)\}"

new_entities_block = """
            {activeSideTab === 'entities' && (
              <div className="space-y-4">
                <h3 className="text-sm font-semibold text-slate-300 uppercase tracking-wider mb-3">Top Suspects & Targets (AI Ranked)</h3>
                
                {/* PERSON DOSSIER */}
                <div 
                  onClick={() => setExpandedEntity(expandedEntity === 'e1' ? null : 'e1')}
                  className={`bg-slate-800 border transition-all cursor-pointer overflow-hidden ${expandedEntity === 'e1' ? 'border-blue-500 shadow-[0_0_15px_rgba(59,130,246,0.15)] rounded-lg' : 'border-slate-700 hover:border-slate-500 rounded-lg'} p-0`}
                >
                  <div className="p-3 flex justify-between items-start bg-slate-800/80">
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-red-500 shadow-[0_0_8px_rgba(239,68,68,0.8)]"></span>
                        <h4 className="font-bold text-slate-100 text-base tracking-wide">Rakesh Sharma</h4>
                      </div>
                      <p className="text-xs text-red-400 font-semibold mt-0.5 tracking-wider">TARGET: PRIMARY SUSPECT</p>
                    </div>
                    <span className="text-xs bg-red-500/20 text-red-400 border border-red-500/30 px-2 py-0.5 rounded font-mono">THREAT: HIGH</span>
                  </div>
                  
                  {expandedEntity === 'e1' && (
                    <div className="px-3 pb-3 pt-1 text-sm border-t border-slate-700 bg-slate-900/50">
                      <div className="grid grid-cols-2 gap-y-3 gap-x-2 mt-2">
                        <div>
                          <span className="text-[10px] text-slate-500 uppercase font-semibold">Known Aliases</span>
                          <p className="text-slate-300 text-xs">"Raka", "Boss"</p>
                        </div>
                        <div>
                          <span className="text-[10px] text-slate-500 uppercase font-semibold">Last Known Location</span>
                          <p className="text-slate-300 text-xs">Connaught Place, Delhi</p>
                        </div>
                        <div>
                          <span className="text-[10px] text-slate-500 uppercase font-semibold">Associated Cases</span>
                          <p className="text-blue-400 text-xs cursor-pointer hover:underline">FIR-2026-DEL-001</p>
                        </div>
                        <div>
                          <span className="text-[10px] text-slate-500 uppercase font-semibold">Centrality Score</span>
                          <p className="text-slate-300 text-xs font-mono">0.89 (Top 1%)</p>
                        </div>
                      </div>
                      <button className="w-full mt-4 bg-slate-800 hover:bg-slate-700 border border-slate-600 text-slate-200 text-xs py-1.5 rounded transition-colors">
                        View Full Intelligence Profile
                      </button>
                    </div>
                  )}
                </div>

                {/* PHONE DOSSIER */}
                <div 
                  onClick={() => setExpandedEntity(expandedEntity === 'e2' ? null : 'e2')}
                  className={`bg-slate-800 border transition-all cursor-pointer overflow-hidden ${expandedEntity === 'e2' ? 'border-blue-500 shadow-[0_0_15px_rgba(59,130,246,0.15)] rounded-lg' : 'border-slate-700 hover:border-slate-500 rounded-lg'} p-0`}
                >
                  <div className="p-3 flex justify-between items-start bg-slate-800/80">
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-blue-500 shadow-[0_0_8px_rgba(59,130,246,0.8)]"></span>
                        <h4 className="font-bold text-slate-100 text-base tracking-wide font-mono">+91 9876543210</h4>
                      </div>
                      <p className="text-xs text-blue-400 font-semibold mt-0.5 tracking-wider">TARGET: COMMUNICATION ASSET</p>
                    </div>
                    <span className="text-xs bg-blue-500/20 text-blue-400 border border-blue-500/30 px-2 py-0.5 rounded font-mono">ACTIVE PING</span>
                  </div>
                  
                  {expandedEntity === 'e2' && (
                    <div className="px-3 pb-3 pt-1 text-sm border-t border-slate-700 bg-slate-900/50">
                      <div className="grid grid-cols-2 gap-y-3 gap-x-2 mt-2">
                        <div>
                          <span className="text-[10px] text-slate-500 uppercase font-semibold">Telecom Carrier</span>
                          <p className="text-slate-300 text-xs">Jio / Airtel (India)</p>
                        </div>
                        <div>
                          <span className="text-[10px] text-slate-500 uppercase font-semibold">Registered KYC</span>
                          <p className="text-amber-400 text-xs">Fake ID (Flagged)</p>
                        </div>
                        <div>
                          <span className="text-[10px] text-slate-500 uppercase font-semibold">Last Cell Tower</span>
                          <p className="text-slate-300 text-xs">Sector 4, Noida</p>
                        </div>
                        <div>
                          <span className="text-[10px] text-slate-500 uppercase font-semibold">Linked Handset (IMEI)</span>
                          <p className="text-slate-300 text-xs font-mono">35102930192301</p>
                        </div>
                      </div>
                      <button className="w-full mt-4 bg-slate-800 hover:bg-slate-700 border border-slate-600 text-slate-200 text-xs py-1.5 rounded transition-colors">
                        Request CDR Subpoena
                      </button>
                    </div>
                  )}
                </div>

              </div>
            )}
"""

content = re.sub(old_entities_pattern, new_entities_block.strip(), content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Entities dossier upgraded.")
