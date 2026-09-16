import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_panel = """{/* Expandable Explain Link Panel (Bottom) */}
          <div className="h-48 bg-slate-900 border-t border-slate-800 shrink-0 p-4 overflow-y-auto">"""

new_panel = """{/* Expandable Explain Link Panel (Bottom) */}
          {activeMainTab === 'graph' && (
          <div className="h-48 bg-slate-900 border-t border-slate-800 shrink-0 p-4 overflow-y-auto">"""

content = content.replace(old_panel, new_panel)

# find the closing div of this panel, it's right before `{/* Side Panel (Right) - 400px fixed width */}`
content = content.replace(
    "            )}\n\n          </div>\n\n        </div>\n\n        {/* Side Panel (Right) - 400px fixed width */}",
    "            )}\n\n          </div>\n          )}\n\n        </div>\n\n        {/* Side Panel (Right) - 400px fixed width */}"
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("AI Panel hidden on non-graph tabs.")
