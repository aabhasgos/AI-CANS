import re
import os

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\layout\Header.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add useState import
if "useState" not in content:
    content = content.replace("import React from 'react';", "import React, { useState } from 'react';")

# Add state variables
if "const [searchQuery" not in content:
    content = content.replace("const navigate = useNavigate();", "const navigate = useNavigate();\n  const [searchQuery, setSearchQuery] = useState('');\n  const [isSearchOpen, setIsSearchOpen] = useState(false);")

# Update search input
search_pattern = r"<input\s*type=\"text\"\s*placeholder=\"CCTNS/ICJS Global Search.*?/>"
new_search = """
        <input
          type="text"
          value={searchQuery}
          onChange={(e) => {
            setSearchQuery(e.target.value);
            setIsSearchOpen(e.target.value.length > 0);
          }}
          onBlur={() => setTimeout(() => setIsSearchOpen(false), 200)}
          placeholder="CCTNS/ICJS Global Search (Entities, FIRs, Phone Numbers...)"
          className="w-full bg-slate-800 border border-slate-700 text-slate-200 text-sm rounded-md pl-10 pr-4 py-2 focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 placeholder-slate-500"
        />
        {isSearchOpen && (
          <div className="absolute top-full left-0 right-0 mt-1 bg-slate-800 border border-slate-700 rounded-md shadow-xl overflow-hidden z-50">
            <div className="p-2 text-xs font-semibold text-slate-400 uppercase tracking-wider bg-slate-900/50">Top Intelligence Results</div>
            <div className="p-3 hover:bg-slate-700 cursor-pointer flex items-center gap-3 border-b border-slate-700/50" onClick={() => navigate('/cases/1')}>
              <div className="w-8 h-8 rounded bg-blue-500/20 text-blue-400 flex items-center justify-center shrink-0">FIR</div>
              <div>
                <div className="text-sm font-medium text-slate-200">Hawala Syndicate Crackdown</div>
                <div className="text-xs text-slate-400">Match found in case description</div>
              </div>
            </div>
            <div className="p-3 hover:bg-slate-700 cursor-pointer flex items-center gap-3" onClick={() => navigate('/cases/1')}>
              <div className="w-8 h-8 rounded bg-red-500/20 text-red-400 flex items-center justify-center shrink-0">PER</div>
              <div>
                <div className="text-sm font-medium text-slate-200">Rakesh Sharma (Suspect)</div>
                <div className="text-xs text-slate-400">Match found in known aliases</div>
              </div>
            </div>
          </div>
        )}
"""
content = re.sub(search_pattern, new_search, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Header integrated.")
