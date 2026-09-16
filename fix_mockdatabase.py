import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\data\mockDatabase.ts"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the fallback block for new cases
old_fallback = """  if (db[id]) return db[id];
  
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
      carrier: 'N/A',
      kyc: 'N/A',
      imei: 'N/A',
      history: [],
      notes: 'No intelligence gathered yet. Process raw documents in the Ingestion tab to extract entities.'
    },
    graph: {
      nodes: [],
      edges: []
    }
  };"""

new_fallback = """  if (db[id]) return db[id];
  
  // If not found in static db, try to pull from localStorage to get the title
  let title = "New Investigation Case";
  let leadIO = "Unassigned";
  let graphData = { nodes: [] as any[], edges: [] as any[] };
  let primarySuspect = 'Unknown Subject';
  
  try {
    const saved = localStorage.getItem('ai_cnas_cases');
    if (saved) {
      const parsed = JSON.parse(saved);
      const found = parsed.find((c: any) => c.id === id);
      if (found) {
        title = found.title;
        if (found.assignedOfficer) leadIO = found.assignedOfficer;
      }
    }
    
    // Check if the ingestion page generated a graph for this specific case!
    const savedGraph = localStorage.getItem(`ai_cnas_case_graph_${id}`);
    if (savedGraph) {
      graphData = JSON.parse(savedGraph);
      const mainNode = graphData.nodes.find((n: any) => n.data.id === 'ext_main');
      if (mainNode) primarySuspect = mainNode.data.label;
    }
  } catch(e) {}

  return {
    title: title,
    leadIO: leadIO,
    jurisdiction: 'State Police / Cyber Cell',
    ipc: 'Under Review',
    summary: graphData.nodes.length > 0 
      ? `Intelligence network automatically generated via NLP extraction from uploaded documents. Currently tracking ${graphData.nodes.length} entities.`
      : 'This is a newly registered case. Awaiting data ingestion (FIRs, CDRs) to populate intelligence network.',
    suspect: {
      name: primarySuspect,
      aliases: 'None',
      threat: graphData.nodes.length > 0 ? 'MODERATE' : 'UNKNOWN',
      location: 'Unverified',
      centrality: graphData.nodes.length > 0 ? '0.75' : '0',
      carrier: 'Unknown',
      kyc: 'Pending Verification',
      imei: 'Unknown',
      history: [],
      notes: graphData.nodes.length > 0 ? 'Entities successfully extracted and graphed via Data Ingestion pipeline.' : 'No intelligence gathered yet. Process raw documents in the Ingestion tab to extract entities.'
    },
    graph: graphData
  };"""

content = content.replace(old_fallback, new_fallback)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("mockDatabase updated to serve localStorage graphs for dynamic cases.")
