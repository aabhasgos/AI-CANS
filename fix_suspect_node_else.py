import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\IngestionPage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the else block for fake entities
pattern = r"nodes\.push\(\{ data: \{ id: 'ext_main', label: 'Target Entity', type: 'ORGANIZATION', centrality: 0\.9, community: 1 \} \}\);"
new_node = "nodes.push({ data: { id: 'ext_main', label: 'Suspected Shell Company', type: 'ORGANIZATION', centrality: 0.9, community: 1 } });"

content = re.sub(pattern, new_node, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed fake entity generation.")
