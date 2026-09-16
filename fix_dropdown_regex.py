import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\IngestionPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the select dropdown to actually call handleCreateCase when "NEW" is selected
pattern = r"<select\s+value=\{caseId\}\s+onChange=\{\(e\) => setCaseId\(e\.target\.value\)\}\s+className=\"w-full bg-slate-800 border border-slate-700 text-slate-200 rounded-md px-3 py-2 text-sm \n?focus:ring-1 focus:ring-blue-500 focus:outline-none\"\s*>[\s\S]*?</select>"

new_select = """<select 
                  value={caseId}
                  onChange={(e) => {
                    if (e.target.value === 'NEW') handleCreateCase();
                    else setCaseId(e.target.value);
                  }}
                  className="w-full bg-slate-800 border border-slate-700 text-slate-200 rounded-md px-3 py-2 text-sm focus:ring-1 focus:ring-blue-500 focus:outline-none"
                >
                  {availableCases.map(c => (
                    <option key={c.id} value={c.id}>{c.caseNumber}: {c.title}</option>
                  ))}
                  <option value="NEW" className="text-blue-400 font-bold">+ Create New Case & Save</option>
                </select>"""

content = re.sub(pattern, new_select, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed dropdown to actually call handleCreateCase and list available cases.")
