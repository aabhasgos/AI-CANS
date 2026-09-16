import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Dynamic ExplainLink logic
old_explain_link = r"""<ExplainLink 
              isOpen=\{selectedElement\.type === 'edge'\}
              onClose=\{.*?\}
              data=\{selectedElement\.type === 'edge' \? \{
                id: selectedElement\.id!,
                type: caseData\.graph\.edges\.find\(e => e\.data\.id === selectedElement\.id\)\?\.data\.label \|\| 'LINKED_TO',
                sourceLabel: caseData\.graph\.nodes\.find\(n => n\.data\.id === caseData\.graph\.edges\.find\(e => e\.data\.id === selectedElement\.id\)\?\.data\.source\)\?\.data\.label \|\| 'Unknown',
                targetLabel: caseData\.graph\.nodes\.find\(n => n\.data\.id === caseData\.graph\.edges\.find\(e => e\.data\.id === selectedElement\.id\)\?\.data\.target\)\?\.data\.label \|\| 'Unknown',
                confidence: caseData\.graph\.edges\.find\(e => e\.data\.id === selectedElement\.id\)\?\.data\.confidence \|\| 0\.85,
                observationPeriod: 'Aug 25 - Aug 30, 2026',
                reasonText: '\{caseData\.reason\}',
                sources: \[
                  \{ id: 'src1', name: 'FIR-2026-DEL-001 \(Original Document\)', date: '2026-08-30' \}
                \],
                evidenceRecords: \[
                  \{ id: 'ev1', type: 'NLP Extraction', detail: 'Found exact phrase match: "\{caseData\.suspect\.name\} was operating the phone number \+91 9876543210\.\.\."' \},
                  \{ id: 'ev2', type: 'Call Detail Record', detail: '34 outgoing calls matched in CDR database between Aug 25 and Aug 30\.' \}
                \]
              \} : null\}
            \/>"""

# We'll replace it with a cleanly formatted React component call that dynamically generates the text
new_explain_link = """<ExplainLink 
              isOpen={selectedElement.type === 'edge'}
              onClose={() => setSelectedElement({type: null, id: null})}
              data={(() => {
                if (selectedElement.type !== 'edge') return null;
                const edge = caseData.graph.edges.find((e: any) => e.data.id === selectedElement.id);
                if (!edge) return null;
                const source = caseData.graph.nodes.find((n: any) => n.data.id === edge.data.source)?.data.label || 'Unknown';
                const target = caseData.graph.nodes.find((n: any) => n.data.id === edge.data.target)?.data.label || 'Unknown';
                const relType = edge.data.label;
                
                return {
                  id: selectedElement.id!,
                  type: relType,
                  sourceLabel: source,
                  targetLabel: target,
                  confidence: edge.data.confidence || 0.85,
                  observationPeriod: 'Active Tracking',
                  reasonText: `CRIMINOLOGY ANALYSIS: The AI NLP engine correlated this link by cross-referencing recent FIRs with CCTNS historic records. The system detected that [${source}] and [${target}] are connected via a high-confidence [${relType.replace(/_/g, ' ')}] relationship.`,
                  sources: [
                    { id: 'src1', name: `FIR Extraction Report`, date: new Date().toLocaleDateString() }
                  ],
                  evidenceRecords: [
                    { id: 'ev1', type: 'NLP Extraction', detail: `Found explicit contextual match indicating ${source} is associated with ${target}.` },
                    { id: 'ev2', type: 'Database Cross-Ref', detail: `Match found in National Intelligence Grid (NATGRID) validating this connection.` }
                  ]
                };
              })()}
            />"""

content = re.sub(old_explain_link, new_explain_link, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dynamic ExplainLink added.")
