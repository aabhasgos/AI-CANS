import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

evidence_block_old = r"""<div className="bg-slate-800 border border-slate-700 hover:border-slate-500 cursor-pointer rounded-lg p-3 transition-colors">.*?<button className="w-full py-2 bg-slate-800 hover:bg-slate-700 border border-slate-600 border-dashed rounded text-sm text-slate-300 font-medium transition-colors">
                  \+ Upload More Evidence
                <\/button>"""

evidence_block_new = """{caseData.evidence?.map((ev: any) => (
                  <div key={ev.id} onClick={() => alert(`Opening secure evidence viewer for: ${ev.name}`)} className="bg-slate-800 border border-slate-700 hover:border-slate-500 cursor-pointer rounded-lg p-3 transition-colors">
                    <div className="flex items-center gap-3">
                      <div className={`w-10 h-10 rounded flex items-center justify-center shrink-0 ${ev.type === 'cdr' ? 'bg-amber-500/20 text-amber-400' : ev.type === 'media' ? 'bg-purple-500/20 text-purple-400' : 'bg-blue-500/20 text-blue-400'}`}>
                        {ev.type === 'cdr' ? <Activity size={20} /> : <FileText size={20} />}
                      </div>
                      <div>
                        <h4 className="font-medium text-slate-200 text-sm truncate w-48">{ev.name}</h4>
                        <p className="text-xs text-slate-500 mt-0.5">Uploaded {ev.date}</p>
                      </div>
                    </div>
                    <div className="mt-3 flex gap-2">
                      <span className="text-[10px] uppercase bg-slate-900 px-2 py-1 rounded border border-slate-700 text-emerald-400">{ev.entities} Entities Extracted</span>
                    </div>
                  </div>
                ))}
                
                <button onClick={() => window.location.href='/ingest'} className="w-full py-2 bg-slate-800 hover:bg-slate-700 border border-slate-600 border-dashed rounded text-sm text-slate-300 font-medium transition-colors">
                  + Upload More Evidence
                </button>"""

content = re.sub(evidence_block_old, evidence_block_new, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Evidence tab made dynamic.")
