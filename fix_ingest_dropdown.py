import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\IngestionPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Make the Target Case dropdown dynamic and able to create/name new cases properly
old_dropdown_state = "const [caseId, setCaseId] = useState('CASE-2024-102');"
new_dropdown_state = """const [caseId, setCaseId] = useState('1');
  const [availableCases, setAvailableCases] = useState<any[]>([]);

  useEffect(() => {
    const saved = localStorage.getItem('ai_cnas_cases');
    if (saved) {
      const parsed = JSON.parse(saved);
      setAvailableCases(parsed);
      if (parsed.length > 0) setCaseId(parsed[0].id);
    } else {
      const defaultCases = [
        { id: '1', caseNumber: 'FIR-2026-DEL-001', title: 'Hawala Syndicate Crackdown', status: 'OPEN' },
        { id: '2', caseNumber: 'FIR-2026-BOM-084', title: 'Jamtara Phishing Ring', status: 'UNDER_REVIEW' }
      ];
      setAvailableCases(defaultCases);
      setCaseId('1');
    }
  }, []);

  const handleCreateCase = () => {
    const title = window.prompt("Enter the name for the new case (e.g. 'Mumbai Cyber Fraud'):");
    if (title) {
      const newId = Date.now().toString();
      const newCase = {
        id: newId,
        caseNumber: `FIR-2026-NEW-${Math.floor(Math.random() * 1000)}`,
        title: title,
        status: 'OPEN',
        createdAt: new Date().toISOString(),
        entityCount: 0
      };
      const updatedCases = [newCase, ...availableCases];
      setAvailableCases(updatedCases);
      setCaseId(newId);
      localStorage.setItem('ai_cnas_cases', JSON.stringify(updatedCases));
      alert(`Successfully created and saved case: ${title}. You can now process documents into it.`);
    }
  };"""

if "const [availableCases" not in content:
    content = content.replace(old_dropdown_state, new_dropdown_state)

# Replace the actual select HTML
old_select = """                <select 
                  className="w-full bg-slate-900 border border-slate-700 text-slate-200 rounded-md py-2 px-3 focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
                  value={caseId}
                  onChange={(e) => setCaseId(e.target.value)}
                >
                  <option value="CASE-2024-102">CASE 2024 102: Hawala Syndicate Crackdown</option>
                  <option value="CASE-2024-098">CASE 2024 098: Jamtara Phishing Ring</option>
                  <option value="NEW">+ Create New Case Workspace</option>
                </select>"""

new_select = """                <select 
                  className="w-full bg-slate-900 border border-slate-700 text-slate-200 rounded-md py-2 px-3 focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
                  value={caseId}
                  onChange={(e) => {
                    if (e.target.value === 'NEW') handleCreateCase();
                    else setCaseId(e.target.value);
                  }}
                >
                  {availableCases.map(c => (
                    <option key={c.id} value={c.id}>{c.caseNumber}: {c.title}</option>
                  ))}
                  <option value="NEW" className="text-blue-400 font-bold">+ Create New Case & Save</option>
                </select>"""

if "{availableCases.map" not in content:
    content = content.replace(old_select, new_select)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("IngestionPage dropdown made dynamic.")
