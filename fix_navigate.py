import re

filepath = r"C:\Users\Sarvesh tiwari\Videos\SIH\frontend\src\pages\CasePage.tsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add import
if "import { useNavigate } from 'react-router-dom';" not in content:
    content = content.replace(
        "import { useParams } from 'react-router-dom';",
        "import { useParams, useNavigate } from 'react-router-dom';"
    )

# 2. Add hook declaration
if "const navigate = useNavigate();" not in content:
    content = content.replace(
        "const { id } = useParams<{ id: string }>();",
        "const { id } = useParams<{ id: string }>();\n  const navigate = useNavigate();"
    )

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("useNavigate added to CasePage.")
