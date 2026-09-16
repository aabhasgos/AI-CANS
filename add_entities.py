import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Make caseData stateful
old_init = "const caseData = getCaseData(id || '1');"
new_init = """const initialData = getCaseData(id || '1');
  const [caseData, setCaseData] = useState(initialData);
  
  const handleAddEntity = () => {
    const name = window.prompt("Enter suspect/entity name:");
    if (!name) return;
    const type = window.prompt("Enter type (PERSON, PHONE, ACCOUNT, VEHICLE, LOCATION):", "PERSON") || "PERSON";
    
    const newNode = {
      data: { id: `manual-${Date.now()}`, label: name, type: type }
    };
    
    // Add to graph
    setCaseData({
      ...caseData,
      graph: {
        ...caseData.graph,
        nodes: [...caseData.graph.nodes, newNode]
      }
    });
    alert(`Successfully added ${name} to the intelligence graph!`);
  };"""

content = content.replace(old_init, new_init)

# Add the Add Entity button
old_suspects = """<h3 className="text-sm font-semibold text-slate-300 uppercase tracking-wider mb-3">Top Suspects & Targets (AI Ranked)</h3>"""
new_suspects = """<div className="flex justify-between items-center mb-3">
                  <h3 className="text-sm font-semibold text-slate-300 uppercase tracking-wider">Top Suspects & Targets</h3>
                  <button onClick={handleAddEntity} className="text-xs bg-slate-700 hover:bg-slate-600 px-2 py-1 rounded text-slate-200 transition-colors">+ Add Entity</button>
                </div>"""

content = content.replace(old_suspects, new_suspects)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Add Entity feature added to CasePage.")
