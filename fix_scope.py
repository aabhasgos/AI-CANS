import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\data\mockDatabase.ts"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the block scoping issue by moving the declarations outside the try block
old_block = """  try {
    const saved = localStorage.getItem('ai_cnas_cases');
    if (saved) {
      const parsed = JSON.parse(saved);
      const found = parsed.find((c: any) => c.id === id);
      if (found) {
        title = found.title || title;
        if (found.assignedOfficer) leadIO = found.assignedOfficer;
      }
    }
    
    // Check if the ingestion page generated a graph for this specific case!
    let timelineData: any[] = [];
    let mapData = { locations: [] as any[], connections: [] as any[] };
    let historyData: any[] = [];"""

new_block = """  let timelineData: any[] = [];
  let mapData = { locations: [] as any[], connections: [] as any[] };
  let historyData: any[] = [];

  try {
    const saved = localStorage.getItem('ai_cnas_cases');
    if (saved) {
      const parsed = JSON.parse(saved);
      const found = parsed.find((c: any) => c.id === id);
      if (found) {
        title = found.title || title;
        if (found.assignedOfficer) leadIO = found.assignedOfficer;
      }
    }
    
    // Check if the ingestion page generated a graph for this specific case!"""

content = content.replace(old_block, new_block)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed scope issue in mockDatabase.ts")
