import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\graph\ExplainLink.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add state to ExplainLink
if "const [viewerTarget, setViewerTarget]" not in content:
    content = content.replace(
        "export const ExplainLink: React.FC<ExplainLinkProps> = ({ data, isOpen, onClose }) => {",
        "export const ExplainLink: React.FC<ExplainLinkProps> = ({ data, isOpen, onClose }) => {\n  const [viewerTarget, setViewerTarget] = React.useState<string | null>(null);"
    )

# 2. Replace alerts with setViewerTarget
content = content.replace(
    "onClick={() => alert(`Accessing secure source document: ${src.name}`)}",
    "onClick={() => setViewerTarget(src.name)}"
)
content = content.replace(
    "onClick={() => alert(`Fetching classified record details for ${rec.type}...`)}",
    "onClick={() => setViewerTarget(rec.type + ' Data Record')}"
)

# 3. Add overlay
viewer_overlay = """
      {viewerTarget && (
        <div className="fixed inset-0 z-[110] flex items-center justify-center bg-slate-950/90 backdrop-blur-md p-4">
          <div className="bg-slate-900 border border-slate-700 rounded-xl shadow-[0_0_50px_rgba(0,0,0,0.8)] w-full max-w-3xl h-[60vh] flex flex-col overflow-hidden animate-in zoom-in-95 duration-200">
            <div className="h-12 bg-slate-800 border-b border-slate-700 flex items-center justify-between px-4 shrink-0">
              <div className="flex items-center gap-3">
                <ShieldAlert className="w-4 h-4 text-emerald-500" />
                <span className="font-mono text-xs text-emerald-400 font-bold uppercase tracking-wider">NATGRID Secure Terminal // {viewerTarget}</span>
              </div>
              <button onClick={(e) => { e.stopPropagation(); setViewerTarget(null); }} className="text-slate-400 hover:text-white transition-colors">
                <X className="w-5 h-5" />
              </button>
            </div>
            <div className="flex-1 bg-slate-950 p-6 overflow-auto font-mono text-sm text-emerald-500/90 flex flex-col gap-2">
              <p className="opacity-70">&gt; Establishing secure uplink to central intelligence grid...</p>
              <p className="opacity-70">&gt; Verifying access clearance... [APPROVED]</p>
              <p className="opacity-70">&gt; Fetching target node record: {viewerTarget}</p>
              <div className="mt-4 border border-emerald-500/20 bg-emerald-900/10 p-4 rounded text-emerald-400">
                <div className="animate-pulse flex items-center gap-2 mb-4">
                  <div className="w-2 h-2 bg-emerald-500 rounded-full"></div>
                  STREAMING CLASSIFIED DATA
                </div>
                <div className="w-full h-32 bg-slate-900 border border-slate-800 rounded flex items-center justify-center text-slate-600 opacity-50">
                  [DATA REDACTED FOR UNAUTHORIZED DISPLAY]
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
"""

content = content.replace("    </>\n  );\n};", viewer_overlay + "    </>\n  );\n};")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added Secure Viewer Overlay to ExplainLink.")
