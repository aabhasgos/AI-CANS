import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add the rename functionality
old_title_code = """        <div className="h-14 bg-slate-900 border-b border-slate-800 flex items-center justify-between px-4 shrink-0">
          <div className="flex items-center gap-4">
            <div className="text-slate-400 text-sm font-medium">CASE - 2024 - {id}</div>
            <h2 className="text-slate-200 font-bold">{caseData.title}</h2>
            <span className="px-2 py-0.5 bg-blue-500/20 text-blue-400 text-xs rounded border border-blue-500/30 font-medium">Active Investigation</span>
          </div>"""

new_title_code = """        <div className="h-14 bg-slate-900 border-b border-slate-800 flex items-center justify-between px-4 shrink-0">
          <div className="flex items-center gap-4">
            <div className="text-slate-400 text-sm font-medium">CASE-2026-{id?.slice(0,4)}</div>
            <h2 className="text-slate-200 font-bold flex items-center gap-2">
              {caseData.title}
              <button 
                onClick={() => {
                  const newTitle = window.prompt("Enter new name for this case:", caseData.title);
                  if (newTitle && newTitle !== caseData.title) {
                     try {
                        const saved = localStorage.getItem('ai_cnas_cases');
                        if (saved) {
                           let cases = JSON.parse(saved);
                           cases = cases.map((c: any) => c.id === id ? { ...c, title: newTitle } : c);
                           localStorage.setItem('ai_cnas_cases', JSON.stringify(cases));
                           window.location.reload(); // Quick refresh to update state
                        }
                     } catch(e) {}
                  }
                }}
                className="text-slate-500 hover:text-slate-300 transition-colors"
                title="Rename Case"
              >
                ✎
              </button>
            </h2>
            <span className="px-2 py-0.5 bg-blue-500/20 text-blue-400 text-xs rounded border border-blue-500/30 font-medium">Active Investigation</span>
          </div>"""

content = content.replace(old_title_code, new_title_code)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added rename functionality to CasePage.tsx.")
