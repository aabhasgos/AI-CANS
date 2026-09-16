import glob

for f in glob.glob('frontend/src/**/*.tsx', recursive=True):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace \$ or similar weird escapes
        if r'\${' in content:
            print(f'Fixing syntax in {f}')
            content = content.replace(r'\${', '${')
            
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
    except Exception as e:
        pass
