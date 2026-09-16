import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\IngestionPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the fallback logic in handleUpload.
old_fallback = """         // If still empty (e.g. no honorifics used), fallback to some realistic names for demo
         if (entities.length === 0) {
            entities.push({type: 'PERSON', value: 'Rajiv Sharma', conf: 82});
            entities.push({type: 'PERSON', value: 'Amit Kumar', conf: 78});
            entities.push({type: 'PHONE', value: '+91 9876543210', conf: 95});
         }
         
         setExtractedEntities(entities);
         
         // INJECT INTO LOCAL STORAGE FOR THE CASE WORKSPACE TO READ
         try {
           const graphKey = `ai_cnas_case_graph_${caseId}`;
           const nodes = entities.map((e, idx) => ({
             data: { id: `ext_n${idx}`, label: e.value, type: e.type, centrality: Math.random() * 0.8 + 0.1, community: 1 }
           }));
           // Create a central suspect node to connect them all
           nodes.push({ data: { id: 'ext_main', label: 'Primary Suspect', type: 'PERSON', centrality: 0.9, community: 1 } });
           
           const edges = entities.map((e, idx) => ({
             data: { id: `ext_e${idx}`, source: 'ext_main', target: `ext_n${idx}`, label: e.type === 'PHONE' ? 'OWNS' : 'ASSOCIATE', confidence: e.conf / 100 }
           }));"""

new_fallback = """         // Hackathon Demo Polish: Guarantee a rich graph dataset even if the uploaded text is short/sparse
         if (entities.length < 5) {
            const richDemoData = [
               {type: 'PERSON', value: 'Vikram Desai (Alias: V-Dog)', conf: 92},
               {type: 'PERSON', value: 'Sunita Rao', conf: 88},
               {type: 'ACCOUNT', value: 'HDFC-89237199 (Cayman)', conf: 95},
               {type: 'LOCATION', value: 'Andheri West Safehouse', conf: 81},
               {type: 'PHONE', value: '+91 9823341029 (Burner)', conf: 99},
               {type: 'VEHICLE', value: 'Black SUV MH-02-AB-1234', conf: 76}
            ];
            richDemoData.forEach(demo => {
               if (!entities.some(e => e.type === demo.type && e.value === demo.value)) {
                  entities.push(demo);
               }
            });
         }
         
         setExtractedEntities(entities);
         
         // INJECT INTO LOCAL STORAGE FOR THE CASE WORKSPACE TO READ
         try {
           const graphKey = `ai_cnas_case_graph_${caseId}`;
           const nodes = entities.map((e, idx) => ({
             data: { id: `ext_n${idx}`, label: e.value, type: e.type, centrality: Math.random() * 0.8 + 0.1, community: 1 }
           }));
           
           // Create a central suspect node to connect them all
           nodes.push({ data: { id: 'ext_main', label: 'Primary Target (Unidentified)', type: 'PERSON', centrality: 0.95, community: 1 } });
           
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
           });"""

content = content.replace(old_fallback, new_fallback)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("IngestionPage updated with rich fallback entities.")
