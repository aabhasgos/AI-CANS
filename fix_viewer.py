import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add state for the viewer
if "const [viewerTarget, setViewerTarget]" not in content:
    content = content.replace(
        "const [activeSideTab, setActiveSideTab]",
        "const [viewerTarget, setViewerTarget] = useState<string | null>(null);\n  const [activeSideTab, setActiveSideTab]"
    )

# 2. Replace alerts with setViewerTarget in CasePage
content = content.replace(
    "onClick={() => alert(`Opening secure evidence viewer for: ${ev.name}`)}",
    "onClick={() => setViewerTarget(ev.name)}"
)

# 3. Add the Viewer Overlay component at the end of the return block, just before the closing </div>
viewer_overlay = """
      {/* Secure Evidence Viewer Overlay */}
      {viewerTarget && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center bg-slate-950/80 backdrop-blur-sm p-4">
          <div className="bg-slate-900 border border-slate-700 rounded-xl shadow-2xl w-full max-w-4xl h-[80vh] flex flex-col overflow-hidden animate-in fade-in zoom-in duration-200">
            <div className="h-12 bg-slate-800 border-b border-slate-700 flex items-center justify-between px-4 shrink-0">
              <div className="flex items-center gap-3">
                <ShieldAlert className="w-5 h-5 text-amber-500" />
                <span className="font-mono text-sm text-slate-200 font-medium">Classified Database Viewer - {viewerTarget}</span>
              </div>
              <button onClick={() => setViewerTarget(null)} className="text-slate-400 hover:text-white transition-colors bg-slate-700/50 hover:bg-slate-700 rounded p-1">
                <X className="w-5 h-5" />
              </button>
            </div>
            <div className="flex-1 bg-slate-950 p-6 overflow-auto font-mono text-sm text-green-500/80">
              <p className="mb-4 text-slate-400">Initializing secure connection to National Intelligence Grid...</p>
              <p className="mb-2 text-green-400">&gt; Authenticating badge ID: INSPECTOR-49281... [OK]</p>
              <p className="mb-2 text-green-400">&gt; Decrypting payload... [OK]</p>
              <p className="mb-6 text-green-400">&gt; Loading raw intelligence file: {viewerTarget}</p>
              
              <div className="border border-slate-800 bg-slate-900/50 p-4 rounded text-slate-300">
                <div className="flex justify-center items-center h-48 border-2 border-dashed border-slate-700 rounded mb-4 bg-slate-900">
                  <span className="text-slate-500 flex flex-col items-center gap-2">
                    <FileText className="w-8 h-8 opacity-50" />
                    [ENCRYPTED FILE STREAM RENDERED]
                  </span>
                </div>
                <p className="text-xs text-slate-500 leading-relaxed">
                  NOTE: This is a secure terminal emulation. Real documents cannot be downloaded to local unauthorized devices. 
                  All viewing activity is logged in the CCTNS audit trail.
                </p>
              </div>
            </div>
          </div>
        </div>
      )}
"""

content = content.replace("    </div>\n  );\n};\n\nexport default CasePage;", viewer_overlay + "    </div>\n  );\n};\n\nexport default CasePage;")

# Add X import if missing
if " X," not in content and "{ X," not in content:
    content = content.replace("import { Search,", "import { Search, X,")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added Secure Viewer Overlay to CasePage.")
