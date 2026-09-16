import re
import os

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add imports at the top
import_str = """
import { NetworkGraph, GraphData } from '../components/graph/NetworkGraph';
import { ExplainLink } from '../components/graph/ExplainLink';
"""

if "import { NetworkGraph" not in content:
    content = content.replace("import { Search, Network,", import_str + "import { Search, Network,")

# 2. Add mock data for the graph right before the component declaration
mock_graph_data = """
const mockGraphData: GraphData = {
  nodes: [
    { data: { id: 'n1', label: 'Rakesh Sharma', type: 'PERSON', centrality: 0.9, community: 1 } },
    { data: { id: 'n2', label: '+91 9876543210', type: 'PHONE', centrality: 0.7, community: 1 } },
    { data: { id: 'n3', label: 'Mohit Kumar', type: 'PERSON', centrality: 0.6, community: 1 } },
    { data: { id: 'n4', label: 'Global Tech Solutions', type: 'ORGANIZATION', centrality: 0.5, community: 2 } },
    { data: { id: 'n5', label: 'Sanjay Khan', type: 'PERSON', centrality: 0.8, community: 2 } },
    { data: { id: 'n6', label: 'Connaught Place, Delhi', type: 'LOCATION', centrality: 0.4, community: 1 } },
  ],
  edges: [
    { data: { id: 'e1', source: 'n1', target: 'n2', label: 'OWNS', confidence: 0.95 } },
    { data: { id: 'e2', source: 'n3', target: 'n2', label: 'CALLED', confidence: 0.88 } },
    { data: { id: 'e3', source: 'n1', target: 'n4', label: 'DIRECTOR_OF', confidence: 0.99 } },
    { data: { id: 'e4', source: 'n5', target: 'n4', label: 'TRANSFERRED_FUNDS', confidence: 0.75 } },
    { data: { id: 'e5', source: 'n1', target: 'n6', label: 'ARRESTED_AT', confidence: 0.82 } },
  ]
};
"""

if "const mockGraphData" not in content:
    content = content.replace("const CasePage: React.FC = () => {", mock_graph_data + "\nconst CasePage: React.FC = () => {")

# 3. Replace the placeholder div with the actual components
placeholder_pattern = r"\{/\* Placeholder for Cytoscape Canvas \*/\}.*?</svg>\s*</div>\s*</div>"
replacement_graph = """
            <div className="absolute inset-0">
              <NetworkGraph 
                elements={mockGraphData} 
                onNodeSelect={(id, data) => setSelectedElement({type: 'node', id})}
                onEdgeSelect={(id, data) => setSelectedElement({type: 'edge', id})}
              />
            </div>
"""
content = re.sub(placeholder_pattern, replacement_graph, content, flags=re.DOTALL)

# 4. Replace the Explain Link Panel placeholder
explain_pattern = r"<div className=\"text-sm text-slate-400 italic\">Select an edge in the graph to see how these entities are connected across different data sources\.</div>"
replacement_explain = """
            {selectedElement.type === 'edge' ? (
              <ExplainLink 
                edgeId={selectedElement.id!}
                sourceName={mockGraphData.nodes.find(n => n.data.id === mockGraphData.edges.find(e => e.data.id === selectedElement.id)?.data.source)?.data.label || 'Unknown'}
                targetName={mockGraphData.nodes.find(n => n.data.id === mockGraphData.edges.find(e => e.data.id === selectedElement.id)?.data.target)?.data.label || 'Unknown'}
                relationshipType={mockGraphData.edges.find(e => e.data.id === selectedElement.id)?.data.label || 'LINKED_TO'}
                confidence={mockGraphData.edges.find(e => e.data.id === selectedElement.id)?.data.confidence || 0.5}
                evidence={[
                  {
                    id: 'ev1',
                    sourceId: 'doc-102',
                    sourceType: 'FIR',
                    title: 'FIR-2026-DEL-001',
                    snippet: `investigation revealed that the suspect used the phone number repeatedly to coordinate...`,
                    date: '2026-08-30'
                  }
                ]}
                onClose={() => setSelectedElement({type: null, id: null})}
              />
            ) : (
              <div className="text-sm text-slate-400 italic">Select an edge (line) in the graph above to see how these entities are connected across different data sources.</div>
            )}
"""
content = content.replace(
    '<div className="text-sm text-slate-400 italic">Select an edge in the graph to see how these entities are connected across different data sources.</div>',
    replacement_explain
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated CasePage.tsx to use real graph components.")
