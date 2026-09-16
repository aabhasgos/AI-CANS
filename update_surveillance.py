import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\components\case\LiveSurveillance.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add props interface
old_header = """import React, { useState, useEffect } from 'react';
import { Camera, Scan, ShieldAlert, MapPin, CheckCircle, Crosshair } from 'lucide-react';

export const LiveSurveillance: React.FC = () => {"""

new_header = """import React, { useState, useEffect } from 'react';
import { Camera, Scan, ShieldAlert, MapPin, CheckCircle, Crosshair } from 'lucide-react';

interface LiveSurveillanceProps {
  caseData: any;
}

export const LiveSurveillance: React.FC<LiveSurveillanceProps> = ({ caseData }) => {"""

content = content.replace(old_header, new_header)

# Replace Rakesh Sharma with caseData.suspect.name
content = content.replace('TARGET ACQUIRED: Rakesh Sharma', 'TARGET ACQUIRED: {caseData.suspect.name || "Unknown Suspect"}')

# Replace Alias
content = content.replace('Alias: "Boss", "Raka"', 'Alias: {caseData.suspect.aliases || "None"}')

# Replace Case Title
content = content.replace('Hawala Syndicate Crackdown', '{caseData.title}')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated LiveSurveillance.tsx with caseData props.")
