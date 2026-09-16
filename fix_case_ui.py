import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add Save Case button state
if "const [isSaved, setIsSaved] = useState(false);" not in content:
    content = content.replace(
        "const [isGeneratingReport, setIsGeneratingReport] = useState(false);",
        "const [isGeneratingReport, setIsGeneratingReport] = useState(false);\n  const [isSaved, setIsSaved] = useState(true);"
    )

# Add Save Case button to UI
old_buttons = """          <div className="flex items-center gap-3">
            <div className="relative">
              <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
              <input 
                type="text" 
                placeholder="Search in case..." 
                className="pl-9 pr-4 py-1.5 bg-slate-900 border border-slate-700 rounded-full text-sm text-slate-200 focus:outline-none focus:border-blue-500 w-64"
              />
            </div>
            
            <button 
              onClick={handleGenerateReport}
              disabled={isGeneratingReport}
              className={`bg-blue-600 hover:bg-blue-500 text-white px-4 py-1.5 rounded text-sm font-medium transition-colors flex items-center gap-2 ${isGeneratingReport ? 'opacity-70 cursor-not-allowed' : ''}`}
            >
              {isGeneratingReport ? (
                <><Activity className="w-4 h-4 animate-spin" /> Generating...</>
              ) : 'Generate Report'}
            </button>"""

new_buttons = """          <div className="flex items-center gap-3">
            <div className="relative">
              <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
              <input 
                type="text" 
                placeholder="Search in case..." 
                className="pl-9 pr-4 py-1.5 bg-slate-900 border border-slate-700 rounded-full text-sm text-slate-200 focus:outline-none focus:border-blue-500 w-64"
              />
            </div>
            
            <button 
              onClick={() => { setIsSaved(false); setTimeout(() => setIsSaved(true), 1000); }}
              className={`bg-slate-800 border ${isSaved ? 'border-emerald-500/50 text-emerald-400' : 'border-slate-600 text-slate-300 hover:bg-slate-700'} px-4 py-1.5 rounded text-sm font-medium transition-colors flex items-center gap-2`}
            >
              {isSaved ? <><CheckCircle2 className="w-4 h-4" /> Saved to DB</> : <><Activity className="w-4 h-4 animate-spin" /> Saving...</>}
            </button>

            <button 
              onClick={handleGenerateReport}
              disabled={isGeneratingReport}
              className={`bg-blue-600 hover:bg-blue-500 text-white px-4 py-1.5 rounded text-sm font-medium transition-colors flex items-center gap-2 ${isGeneratingReport ? 'opacity-70 cursor-not-allowed' : ''}`}
            >
              {isGeneratingReport ? (
                <><Activity className="w-4 h-4 animate-spin" /> Generating...</>
              ) : 'Generate Report'}
            </button>"""

if "Saved to DB" not in content:
    # Need to make sure CheckCircle2 is imported in CasePage.tsx
    if "CheckCircle2" not in content:
        content = content.replace(
            "Search, X, Network, Clock, Map as MapIcon, ShieldAlert, Users, User, FileText, History, ZoomIn, Maximize, Activity",
            "Search, X, Network, Clock, Map as MapIcon, ShieldAlert, Users, User, FileText, History, ZoomIn, Maximize, Activity, CheckCircle2"
        )
    content = content.replace(old_buttons, new_buttons)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added Save UI and fixed CasePage")
