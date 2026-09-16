import re

filepath_app = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\App.tsx"

with open(filepath_app, 'r', encoding='utf-8') as f:
    app_content = f.read()

# Add handleDeleteCase
old_return_cases = "return <CaseList cases={cases} onCaseClick={(id) => navigate(`/cases/${id}`)} onCreateNew={handleCreateNew} />;"
new_return_cases = """  const handleDeleteCase = (id: string) => {
    if (window.confirm("Are you sure you want to completely delete this case? This action cannot be undone.")) {
      const updatedCases = cases.filter(c => c.id !== id);
      setCases(updatedCases);
      localStorage.setItem('ai_cnas_cases', JSON.stringify(updatedCases));
    }
  };

  return <CaseList cases={cases} onCaseClick={(id) => navigate(`/cases/${id}`)} onCreateNew={handleCreateNew} onDeleteCase={handleDeleteCase} />;"""

app_content = app_content.replace(old_return_cases, new_return_cases)

with open(filepath_app, 'w', encoding='utf-8') as f:
    f.write(app_content)


filepath_list = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\case\CaseList.tsx"
with open(filepath_list, 'r', encoding='utf-8') as f:
    list_content = f.read()

# Add onDeleteCase prop
list_content = list_content.replace(
    "import { Briefcase, Plus, FolderOpen, Calendar, Users } from 'lucide-react';",
    "import { Briefcase, Plus, FolderOpen, Calendar, Users, Trash2 } from 'lucide-react';"
)
list_content = list_content.replace(
    "onCreateNew: () => void;",
    "onCreateNew: () => void;\n  onDeleteCase?: (caseId: string) => void;"
)
list_content = list_content.replace(
    "export const CaseList: React.FC<CaseListProps> = ({ cases, onCaseClick, onCreateNew }) => {",
    "export const CaseList: React.FC<CaseListProps> = ({ cases, onCaseClick, onCreateNew, onDeleteCase }) => {"
)
list_content = list_content.replace(
    "<span className={`text-[10px] uppercase font-bold px-2 py-0.5 rounded border ${getStatusBadge(c.status)}`}>",
    """{onDeleteCase && (
                <button 
                  onClick={(e) => { e.stopPropagation(); onDeleteCase(c.id); }}
                  className="mr-2 text-slate-500 hover:text-red-500 transition-colors p-1"
                  title="Delete Case"
                >
                  <Trash2 size={14} />
                </button>
              )}
              <span className={`text-[10px] uppercase font-bold px-2 py-0.5 rounded border ${getStatusBadge(c.status)}`}>"""
)

with open(filepath_list, 'w', encoding='utf-8') as f:
    f.write(list_content)

print("Delete case functionality added.")
