import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add useEffect to CasePage to handle route changes
old_init = """const initialData = getCaseData(id || '1');
  const [caseData, setCaseData] = useState(initialData);"""

new_init = """const initialData = getCaseData(id || '1');
  const [caseData, setCaseData] = useState(initialData);
  
  React.useEffect(() => {
    setCaseData(getCaseData(id || '1'));
  }, [id]);"""

# Need to make sure React is available. I'll just use React.useEffect.
content = content.replace(old_init, new_init)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added useEffect to CasePage.")
