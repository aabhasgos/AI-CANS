import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\AnalyticsPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add LocationMap import
if "import { LocationMap }" not in content:
    content = content.replace(
        "import { useNavigate } from 'react-router-dom';",
        "import { useNavigate } from 'react-router-dom';\nimport { LocationMap } from '../components/map/LocationMap';"
    )

# 2. Add global map data
map_data = """
const globalHotspots = [
  { id: '1', name: 'Delhi NCR Command Hub', lat: 28.6139, lng: 77.2090, type: 'headquarters', events: ['32 active overlapping cases', 'Primary Hawala route identified'] },
  { id: '2', name: 'Jamtara Operations Grid', lat: 23.9669, lng: 86.8046, type: 'operation', events: ['Phishing central', 'Abnormal high call volume'] },
  { id: '3', name: 'Mumbai Financial Node', lat: 19.0760, lng: 72.8777, type: 'financial', events: ['Corporate shell companies', 'Offshore money routing'] },
  { id: '4', name: 'Kolkata Transit Point', lat: 22.5726, lng: 88.3639, type: 'transit', events: ['Cross-border smuggling routes'] },
  { id: '5', name: 'Bengaluru Tech Node', lat: 12.9716, lng: 77.5946, type: 'tech', events: ['Crypto laundering identified', 'Server hosting'] }
];

const globalConnections = [
  { from: '1', to: '2' },
  { from: '1', to: '3' },
  { from: '3', to: '5' },
  { from: '4', to: '2' },
  { from: '1', to: '4' }
];

const AnalyticsPage: React.FC = () => {"""

content = content.replace("const AnalyticsPage: React.FC = () => {", map_data)

# 3. Replace the placeholder UI with the actual map
old_geospatial_block = r"\{activeTab === 'geospatial' && \(\s*<div className=\"bg-slate-900 border border-slate-800 rounded-lg p-10 text-center flex flex-col items-center justify-center min-h-\[400px\]\">.*?<\/div>\s*\)\}"

new_geospatial_block = """{activeTab === 'geospatial' && (
          <div className="bg-slate-900 border border-slate-800 rounded-lg overflow-hidden flex flex-col" style={{ height: '600px' }}>
            <div className="p-4 border-b border-slate-800 bg-slate-900 flex justify-between items-center z-10">
              <h3 className="text-slate-200 font-semibold flex items-center gap-2">
                <MapIcon className="w-5 h-5 text-blue-400" /> National Threat Map (Cross-Case Intersections)
              </h3>
              <div className="flex gap-2">
                <span className="px-2 py-1 bg-red-500/20 text-red-400 text-xs rounded border border-red-500/30">High Priority</span>
                <span className="px-2 py-1 bg-slate-800 text-slate-400 text-xs rounded border border-slate-700">Live Feed</span>
              </div>
            </div>
            <div className="flex-1 relative z-0">
              <LocationMap locations={globalHotspots} connections={globalConnections} />
            </div>
          </div>
        )}"""

content = re.sub(old_geospatial_block, new_geospatial_block, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected actual global LocationMap into Geospatial Hotspots tab.")
