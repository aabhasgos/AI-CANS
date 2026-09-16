import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\IngestionPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add state to fetch cases from localStorage
old_states = """  const [file, setFile] = useState<File | null>(null);
  const [caseId, setCaseId] = useState('CASE-2024-102');
  const [docType, setDocType] = useState('FIR');
  const [status, setStatus] = useState<'IDLE' | 'UPLOADING' | 'PROCESSING' | 'SUCCESS' | 'ERROR'>('IDLE');
  const [entities, setEntities] = useState<string[]>([]);"""

new_states = """  const [file, setFile] = useState<File | null>(null);
  const [docType, setDocType] = useState('FIR');
  const [status, setStatus] = useState<'IDLE' | 'UPLOADING' | 'PROCESSING' | 'SUCCESS' | 'ERROR'>('IDLE');
  const [entities, setEntities] = useState<string[]>([]);
  
  const [savedCases, setSavedCases] = useState<any[]>([]);
  const [caseId, setCaseId] = useState('');

  React.useEffect(() => {
    const casesData = localStorage.getItem('ai_cnas_cases');
    if (casesData) {
      const parsed = JSON.parse(casesData);
      setSavedCases(parsed);
      if (parsed.length > 0) setCaseId(parsed[0].id);
    } else {
      // Fallback defaults if localStorage is empty
      const fallback = [
        { id: '1', title: 'Hawala Syndicate Crackdown' },
        { id: '2', title: 'Jamtara Phishing Ring' }
      ];
      setSavedCases(fallback);
      setCaseId('1');
    }
  }, []);"""
content = content.replace(old_states, new_states)

# 2. Replace hardcoded select options
old_select = """                <select 
                  value={caseId}
                  onChange={(e) => setCaseId(e.target.value)}
                  className="w-full bg-slate-800 border border-slate-700 text-slate-200 rounded-md px-3 py-2 text-sm focus:ring-1 focus:ring-blue-500 focus:outline-none"
                >
                  <option value="CASE-2024-102">CASE-2024-102: Hawala Syndicate Crackdown</option>
                  <option value="CASE-2024-098">CASE-2024-098: Jamtara Phishing Ring</option>
                  <option value="NEW">+ Create New Case</option>
                </select>"""

new_select = """                <select 
                  value={caseId}
                  onChange={(e) => setCaseId(e.target.value)}
                  className="w-full bg-slate-800 border border-slate-700 text-slate-200 rounded-md px-3 py-2 text-sm focus:ring-1 focus:ring-blue-500 focus:outline-none"
                >
                  {savedCases.map((c) => (
                    <option key={c.id} value={c.id}>Case {c.id}: {c.title}</option>
                  ))}
                  <option value="NEW">+ Create New Case</option>
                </select>"""
content = content.replace(old_select, new_select)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("IngestionPage dynamically loads cases from localStorage.")
