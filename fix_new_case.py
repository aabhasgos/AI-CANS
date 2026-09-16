import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\App.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

cases_wrapper_old = """const CasesWrapper = () => {
  const navigate = useNavigate();
  const mockCases = [
    { id: '1', caseNumber: 'FIR-2026-DEL-001', title: 'Hawala Syndicate Crackdown', status: 'OPEN' as const, entityCount: 142, createdAt: '2026-08-30T10:00:00Z' },
    { id: '2', caseNumber: 'FIR-2026-BOM-084', title: 'Jamtara Phishing Ring', status: 'UNDER_REVIEW' as const, entityCount: 45, createdAt: '2026-08-31T14:30:00Z' },
    { id: '3', caseNumber: 'FIR-2026-RAJ-012', title: 'Cross Border Smuggling Route', status: 'CLOSED' as const, entityCount: 312, createdAt: '2026-08-15T09:15:00Z' }
  ];
  return <CaseList cases={mockCases} onCaseClick={(id) => navigate(`/cases/${id}`)} onCreateNew={() => {}} />;
};"""

cases_wrapper_new = """const CasesWrapper = () => {
  const navigate = useNavigate();
  const [cases, setCases] = React.useState([
    { id: '1', caseNumber: 'FIR-2026-DEL-001', title: 'Hawala Syndicate Crackdown', status: 'OPEN' as const, entityCount: 142, createdAt: '2026-08-30T10:00:00Z' },
    { id: '2', caseNumber: 'FIR-2026-BOM-084', title: 'Jamtara Phishing Ring', status: 'UNDER_REVIEW' as const, entityCount: 45, createdAt: '2026-08-31T14:30:00Z' },
    { id: '3', caseNumber: 'FIR-2026-RAJ-012', title: 'Cross Border Smuggling Route', status: 'CLOSED' as const, entityCount: 312, createdAt: '2026-08-15T09:15:00Z' }
  ]);

  const handleCreateNew = () => {
    const title = window.prompt("Enter new case title (e.g. 'Mumbai Cyber Fraud'):");
    if (title) {
      const newId = (cases.length + 1).toString();
      setCases([{
        id: newId,
        caseNumber: `FIR-2026-NEW-${Math.floor(Math.random() * 1000)}`,
        title: title,
        status: 'OPEN',
        entityCount: 0,
        createdAt: new Date().toISOString()
      }, ...cases]);
      alert("New case successfully registered in the CCTNS database!");
    }
  };

  return <CaseList cases={cases} onCaseClick={(id) => navigate(`/cases/${id}`)} onCreateNew={handleCreateNew} />;
};"""

content = content.replace(cases_wrapper_old.strip(), cases_wrapper_new.strip())

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Cases Wrapper updated.")
