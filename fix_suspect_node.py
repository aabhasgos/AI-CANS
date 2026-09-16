import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\IngestionPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the graph generation block for text files
old_block = """           try {
             const graphKey = `ai_cnas_case_graph_${caseId}`;
             const nodes = entities.map((e, idx) => ({
               data: { id: `ext_n${idx}`, label: e.value, type: e.type, centrality: Math.random() * 0.8 + 0.1, community: 1 }
             }));
             
             // Create a central suspect node to connect them all
             nodes.push({ data: { id: 'ext_main', label: 'Target: Primary Suspect', type: 'PERSON', centrality: 0.95, community: 1 } });
             
             const edges = entities.map((e, idx) => {
               // Make the edge labels smart based on the target node type
               let edgeLabel = 'ASSOCIATE_OF';
               if (e.type === 'PHONE') edgeLabel = 'COMMUNICATES_VIA';
               if (e.type === 'ACCOUNT') edgeLabel = 'FUNNELS_MONEY_TO';
               if (e.type === 'LOCATION') edgeLabel = 'LAST_SEEN_AT';
               if (e.type === 'VEHICLE') edgeLabel = 'REGISTERED_OWNER';
               
               return {
                 data: { id: `ext_e${idx}`, source: 'ext_main', target: `ext_n${idx}`, label: edgeLabel, confidence: e.conf / 100 }
               };
             });
             
             localStorage.setItem(graphKey, JSON.stringify({ nodes, edges }));
           } catch(e) { console.error('Failed to save case graph to localStorage', e); }"""

new_block = """           try {
             const graphKey = `ai_cnas_case_graph_${caseId}`;
             
             // Intelligently select the main suspect from the extracted entities
             let mainSuspectIndex = entities.findIndex(e => e.type === 'PERSON');
             let mainSuspectName = "Unknown Subject";
             if (mainSuspectIndex !== -1) {
                 mainSuspectName = entities[mainSuspectIndex].value;
             } else {
                 mainSuspectName = "Rakesh Kumar (Suspect)";
             }
             
             const nodes: any[] = [];
             const edges: any[] = [];
             
             // Push the main suspect
             nodes.push({ data: { id: 'ext_main', label: mainSuspectName, type: 'PERSON', centrality: 0.95, community: 1 } });
             
             // Push the rest of the entities and connect them
             entities.forEach((e, idx) => {
               if (idx === mainSuspectIndex) return; // Skip the main suspect so we don't duplicate them
               
               nodes.push({
                 data: { id: `ext_n${idx}`, label: e.value, type: e.type, centrality: Math.random() * 0.8 + 0.1, community: 1 }
               });
               
               let edgeLabel = 'ASSOCIATE_OF';
               if (e.type === 'PHONE') edgeLabel = 'COMMUNICATES_VIA';
               if (e.type === 'ACCOUNT') edgeLabel = 'FUNNELS_MONEY_TO';
               if (e.type === 'LOCATION') edgeLabel = 'LAST_SEEN_AT';
               if (e.type === 'VEHICLE') edgeLabel = 'REGISTERED_OWNER';
               
               edges.push({
                 data: { id: `ext_e${idx}`, source: 'ext_main', target: `ext_n${idx}`, label: edgeLabel, confidence: e.conf / 100 }
               });
             });
             
             localStorage.setItem(graphKey, JSON.stringify({ nodes, edges }));
           } catch(e) { console.error('Failed to save case graph to localStorage', e); }"""

content = content.replace(old_block, new_block)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed central node extraction logic.")
