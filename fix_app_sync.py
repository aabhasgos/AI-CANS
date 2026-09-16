import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\App.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_handle = """  const handleCreateNew = () => {
    const title = window.prompt("Enter new case title (e.g. 'Mumbai Cyber Fraud'):");
    if (title) {
      const newId = (cases.length + 1).toString();
      const updatedCases = [{
        id: newId,
        caseNumber: `FIR-2026-NEW-${Math.floor(Math.random() * 1000)}`,
        title: title,
        status: 'OPEN',
        entityCount: 0,
        createdAt: new Date().toISOString()
      }, ...cases];
      setCases(updatedCases);
      // Auto-navigate to the newly created case
      navigate(`/cases/${newId}`);
    }
  };"""

new_handle = """  const handleCreateNew = () => {
    const title = window.prompt("Enter new case title (e.g. 'Mumbai Cyber Fraud'):");
    if (title) {
      const newId = (cases.length + 1).toString();
      const updatedCases = [{
        id: newId,
        caseNumber: `FIR-2026-NEW-${Math.floor(Math.random() * 1000)}`,
        title: title,
        status: 'OPEN',
        entityCount: 0,
        createdAt: new Date().toISOString()
      }, ...cases];
      setCases(updatedCases);
      localStorage.setItem('ai_cnas_cases', JSON.stringify(updatedCases)); // Synchronous save to guarantee persistence before unmount
      // Auto-navigate to the newly created case
      navigate(`/cases/${newId}`);
    }
  };"""

content = content.replace(old_handle, new_handle)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("App.tsx new cases synchronous save fixed.")
