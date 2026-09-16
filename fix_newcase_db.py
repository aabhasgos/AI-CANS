import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\data\mockDatabase.ts"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Change the default return logic to dynamically build an empty case if it's a new case ID.
old_return = "return db[id] || db['1'];"
new_return = """
  if (db[id]) return db[id];
  
  // If not found in static db, try to pull from localStorage to get the title
  let title = "New Investigation Case";
  try {
    const saved = localStorage.getItem('ai_cnas_cases');
    if (saved) {
      const parsed = JSON.parse(saved);
      const found = parsed.find((c: any) => c.id === id);
      if (found) title = found.title;
    }
  } catch(e) {}

  return {
    title: title,
    leadIO: 'Unassigned',
    jurisdiction: 'Pending Assignment',
    ipc: 'Under Review',
    summary: 'This is a newly registered case. Awaiting data ingestion (FIRs, CDRs) to populate intelligence network.',
    suspect: {
      name: 'Unknown Subject',
      aliases: 'None',
      threat: 'UNKNOWN',
      location: 'Unknown',
      centrality: '0',
      carrier: 'Unknown',
      kyc: 'Unknown',
      imei: 'Unknown',
      history: [],
      notes: 'No records available yet. Please upload evidence.'
    },
    graph: { nodes: [], edges: [] },
    timeline: [],
    map: { locations: [], connections: [] },
    evidence: [],
    reason: 'Insufficient data. Please ingest documents to generate AI correlations.'
  };
"""

content = content.replace(old_return, new_return)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("mockDatabase now supports dynamic new cases.")
