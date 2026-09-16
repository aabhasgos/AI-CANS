import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Import
import_str = "import { LiveSurveillance } from '../components/case/LiveSurveillance';"
if import_str not in content:
    content = content.replace("import { AiCopilot } from '../components/chat/AiCopilot';", "import { AiCopilot } from '../components/chat/AiCopilot';\n" + import_str)

# 2. Update strict type of activeMainTab if exists, but we can just use strings
# Search for activeMainTab state
if "'graph' | 'timeline' | 'map' | 'dossier'" in content:
    content = content.replace("'graph' | 'timeline' | 'map' | 'dossier'", "'graph' | 'timeline' | 'map' | 'dossier' | 'surveillance'")

# 3. Add the 5th tab button in the header nav
tab_buttons = """                  <button 
                    onClick={() => setActiveMainTab('dossier')}
                    className={`px-6 py-4 text-sm font-medium border-b-2 flex flex-col items-center gap-1 transition-colors ${
                      activeMainTab === 'dossier' 
                        ? 'border-blue-500 text-blue-400' 
                        : 'border-transparent text-slate-400 hover:text-slate-300 hover:border-slate-700'
                    }`}
                  >
                    <div className="flex items-center gap-2">
                      <FileText className="w-4 h-4" /> 4. Master Criminal Dossier & Case Details
                    </div>
                  </button>
                </nav>"""

new_tab_buttons = """                  <button 
                    onClick={() => setActiveMainTab('dossier')}
                    className={`px-6 py-4 text-sm font-medium border-b-2 flex flex-col items-center gap-1 transition-colors ${
                      activeMainTab === 'dossier' 
                        ? 'border-blue-500 text-blue-400' 
                        : 'border-transparent text-slate-400 hover:text-slate-300 hover:border-slate-700'
                    }`}
                  >
                    <div className="flex items-center gap-2">
                      <FileText className="w-4 h-4" /> 4. Master Criminal Dossier
                    </div>
                  </button>
                  <button 
                    onClick={() => setActiveMainTab('surveillance')}
                    className={`px-6 py-4 text-sm font-medium border-b-2 flex flex-col items-center gap-1 transition-colors ${
                      activeMainTab === 'surveillance' 
                        ? 'border-red-500 text-red-400' 
                        : 'border-transparent text-slate-400 hover:text-slate-300 hover:border-slate-700'
                    }`}
                  >
                    <div className="flex items-center gap-2">
                      <Camera className="w-4 h-4" /> 5. Live Surveillance
                    </div>
                  </button>
                </nav>"""

content = content.replace(tab_buttons, new_tab_buttons)
# Check if Camera is imported from lucide-react. If not, add it.
if "Camera" not in content[:500]:
    content = content.replace("import { Network, Search, AlertCircle, FileText, Database, Shield, BrainCircuit, Activity, Clock, Map, Filter, Download, Maximize2, Minimize2, RefreshCw, ZoomIn, ZoomOut, User, Users, MapPin, Smartphone, ShieldAlert } from 'lucide-react';", 
    "import { Network, Search, AlertCircle, FileText, Database, Shield, BrainCircuit, Activity, Clock, Map, Filter, Download, Maximize2, Minimize2, RefreshCw, ZoomIn, ZoomOut, User, Users, MapPin, Smartphone, ShieldAlert, Camera } from 'lucide-react';")

# 4. Render LiveSurveillance
render_logic = """              {activeMainTab === 'dossier' && (
                <div className="h-full w-full overflow-y-auto bg-slate-900">
                  <div className="max-w-5xl mx-auto p-6">"""

new_render_logic = """              {activeMainTab === 'surveillance' && (
                <LiveSurveillance />
              )}
              {activeMainTab === 'dossier' && (
                <div className="h-full w-full overflow-y-auto bg-slate-900">
                  <div className="max-w-5xl mx-auto p-6">"""

content = content.replace(render_logic, new_render_logic)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected LiveSurveillance tab into CasePage.tsx.")
