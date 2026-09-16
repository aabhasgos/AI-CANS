import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\data\mockDatabase.ts"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"// Check if the ingestion page generated a graph for this specific case![\s\S]*?graph: graphData,\n\s*timeline: \[\],\n\s*map: \{ locations: \[\], connections: \[\] \},\n\s*evidence: \[\],\n\s*reason: graphData\.nodes\.length > 0 \? .*? : .*?\n\s*\};\n\};"

new_fallback = """// Check if the ingestion page generated a graph for this specific case!
    let timelineData: any[] = [];
    let mapData = { locations: [] as any[], connections: [] as any[] };
    let historyData: any[] = [];
    
    const savedGraph = localStorage.getItem(`ai_cnas_case_graph_${id}`);
    if (savedGraph) {
      graphData = JSON.parse(savedGraph);
      const mainNode = graphData.nodes.find((n: any) => n.data.id === 'ext_main');
      if (mainNode) primarySuspect = mainNode.data.label;
      
      // Auto-generate rich timeline based on the nodes
      graphData.nodes.forEach((n: any, idx: number) => {
        if (n.data.id === 'ext_main') return;
        
        let type = 'ENTITY';
        let title = `Entity Identified: ${n.data.label}`;
        if (n.data.type === 'PHONE') { type = 'COMMUNICATION'; title = `Intercepted Communication: ${n.data.label}`; }
        if (n.data.type === 'ACCOUNT') { type = 'TRANSACTION'; title = `Suspicious Transfer: ${n.data.label}`; }
        if (n.data.type === 'LOCATION') { type = 'LOCATION'; title = `Surveillance Ping: ${n.data.label}`; }
        
        timelineData.push({
          id: `t_${idx}`,
          date: `2026-08-${10 + (idx % 20)}`,
          type: type,
          title: title,
          description: `AI extraction pipeline confirmed linking of ${n.data.label} to primary target via NLP document processing.`,
          source: 'FIR Text Extraction'
        });
        
        // Auto-generate map pins for locations
        if (n.data.type === 'LOCATION') {
          mapData.locations.push({
            id: `loc_${idx}`,
            name: n.data.label,
            coordinates: [19.11 + (Math.random()*2), 72.84 + (Math.random()*2)],
            type: 'SAFEHOUSE',
            threat: 'HIGH'
          });
        }
      });
      
      // Auto-generate criminal history for the dossier
      historyData = [
        { year: '2024', fir: `FIR-2024-${id.slice(0, 3)}`, charges: 'Suspected Cyber Fraud / IPC 420', status: 'Under Investigation', color: 'text-amber-400' }
      ];
    }
  } catch(e) { console.error(e); }

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
      aliases: 'Identified via Extraction',
      threat: graphData.nodes.length > 0 ? 'HIGH' : 'UNKNOWN',
      location: mapData.locations.length > 0 ? mapData.locations[0].name : 'Unverified',
      centrality: graphData.nodes.length > 0 ? '0.85 (Top 5%)' : '0',
      carrier: 'Unknown',
      kyc: 'Flagged Identity',
      imei: 'Pending Trace',
      history: historyData,
      notes: graphData.nodes.length > 0 ? 'Primary suspect identified via automated entity resolution. Subject is heavily linked to offshore accounts and burner devices.' : 'No intelligence gathered yet. Process raw documents in the Ingestion tab to extract entities.'
    },
    graph: graphData,
    timeline: timelineData,
    map: mapData,
    evidence: [],
    reason: graphData.nodes.length > 0 ? 'AI detected strong topological correlations between extracted phone numbers, locations, and bank accounts in the uploaded document.' : 'Insufficient data. Please ingest documents to generate AI correlations.'
  };
};"""

content = re.sub(pattern, new_fallback, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("mockDatabase updated to auto-generate timeline, map, and dossier data.")
