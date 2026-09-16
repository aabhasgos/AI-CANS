import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\layout\Header.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add state for notifications dropdown
if "isNotificationsOpen" not in content:
    content = content.replace("const [isSearchOpen", "const [isNotificationsOpen, setIsNotificationsOpen] = useState(false);\n  const [isSearchOpen")

# 2. Update the Bell button to toggle the dropdown
bell_button_pattern = r"<button className=\"p-2 hover:bg-slate-800 rounded-full relative\">\s*<Bell className=\"w-5 h-5 text-slate-400\" \/>\s*<span className=\"absolute top-1\.5 right-1\.5 w-2 h-2 bg-red-500 rounded-full border border-slate-900\"><\/span>\s*<\/button>"

new_bell_button = """
        <div className="relative">
          <button 
            onClick={() => setIsNotificationsOpen(!isNotificationsOpen)}
            onBlur={() => setTimeout(() => setIsNotificationsOpen(false), 200)}
            className="p-2 hover:bg-slate-800 rounded-full relative focus:outline-none"
          >
            <Bell className="w-5 h-5 text-slate-400" />
            <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-red-500 rounded-full border border-slate-900 animate-pulse"></span>
          </button>
          
          {isNotificationsOpen && (
            <div className="absolute top-full right-0 mt-2 w-80 bg-slate-800 border border-slate-700 rounded-md shadow-2xl overflow-hidden z-50">
              <div className="p-3 border-b border-slate-700 bg-slate-900/80 flex justify-between items-center">
                <span className="text-sm font-semibold text-slate-200">System Alerts</span>
                <span className="text-xs text-blue-400 cursor-pointer">Mark all read</span>
              </div>
              <div className="max-h-80 overflow-y-auto">
                <div className="p-3 border-b border-slate-700/50 hover:bg-slate-700 cursor-pointer bg-slate-800">
                  <div className="flex items-center gap-2 mb-1">
                    <span className="w-2 h-2 rounded-full bg-red-500"></span>
                    <span className="text-xs font-bold text-red-400">CRITICAL MATCH</span>
                  </div>
                  <p className="text-sm text-slate-200">CCTNS Database match found for suspect "Rakesh Sharma" in pending FIR.</p>
                  <span className="text-xs text-slate-500 mt-1 block">Just now</span>
                </div>
                <div className="p-3 border-b border-slate-700/50 hover:bg-slate-700 cursor-pointer">
                  <div className="flex items-center gap-2 mb-1">
                    <span className="w-2 h-2 rounded-full bg-amber-500"></span>
                    <span className="text-xs font-bold text-amber-400">GEO-FENCE ALERT</span>
                  </div>
                  <p className="text-sm text-slate-300">Target handset (+91 9876543210) pinged outside active jurisdiction (Delhi).</p>
                  <span className="text-xs text-slate-500 mt-1 block">45 mins ago</span>
                </div>
                <div className="p-3 hover:bg-slate-700 cursor-pointer">
                  <div className="flex items-center gap-2 mb-1">
                    <span className="w-2 h-2 rounded-full bg-blue-500"></span>
                    <span className="text-xs font-bold text-blue-400">SYSTEM</span>
                  </div>
                  <p className="text-sm text-slate-300">Daily intelligence digest compiled successfully.</p>
                  <span className="text-xs text-slate-500 mt-1 block">2 hours ago</span>
                </div>
              </div>
            </div>
          )}
        </div>
"""

content = re.sub(bell_button_pattern, new_bell_button.strip(), content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Notifications wired.")
