import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# The specific block to look for:
pattern = r"(<FileText className=\"w-4 h-4\" /> 4\. Master Criminal Dossier & Case Details\s*</button>)"

replacement = r"""\1
              
              <button 
                onClick={() => setActiveMainTab('surveillance')}
                className={`flex items-center gap-2 px-4 py-2.5 text-sm font-medium border-b-2 transition-colors ${activeMainTab === 'surveillance' ? 'border-red-500 text-red-400' : 'border-transparent text-slate-400 hover:text-slate-200'}`}
              >
                <Camera className="w-4 h-4" /> 5. Live Surveillance
              </button>"""

content = re.sub(pattern, replacement, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected 5th tab button!")
