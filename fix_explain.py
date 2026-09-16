import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# The incorrect code block I wrote earlier:
old_explain_block = """
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

new_explain_block = """
            <ExplainLink 
              isOpen={selectedElement.type === 'edge'}
              onClose={() => setSelectedElement({type: null, id: null})}
              data={selectedElement.type === 'edge' ? {
                id: selectedElement.id!,
                type: mockGraphData.edges.find(e => e.data.id === selectedElement.id)?.data.label || 'LINKED_TO',
                sourceLabel: mockGraphData.nodes.find(n => n.data.id === mockGraphData.edges.find(e => e.data.id === selectedElement.id)?.data.source)?.data.label || 'Unknown',
                targetLabel: mockGraphData.nodes.find(n => n.data.id === mockGraphData.edges.find(e => e.data.id === selectedElement.id)?.data.target)?.data.label || 'Unknown',
                confidence: mockGraphData.edges.find(e => e.data.id === selectedElement.id)?.data.confidence || 0.85,
                observationPeriod: 'Aug 25 - Aug 30, 2026',
                reasonText: 'The AI NLP engine extracted this direct connection from FIR-2026-DEL-001 where the suspect was mentioned utilizing this asset repeatedly during the operation.',
                sources: [
                  { id: 'src1', name: 'FIR-2026-DEL-001 (Original Document)', date: '2026-08-30' }
                ],
                evidenceRecords: [
                  { id: 'ev1', type: 'NLP Extraction', detail: 'Found exact phrase match: "Rakesh Sharma was operating the phone number +91 9876543210..."' },
                  { id: 'ev2', type: 'Call Detail Record', detail: '34 outgoing calls matched in CDR database between Aug 25 and Aug 30.' }
                ]
              } : null}
            />
            
            {selectedElement.type !== 'edge' && (
               <div className="text-sm text-slate-400 italic mt-2 p-4">Waiting for selection... click on any line between two circles in the network graph above to generate the AI report!</div>
            )}
"""

if "edgeId={selectedElement.id!}" in content:
    content = content.replace(old_explain_block.strip(), new_explain_block.strip())

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed ExplainLink props.")
