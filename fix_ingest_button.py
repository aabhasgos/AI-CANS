import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\IngestionPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add imports
if "useNavigate" not in content:
    content = content.replace(
        "import React, { useState, useRef, useEffect } from 'react';", 
        "import React, { useState, useRef, useEffect } from 'react';\nimport { useNavigate } from 'react-router-dom';"
    )

content = content.replace(
    "import { UploadCloud, FileText, CheckCircle2, AlertCircle, Loader2 } from 'lucide-react';",
    "import { UploadCloud, FileText, CheckCircle2, AlertCircle, Loader2, ExternalLink } from 'lucide-react';"
)

# 2. Add navigate hook
if "const navigate = useNavigate();" not in content:
    content = content.replace(
        "const [docType, setDocType] = useState('FIR');",
        "const navigate = useNavigate();\n  const [docType, setDocType] = useState('FIR');"
    )

# 3. Add the button footer
old_table_end = """                      ))}
                    </tbody>
                  </table>
                </div>"""

new_table_end = """                      ))}
                    </tbody>
                  </table>
                </div>
                <div className="p-4 border-t border-slate-800 bg-slate-900/50 flex justify-end">
                  <button 
                    onClick={() => navigate(`/cases/${caseId}`)} 
                    className="bg-blue-600 hover:bg-blue-500 text-white px-5 py-2.5 rounded-md shadow-lg transition-colors font-medium text-sm flex items-center gap-2"
                  >
                    Open Case Workspace <ExternalLink className="w-4 h-4" />
                  </button>
                </div>"""

content = content.replace(old_table_end, new_table_end)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added Open Case Workspace button to IngestionPage.")
