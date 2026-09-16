import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"(<button\s+onClick=\{\(\) => \{\s+setIsGeneratingReport\(true\);)"

new_buttons = """<button 
              onClick={() => { setIsSaved(false); setTimeout(() => setIsSaved(true), 1000); }}
              className={`mr-2 px-3 py-1.5 border ${isSaved ? 'border-emerald-500/50 text-emerald-400 bg-emerald-500/10' : 'border-slate-600 text-slate-300 hover:bg-slate-700'} text-sm font-medium rounded-md transition-colors flex items-center gap-2`}
            >
              {isSaved ? <><CheckCircle2 className="w-4 h-4" /> Auto-Saved</> : <><Activity className="w-4 h-4 animate-spin" /> Saving...</>}
            </button>
            
            \\1"""

content = re.sub(pattern, new_buttons, content)

if "CheckCircle2" not in content:
    content = content.replace(
        "Search, X, Network, Clock, Map as MapIcon, ShieldAlert, Users, User, FileText, History, ZoomIn, Maximize, Activity",
        "Search, X, Network, Clock, Map as MapIcon, ShieldAlert, Users, User, FileText, History, ZoomIn, Maximize, Activity, CheckCircle2"
    )

# Fix the dossier tab crash issue.
# The dossier tab sets activeMainTab to 'dossier', but 'dossier' is not allowed in the type definition, nor does it render properly.
# Looking closely at CasePage.tsx, it seems dossier is meant to be a side tab, or maybe the main tab type is just missing 'dossier'.
# Let's fix the type definition for activeMainTab.
type_def = "const [activeMainTab, setActiveMainTab] = useState<'graph' | 'timeline' | 'map'>('graph');"
new_type_def = "const [activeMainTab, setActiveMainTab] = useState<'graph' | 'timeline' | 'map' | 'dossier'>('graph');"
content = content.replace(type_def, new_type_def)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected Save button and fixed dossier tab type.")
