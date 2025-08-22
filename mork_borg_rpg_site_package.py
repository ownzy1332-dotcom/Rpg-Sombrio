import os

# Estrutura de pasta
folders = ['MorkBorgRPG', 'MorkBorgRPG/css', 'MorkBorgRPG/js']
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# index.html
index_html = """<!DOCTYPE html>
<html lang='pt-BR'>
<head>
  <meta charset='UTF-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <title>Mörk Borg RPG - Portal Sombrio</title>
  <link href='css/style.css' rel='stylesheet'>
</head>
<body>
  <header>
    <h1>Mörk Borg RPG</h1>
  </header>
  <main>
    <button onclick='generateCharacter()'>Gerar Personagem</button>
    <div id='characterSheet'></div>
  </main>
  <script src='js/scripts.js'></script>
</body>
</html>"""

with open('MorkBorgRPG/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# style.css
style_css = """body { background: #0a0a0a; color: #f5f5f5; font-family: 'Cinzel', serif; }
button { padding: 10px; background: #222; color: #f5f5f5; border-radius: 12px; }
"""
with open('MorkBorgRPG/css/style.css', 'w', encoding='utf-8') as f:
    f.write(style_css)

# scripts.js
scripts_js = """function generateCharacter() {
  document.getElementById('characterSheet').innerHTML = '<p>Personagem gerado: Sombrio...</p>';
}"""
with open('MorkBorgRPG/js/scripts.js', 'w', encoding='utf-8') as f:
    f.write(scripts_js)

print('Pasta MorkBorgRPG criada com index.html, css/style.css e js/scripts.js')
