import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the duplicate let declarations
duplicate_block = """                const sourceType = caseData.graph.nodes.find((n: any) => n.data.id === edge.data.source)?.data.type || 'ENTITY';
                const targetType = caseData.graph.nodes.find((n: any) => n.data.id === edge.data.target)?.data.type || 'ENTITY';
                
                let reasonText = "";
                let evidence1 = "";
                let evidence2 = "";"""

fixed_block = """                const sourceType = caseData.graph.nodes.find((n: any) => n.data.id === edge.data.source)?.data.type || 'ENTITY';
                const targetType = caseData.graph.nodes.find((n: any) => n.data.id === edge.data.target)?.data.type || 'ENTITY';"""

content = content.replace(duplicate_block, fixed_block)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Duplicate declarations removed.")
