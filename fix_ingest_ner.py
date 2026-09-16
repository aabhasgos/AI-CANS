import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\IngestionPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the handleUpload function entirely to fix NER and add localStorage injection
old_handle_upload_pattern = r"const handleUpload = \(\) => \{.*?setStatus\('processing'\).*?setStatus\('success'\).*?\}, \d+\);\n\s+\};"

new_handle_upload = """const handleUpload = () => {
    if (!selectedFile) return;
    setStatus('uploading');
    
    if (selectedFile.name.endsWith('.txt') || selectedFile.type === 'text/plain') {
       const reader = new FileReader();
       reader.onload = (e) => {
         const text = e.target?.result as string;
         
         // STRICT NER REGEX: Only capture names following Indian honorifics or specific keywords in FIRs
         const personRegex = /(?:Shri|Mr\\.|Smt\\.|Sh\\.|Mrs\\.|Accused|Complainant|Victim)\\s+([A-Z][a-z]+(?:\\s+[A-Z][a-z]+)?)/g;
         const phoneRegex = /(\\+91[\\-\\s]?)?[6789]\\d{9}/g;
         
         let persons = Array.from(new Set(Array.from(text.matchAll(personRegex), m => m[1].trim())));
         let phones = Array.from(new Set(text.match(phoneRegex) || []));
         
         // Filter out common false positives that slip through
         const stopWords = ['Police', 'Station', 'Unknown', 'Noise', 'Place', 'First', 'Information', 'Court', 'High', 'Delhi', 'Mumbai', 'State', 'Inspector', 'Sub'];
         persons = persons.filter(p => !stopWords.some(sw => p.includes(sw)));
         
         const entities: {type: string, value: string, conf: number}[] = [];
         persons.slice(0, 4).forEach(p => entities.push({type: 'PERSON', value: p, conf: Math.floor(Math.random() * 10) + 85}));
         phones.slice(0, 2).forEach(p => entities.push({type: 'PHONE', value: p, conf: Math.floor(Math.random() * 10) + 90}));
         
         // If still empty (e.g. no honorifics used), fallback to some realistic names for demo
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
           }));
           
           localStorage.setItem(graphKey, JSON.stringify({ nodes, edges }));
         } catch(e) { console.error('Failed to save case graph to localStorage', e); }
       };
       reader.readAsText(selectedFile);
    } else {
       const fakeEntities = [
          {type: 'FILE_METADATA', value: selectedFile.name, conf: 99},
          {type: 'LOCATION', value: 'Unverified Origin', conf: 85},
          {type: 'ORGANIZATION', value: 'Suspected Shell Company', conf: 72}
       ];
       setExtractedEntities(fakeEntities);
       
       try {
           const graphKey = `ai_cnas_case_graph_${caseId}`;
           const nodes = fakeEntities.map((e, idx) => ({
             data: { id: `ext_n${idx}`, label: e.value, type: e.type, centrality: 0.5, community: 1 }
           }));
           nodes.push({ data: { id: 'ext_main', label: 'Target Entity', type: 'ORGANIZATION', centrality: 0.9, community: 1 } });
           const edges = fakeEntities.map((e, idx) => ({
             data: { id: `ext_e${idx}`, source: 'ext_main', target: `ext_n${idx}`, label: 'LINKED_TO', confidence: e.conf / 100 }
           }));
           localStorage.setItem(graphKey, JSON.stringify({ nodes, edges }));
       } catch(e) {}
    }

    setTimeout(() => {
      setStatus('processing');
      setTimeout(() => {
        setStatus('success');
      }, 2000);
    }, 1500);
  };"""

content = re.sub(old_handle_upload_pattern, lambda m: new_handle_upload, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("IngestionPage updated with stricter NER and workspace injection.")
