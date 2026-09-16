import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\Dashboard.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add the 'Assigned Officer' display and state update logic
old_expanded_row = """                          <div className="bg-slate-800/80 p-4 rounded-lg border border-slate-700 flex flex-col gap-3">
                            <div>
                              <span className="font-semibold text-slate-100">Case Registered:</span> {new Date(c.createdAt || Date.now()).toLocaleDateString()}
                            </div>
                            <div>
                              <span className="font-semibold text-slate-100">Brief Summary:</span> Investigation into {c.title.toLowerCase()}. {c.entityCount || 0} entities currently tracked by the system.
                            </div>
                            <div className="flex gap-4 mt-2">
                              <button onClick={() => navigate(`/cases/${c.id}`)} className="bg-blue-600 hover:bg-blue-500 text-white px-4 py-1.5 rounded shadow transition-colors font-medium text-xs">Open Case Workspace</button>
                              <button onClick={() => {
                                const officer = window.prompt("Enter Officer Name or Badge ID to assign to this case:");
                                if (officer) {
                                  alert(`Successfully assigned ${officer} to ${c.title}. The audit log has been updated.`);
                                }
                              }} className="bg-slate-700 hover:bg-slate-600 text-white px-4 py-1.5 rounded border border-slate-500 transition-colors font-medium text-xs">Assign Officer</button>
                            </div>
                          </div>"""

new_expanded_row = """                          <div className="bg-slate-800/80 p-4 rounded-lg border border-slate-700 flex flex-col gap-3">
                            <div className="grid grid-cols-2 gap-4">
                              <div>
                                <span className="font-semibold text-slate-100">Case Registered:</span> {new Date(c.createdAt || Date.now()).toLocaleDateString()}
                              </div>
                              <div>
                                <span className="font-semibold text-slate-100">Lead Officer:</span> {c.assignedOfficer ? <span className="text-emerald-400 font-medium">{c.assignedOfficer}</span> : <span className="text-amber-500/80 italic">Unassigned</span>}
                              </div>
                            </div>
                            <div>
                              <span className="font-semibold text-slate-100">Brief Summary:</span> Investigation into {c.title.toLowerCase()}. {c.entityCount || 0} entities currently tracked by the system.
                            </div>
                            <div className="flex gap-4 mt-2">
                              <button onClick={() => navigate(`/cases/${c.id}`)} className="bg-blue-600 hover:bg-blue-500 text-white px-4 py-1.5 rounded shadow transition-colors font-medium text-xs">Open Case Workspace</button>
                              <button onClick={() => {
                                const officer = window.prompt("Enter Officer Name or Badge ID to assign to this case:");
                                if (officer) {
                                  // Update state and localStorage
                                  const updatedCases = recentCases.map(caseItem => 
                                    caseItem.id === c.id ? { ...caseItem, assignedOfficer: officer } : caseItem
                                  );
                                  setRecentCases(updatedCases);
                                  localStorage.setItem('ai_cnas_cases', JSON.stringify(updatedCases));
                                  alert(`Successfully assigned ${officer} to ${c.title}. The audit log has been updated.`);
                                }
                              }} className="bg-slate-700 hover:bg-slate-600 text-white px-4 py-1.5 rounded border border-slate-500 transition-colors font-medium text-xs">
                                {c.assignedOfficer ? 'Reassign Officer' : 'Assign Officer'}
                              </button>
                            </div>
                          </div>"""

content = content.replace(old_expanded_row, new_expanded_row)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dashboard assigned officer UI injected.")
