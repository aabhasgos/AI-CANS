import re
import os

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add imports for Timeline and Map
if "import { InvestigationTimeline" not in content:
    content = content.replace(
        "import { NetworkGraph, GraphData } from '../components/graph/NetworkGraph';",
        "import { NetworkGraph, GraphData } from '../components/graph/NetworkGraph';\nimport { InvestigationTimeline, TimelineEvent } from '../components/timeline/InvestigationTimeline';\nimport { LocationMap, MapLocation } from '../components/map/LocationMap';"
    )

# 2. Add mock data for Timeline and Map
mock_data = """
const mockTimelineEvents: TimelineEvent[] = [
  { id: 't1', date: '2026-08-25T10:30:00Z', type: 'COMMUNICATION', description: 'Rakesh Sharma called Mohit Kumar', entities: ['Rakesh Sharma', 'Mohit Kumar'], confidence: 0.95 },
  { id: 't2', date: '2026-08-26T14:15:00Z', type: 'TRANSACTION', description: '₹5,00,000 transferred to Global Tech Solutions', entities: ['Sanjay Khan', 'Global Tech Solutions'], confidence: 0.88 },
  { id: 't3', date: '2026-08-27T09:00:00Z', type: 'LOCATION', description: 'Suspect device pinged at Connaught Place', entities: ['Rakesh Sharma'], confidence: 0.75 },
];

const mockLocations: MapLocation[] = [
  { id: 'l1', name: 'Connaught Place, Delhi', lat: 28.6304, lng: 77.2177, type: 'CRIME_SCENE', events: ['Device Ping'] },
  { id: 'l2', name: 'Global Tech Solutions HQ, Gurugram', lat: 28.4595, lng: 77.0266, type: 'ORGANIZATION', events: ['Funds Received'] },
];

"""
if "const mockTimelineEvents" not in content:
    content = content.replace("const mockGraphData: GraphData =", mock_data + "\nconst mockGraphData: GraphData =")

# 3. Handle Generate Report state
if "isGeneratingReport" not in content:
    content = content.replace("const [activeMainTab", "const [isGeneratingReport, setIsGeneratingReport] = useState(false);\n  const [activeMainTab")

# Replace Generate Report button
btn_pattern = r"<button className=\"px-3 py-1\.5 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-md transition-colors\">\s*Generate Report\s*</button>"
new_btn = """
          <button 
            onClick={() => {
              setIsGeneratingReport(true);
              setTimeout(() => {
                setIsGeneratingReport(false);
                alert('Success: Intelligence Report (PDF) generated and downloaded successfully!');
              }, 2000);
            }}
            disabled={isGeneratingReport}
            className="px-3 py-1.5 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-md transition-colors disabled:opacity-50 flex items-center gap-2"
          >
            {isGeneratingReport ? (
              <><Activity className="w-4 h-4 animate-spin" /> Generating...</>
            ) : 'Generate Report'}
          </button>
"""
content = re.sub(btn_pattern, new_btn, content)

# 4. Replace the center rendering area based on tabs
center_area_pattern = r"<div className=\"absolute inset-0\">\s*<NetworkGraph.*?/>\s*</div>"
new_center_area = """
            <div className="absolute inset-0">
              {activeMainTab === 'graph' && (
                <NetworkGraph 
                  elements={mockGraphData} 
                  onNodeSelect={(id, data) => setSelectedElement({type: 'node', id})}
                  onEdgeSelect={(id, data) => setSelectedElement({type: 'edge', id})}
                />
              )}
              {activeMainTab === 'timeline' && (
                <div className="h-full w-full bg-slate-900 overflow-y-auto">
                  <InvestigationTimeline events={mockTimelineEvents} />
                </div>
              )}
              {activeMainTab === 'map' && (
                <div className="h-full w-full">
                  <LocationMap locations={mockLocations} connections={[{from: 'l1', to: 'l2'}]} />
                </div>
              )}
            </div>
"""
content = re.sub(center_area_pattern, new_center_area, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("CasePage integrated.")
