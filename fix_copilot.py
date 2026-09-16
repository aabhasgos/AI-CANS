import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\chat\AiCopilot.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_logic = """      if (lowerInput.includes('who') || lowerInput.includes('suspect') || lowerInput.includes('target')) {
        aiResponse = `Based on the Knowledge Graph centrality score, the primary target is **${caseData.suspect.name}**. They have the highest betweenness centrality (0.85), acting as the main bridge between the burner phones and the shell accounts.`;
      } 
      else if (lowerInput.includes('money') || lowerInput.includes('finance') || lowerInput.includes('account')) {
        aiResponse = `The financial trail shows layering. The entities extracted indicate funds are being moved through suspected shell accounts before hitting the primary target's network. I recommend generating a financial subpoena.`;
      }
      else if (lowerInput.includes('location') || lowerInput.includes('where')) {
        aiResponse = `Geospatial correlation shows the highest density of activity near **${caseData.suspect.location}**. This aligns with the intercepted burner phone pings.`;
      }
      else if (lowerInput.includes('summary') || lowerInput.includes('summarize')) {
        aiResponse = caseData.summary || `This case involves ${caseData.graph?.nodes?.length || 0} extracted entities. The AI has flagged a high-threat cluster around ${caseData.suspect.name}.`;
      }
      else {
        aiResponse = `I have cross-referenced that query against the extracted FIR and CDR data. While there's no direct match in the graph, I suggest we run a deep-scan on the secondary aliases linked to ${caseData.suspect.name}.`;
      }"""

new_logic = """      // Smarter simulated Graph RAG logic
      const nodes = caseData.graph?.nodes || [];
      const edges = caseData.graph?.edges || [];
      
      // Look for specific node mentions in the user's input
      const mentionedNodes = nodes.filter((n: any) => lowerInput.includes(n.data.label.toLowerCase()));
      
      if (mentionedNodes.length > 0) {
        // Dynamic graph query simulation
        const n = mentionedNodes[0];
        const connectedEdges = edges.filter((e: any) => e.data.source === n.data.id || e.data.target === n.data.id);
        const connectedCount = connectedEdges.length;
        
        if (mentionedNodes.length > 1) {
           aiResponse = `Analyzing the subgraph... I found direct topological connections between **${mentionedNodes[0].data.label}** and **${mentionedNodes[1].data.label}**. They are bridged through a common communication/financial node with a high confidence score.`;
        } else if (lowerInput.includes('alias') || lowerInput.includes('secondary')) {
           aiResponse = `Running entity resolution... **${n.data.label}** has been matched against the ICJS database. Possible aliases include known variations from historical FIRs, operating primarily out of ${caseData.suspect.location || 'their last known location'}.`;
        } else {
           aiResponse = `**${n.data.label}** is a ${n.data.type} node in this network with a centrality score of ${n.data.centrality?.toFixed(2) || 0.5}. It is directly linked to ${connectedCount} other entities in the extracted FIR data.`;
        }
      } 
      else if (lowerInput.includes('who') || lowerInput.includes('suspect') || lowerInput.includes('target')) {
        aiResponse = `Based on the Knowledge Graph centrality score, the primary target is **${caseData.suspect?.name || 'Unidentified'}**. They act as the main bridge between the burner phones and the shell accounts.`;
      } 
      else if (lowerInput.includes('money') || lowerInput.includes('finance') || lowerInput.includes('account') || lowerInput.includes('bank')) {
        aiResponse = `The financial trail shows layering. The entities extracted indicate funds are being moved through suspected shell accounts before hitting the primary target's network. I recommend generating a financial subpoena.`;
      }
      else if (lowerInput.includes('location') || lowerInput.includes('where')) {
        aiResponse = `Geospatial correlation shows the highest density of activity near **${caseData.suspect?.location || 'Unverified'}**. This aligns with the intercepted burner phone pings.`;
      }
      else if (lowerInput.includes('summary') || lowerInput.includes('summarize')) {
        aiResponse = caseData.summary || `This case involves ${nodes.length} extracted entities. The AI has flagged a high-threat cluster around ${caseData.suspect?.name || 'the primary target'}.`;
      }
      else if (lowerInput.includes('alias') || lowerInput.includes('name')) {
        aiResponse = `The primary aliases extracted from the raw documents for the main suspect include: ${caseData.suspect?.aliases || 'Unknown'}.`;
      }
      else {
        // Fallback that actually sounds intelligent and uses case data context
        const randomNode = nodes.length > 0 ? nodes[Math.floor(Math.random() * nodes.length)].data.label : 'various entities';
        aiResponse = `I've analyzed the semantic relationships. While that specific query doesn't perfectly match a node, the AI found strong correlations between **${randomNode}** and the primary suspect. I recommend reviewing the Master Dossier for further links.`;
      }"""

content = content.replace(old_logic, new_logic)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated AiCopilot.tsx with smarter simulated Graph RAG logic.")
