import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\IngestionPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to insert the button div right after the </div> that closes the table container.
# Let's use regex to find the end of the table div.
pattern = r"(</table>\s*</div>)"
replacement = r"""\1
              <div className="p-4 border-t border-slate-800 bg-slate-900/50 flex justify-end">
                <button 
                  onClick={() => navigate(`/cases/${caseId}`)} 
                  className="bg-blue-600 hover:bg-blue-500 text-white px-5 py-2.5 rounded-md shadow-lg transition-colors font-medium text-sm flex items-center gap-2"
                >
                  Open Case Workspace <ExternalLink className="w-4 h-4" />
                </button>
              </div>"""

new_content = re.sub(pattern, replacement, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Button successfully injected using regex.")
