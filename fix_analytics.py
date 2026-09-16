import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\AnalyticsPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add useNavigate hook if not present
if "const navigate = useNavigate();" not in content:
    content = content.replace("const AnalyticsPage: React.FC = () => {", "import { useNavigate } from 'react-router-dom';\n\nconst AnalyticsPage: React.FC = () => {\n  const navigate = useNavigate();")

# Fix buttons to use navigate
content = content.replace("onClick={() => window.location.href='/cases/1'}", "onClick={() => navigate('/cases/1')}")
content = content.replace("onClick={() => window.location.href='/cases/2'}", "onClick={() => navigate('/cases/2')}")

# Make "Chain of Command Depth" more detailed/perfect
old_chain = """<div className="bg-slate-900 border border-slate-800 rounded-lg p-5 flex flex-col justify-center">
            <h3 className="text-sm font-medium text-slate-400 mb-1">Chain of Command Depth</h3>
            <p className="text-3xl font-bold text-blue-400">3.4</p>
            <p className="text-xs text-slate-500 mt-2">Middle-men between street worker & boss</p>
          </div>"""

new_chain = """<div className="bg-slate-900 border border-slate-800 rounded-lg p-5 flex flex-col justify-between">
            <div>
              <h3 className="text-sm font-medium text-slate-400 mb-1">Chain of Command Depth</h3>
              <div className="flex items-end gap-3 mt-2">
                <p className="text-4xl font-bold text-blue-400">3.4</p>
                <p className="text-sm text-blue-500/80 font-medium mb-1 border border-blue-500/30 px-2 rounded bg-blue-500/10">Layers</p>
              </div>
            </div>
            <div className="mt-4 pt-4 border-t border-slate-800">
              <p className="text-xs text-slate-400">Average operational distance from street-level execution to the mastermind. <strong className="text-slate-300">Target isolation is HIGH.</strong> Requires minimum 3 flips to reach the top.</p>
            </div>
          </div>"""

content = content.replace(old_chain, new_chain)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Analytics page polished and routed.")
