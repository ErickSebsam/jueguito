from pathlib import Path
from string import Template

root = Path(r"c:\Users\amaya\Music\2026\Profe Alex\2025\jueguito\personajes")

font_block = """
  <!-- IMPORTACIÓN DE FUENTES TEMÁTICAS (Google Fonts) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Cinzel:wght@600;700;800&family=Rajdhani:wght@600;700&display=swap" rel="stylesheet">
"""

styles = {
    'aatrox.html': {
        'body_bg': '#0a0a0f',
        'sidebar_start': '#120101',
        'sidebar_end': '#2b0000',
        'border': 'rgba(255, 0, 0, 0.2)',
        'title_color': '#ff4b4b',
        'char_bg': '#3d0a0a',
        'char_hover': 'rgba(255, 75, 75, 0.25)',
        'accent_color': 'rgba(255, 75, 75, 0.5)',
        'panel_start': '#1a0000',
        'panel_end': '#2e0000',
        'panel_border': 'rgba(255, 0, 0, 0.2)',
        'stat_start': '#ff0000',
        'stat_end': '#ff4b1f',
        'button_start': '#ff0000',
        'button_end': '#ff4b1f',
        'button_hover_start': '#ff2b2b',
        'button_hover_end': '#ff6a3d',
        'button_shadow': 'rgba(255, 0, 0, 0.5)',
        'description_border': '#ff4b4b',
    },
    'mordekaiser.html': {
        'body_bg': '#06040a',
        'sidebar_start': '#0d0217',
        'sidebar_end': '#1f0638',
        'border': 'rgba(180, 100, 255, 0.15)',
        'title_color': '#c5a6ff',
        'char_bg': '#231338',
        'char_hover': 'rgba(180, 120, 255, 0.25)',
        'accent_color': 'rgba(180, 120, 255, 0.5)',
        'panel_start': '#150d27',
        'panel_end': '#2c1f46',
        'panel_border': 'rgba(180, 100, 255, 0.2)',
        'stat_start': '#7b3eff',
        'stat_end': '#b874ff',
        'button_start': '#7b3eff',
        'button_end': '#b874ff',
        'button_hover_start': '#b874ff',
        'button_hover_end': '#e0baff',
        'button_shadow': 'rgba(150, 80, 255, 0.5)',
        'description_border': '#b874ff',
    },
    'viego.html': {
        'body_bg': '#050102',
        'sidebar_start': '#0d0203',
        'sidebar_end': '#2e0509',
        'border': 'rgba(255, 42, 42, 0.3)',
        'title_color': '#ff3b3b',
        'char_bg': '#1a0507',
        'char_hover': 'rgba(255, 42, 42, 0.3)',
        'accent_color': 'rgba(255, 60, 0, 0.6)',
        'panel_start': '#120304',
        'panel_end': '#33070b',
        'panel_border': 'rgba(255, 42, 42, 0.3)',
        'stat_start': '#ff003c',
        'stat_end': '#ffae00',
        'button_start': '#ff003c',
        'button_end': '#ff8c00',
        'button_hover_start': '#ff1a40',
        'button_hover_end': '#ffae00',
        'button_shadow': 'rgba(255, 50, 0, 0.6)',
        'description_border': '#ff3b3b',
    },
    # REVISADO: REDISEÑO COMPLETO PARA ZED (Estilo Sombras y Acero Jonio)
    'zed.html': {
        'body_bg': '#050508',
        'sidebar_start': '#0a0a0f',
        'sidebar_end': '#1c0509',
        'border': 'rgba(255, 42, 42, 0.25)',
        'title_color': '#e6b800', # Dorado metálico
        'char_bg': '#18070a',
        'char_hover': 'rgba(255, 42, 42, 0.3)',
        'accent_color': 'rgba(255, 42, 42, 0.5)',
        'panel_start': '#0c080e',
        'panel_end': '#21080d',
        'panel_border': 'rgba(255, 42, 42, 0.25)',
        'stat_start': '#cc0000',
        'stat_end': '#ff4d4d',
        'button_start': '#990000',
        'button_end': '#e60000',
        'button_hover_start': '#cc0000',
        'button_hover_end': '#ff3333',
        'button_shadow': 'rgba(255, 0, 0, 0.6)',
        'description_border': '#ff2a2a',
    },
    # REVISADO: REDISEÑO COMPLETO PARA SHYVANA (Estilo Ruina / Esmeralda)
    'shyvana.html': {
        'body_bg': '#020b08',
        'sidebar_start': '#03140e',
        'sidebar_end': '#0a2e23',
        'border': 'rgba(0, 255, 170, 0.25)',
        'title_color': '#00ffaa',
        'char_bg': '#07241b',
        'char_hover': 'rgba(0, 255, 170, 0.25)',
        'accent_color': 'rgba(0, 255, 170, 0.5)',
        'panel_start': '#041711',
        'panel_end': '#0c382b',
        'panel_border': 'rgba(0, 255, 170, 0.25)',
        'stat_start': '#00b377',
        'stat_end': '#00ffaa',
        'button_start': '#008055',
        'button_end': '#00cc88',
        'button_hover_start': '#00cc88',
        'button_hover_end': '#33ffbb',
        'button_shadow': 'rgba(0, 255, 170, 0.5)',
        'description_border': '#00ffaa',
    },
    'Ashe.html': {
        'body_bg': '#07121a',
        'sidebar_start': '#0b1630',
        'sidebar_end': '#05101b',
        'border': 'rgba(80, 180, 255, 0.2)',
        'title_color': '#8fd7ff',
        'char_bg': '#17304a',
        'char_hover': 'rgba(143, 215, 255, 0.2)',
        'accent_color': 'rgba(143, 215, 255, 0.5)',
        'panel_start': '#091828',
        'panel_end': '#102b42',
        'panel_border': 'rgba(80, 180, 255, 0.2)',
        'stat_start': '#74cbff',
        'stat_end': '#5aaee0',
        'button_start': '#3a82b8',
        'button_end': '#559ad6',
        'button_hover_start': '#559ad6',
        'button_hover_end': '#8fd7ff',
        'button_shadow': 'rgba(80, 180, 255, 0.5)',
        'description_border': '#74cbff',
    },
    'Ezreal.html': {
        'body_bg': '#071119',
        'sidebar_start': '#0b1630',
        'sidebar_end': '#05101c',
        'border': 'rgba(0, 210, 255, 0.2)',
        'title_color': '#5fd7ff',
        'char_bg': '#0c2d44',
        'char_hover': 'rgba(95, 215, 255, 0.2)',
        'accent_color': 'rgba(95, 215, 255, 0.5)',
        'panel_start': '#081727',
        'panel_end': '#10283d',
        'panel_border': 'rgba(0, 210, 255, 0.2)',
        'stat_start': '#5fd7ff',
        'stat_end': '#46b6ff',
        'button_start': '#0088cc',
        'button_end': '#00c0ff',
        'button_hover_start': '#00c0ff',
        'button_hover_end': '#5fd7ff',
        'button_shadow': 'rgba(0, 210, 255, 0.5)',
        'description_border': '#5fd7ff',
    },
    'Garen.html': {
        'body_bg': '#071025',
        'sidebar_start': '#08163d',
        'sidebar_end': '#06204f',
        'border': 'rgba(100, 170, 255, 0.2)',
        'title_color': '#80b8ff',
        'char_bg': '#17335e',
        'char_hover': 'rgba(100, 170, 255, 0.25)',
        'accent_color': 'rgba(100, 170, 255, 0.5)',
        'panel_start': '#081a3b',
        'panel_end': '#0f305c',
        'panel_border': 'rgba(100, 170, 255, 0.2)',
        'stat_start': '#4a8bff',
        'stat_end': '#7fbfff',
        'button_start': '#2562d9',
        'button_end': '#4a8bff',
        'button_hover_start': '#4a8bff',
        'button_hover_end': '#80b8ff',
        'button_shadow': 'rgba(100, 170, 255, 0.5)',
        'description_border': '#80b8ff',
    },
    'Kayle.html': {
        'body_bg': '#100d13',
        'sidebar_start': '#15101a',
        'sidebar_end': '#2a1f2d',
        'border': 'rgba(255, 210, 120, 0.2)',
        'title_color': '#ffd77f',
        'char_bg': '#3a321d',
        'char_hover': 'rgba(255, 215, 127, 0.25)',
        'accent_color': 'rgba(255, 215, 127, 0.5)',
        'panel_start': '#171116',
        'panel_end': '#2e221c',
        'panel_border': 'rgba(255, 210, 120, 0.2)',
        'stat_start': '#ffd77f',
        'stat_end': '#ffeab8',
        'button_start': '#d4a337',
        'button_end': '#ffd77f',
        'button_hover_start': '#ffd77f',
        'button_hover_end': '#fff1c5',
        'button_shadow': 'rgba(255, 210, 120, 0.5)',
        'description_border': '#ffd77f',
    },
    'Teemo.html': {
        'body_bg': '#1b091f',
        'sidebar_start': '#2a0b20',
        'sidebar_end': '#5e1f45',
        'border': 'rgba(255, 190, 255, 0.2)',
        'title_color': '#ffbaf8',
        'char_bg': '#4a1538',
        'char_hover': 'rgba(255, 186, 248, 0.25)',
        'accent_color': 'rgba(255, 186, 248, 0.5)',
        'panel_start': '#370a28',
        'panel_end': '#5f1b4a',
        'panel_border': 'rgba(255, 190, 255, 0.2)',
        'stat_start': '#ffbaf8',
        'stat_end': '#ff8fe6',
        'button_start': '#b84299',
        'button_end': '#ff66d4',
        'button_hover_start': '#ff66d4',
        'button_hover_end': '#ffbaf8',
        'button_shadow': 'rgba(255, 190, 255, 0.5)',
        'description_border': '#ffbaf8',
    },
}

base = Template('''
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      height: 100vh;
      display: flex;
      background-color: $body_bg;
      color: white;
      font-family: 'Rajdhani', sans-serif;
      overflow: hidden;
    }

    /* --- SIDEBAR --- */
    .sidebar {
      width: 18%;
      background: linear-gradient(180deg, $sidebar_start, $sidebar_end);
      border-right: 2px solid $border;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      padding: 3rem 0 2rem 0;
    }

    .sidebar h2 {
      margin-top: 0.5rem;
      margin-bottom: 2rem;
      font-size: 1.5rem;
      font-family: 'Cinzel Decorative', serif;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 3px;
      color: $title_color;
      text-shadow: 0 0 12px rgba(0, 0, 0, 0.5);
    }

    .char-list {
      display: flex;
      flex-direction: column;
      gap: 3.5rem;
      width: 100%;
      align-items: center;
    }

    .char {
      width: 80%;
      background-color: $char_bg;
      padding: 18px 0;
      text-align: center;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.3s ease;
      font-family: 'Cinzel', serif;
      font-weight: 700;
      font-size: 1.1rem;
      letter-spacing: 1px;
      position: relative;
      display: flex;
      justify-content: center;
      align-items: center;
      color: $title_color;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .btonperso {
      position: absolute;
      width: 100%;
      height: 100%;
    }

    .char:hover {
      background: $char_hover;
      transform: scale(1.05);
      box-shadow: 0 0 15px $accent_color;
      border-color: $title_color;
      color: #ffffff;
    }

    /* --- MAIN --- */
    .main {
      flex: 1;
      position: relative;
      display: flex;
      justify-content: center;
      align-items: flex-end;
      overflow: hidden;
    }

    .main video, .main .bg-hero {
      position: absolute;
      width: 100%;
      height: 100%;
      object-fit: cover;
      filter: brightness(0.8) contrast(1.1) saturate(1.1);
    }

    .nombre {
      z-index: 1;
    }

    .nombre img {
      width: 750px;
      height: 300px;
      filter: drop-shadow(0 0 25px $accent_color);
    }

    /* --- STATS PANEL --- */
    .stats-panel {
      width: 25%;
      background: linear-gradient(180deg, $panel_start, $panel_end);
      border-left: 2px solid $panel_border;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 3rem 2rem 2rem 2rem;
    }

    .stats {
      display: flex;
      flex-direction: column;
      justify-content: space-evenly;
      height: 100%;
    }

    .stats h3 {
      font-family: 'Cinzel', serif;
      font-size: 1.8rem;
      font-weight: 700;
      text-align: center;
      margin-top: 0.5rem;
      margin-bottom: 1rem;
      color: $title_color;
      letter-spacing: 1px;
      text-shadow: 0 0 12px rgba(0, 0, 0, 0.6);
    }

    .description {
      font-family: 'Rajdhani', sans-serif;
      font-size: 1.15rem;
      font-weight: 600;
      line-height: 1.5;
      color: #ffffff;
      text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.9);
      background: rgba(0, 0, 0, 0.55);
      padding: 12px;
      border-radius: 6px;
      border-left: 3px solid $description_border;
      margin-bottom: 1rem;
    }

    .barras h3 {
      font-size: 1.2rem;
      font-family: 'Cinzel', serif;
      letter-spacing: 1px;
      color: #e0e0e0;
    }

    .barras h2 {
      font-family: 'Rajdhani', sans-serif;
      font-weight: 700;
      color: #ffffff;
      font-size: 1.8rem;
      text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);
    }

    /* CORREGIDO: Altura fija para evitar el bug de estiramiento */
    .stat-bar {
      background: rgba(255, 255, 255, 0.1);
      border-radius: 8px;
      margin-top: 0.3rem;
      height: 10px;
      overflow: hidden;
    }

    .stat-fill {
      height: 100%;
      background: linear-gradient(90deg, $stat_start, $stat_end);
      box-shadow: 0 0 10px $accent_color;
    }

    /* --- BOTONES (CORREGIDO: Texto blanco con buena lectura) --- */
    .play-btn {
      margin-top: 1.5rem;
      background: linear-gradient(45deg, $button_start, $button_end);
      color: #ffffff;
      border: none;
      padding: 14px 40px;
      font-family: 'Cinzel', serif;
      font-size: 1.2rem;
      font-weight: 800;
      border-radius: 4px;
      cursor: pointer;
      text-transform: uppercase;
      letter-spacing: 2px;
      box-shadow: 0 0 15px $button_shadow;
      transition: all 0.3s ease;
      text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
    }

    .play-btn:hover {
      transform: scale(1.05);
      box-shadow: 0 0 25px $button_shadow;
      background: linear-gradient(45deg, $button_hover_start, $button_hover_end);
      color: #ffffff;
    }

    .play-btn:active {
      transform: scale(0.96);
    }
  </style>
''')

files = [
    ('antagonistas', 'aatrox.html'),
    ('antagonistas', 'mordekaiser.html'),
    ('antagonistas', 'viego.html'),
    ('antagonistas', 'shyvana.html'),
    ('antagonistas', 'zed.html'),
    ('heroes', 'Ashe.html'),
    ('heroes', 'Ezreal.html'),
    ('heroes', 'Garen.html'),
    ('heroes', 'Kayle.html'),
    ('heroes', 'Teemo.html'),
]

for folder, name in files:
    path = root / folder / name
    if not path.exists():
        print(f"Skipping {name}: file not found at {path}")
        continue
        
    content = path.read_text(encoding='utf-8')
    theme = styles[name]
    
    # Inyectar fuentes si no existen
    if font_block.strip() not in content:
        idx = content.lower().rfind('</head>')
        if idx != -1:
            content = content[:idx] + font_block + '\n' + content[idx:]
            
    # Reemplazar bloque de estilos
    start = content.find('<style>')
    end = content.rfind('</style>')
    if start == -1 or end == -1:
        print(f"No <style> tags found in {name}")
        continue
        
    new_style = base.substitute(**theme)
    content = content[:start] + new_style + content[end + len('</style>'):]
    
    # Asegurar clase description en el párrafo principal
    if '<p>' in content and 'class="description"' not in content:
        p_index = content.find('<p>')
        content = content[:p_index] + '<p class="description">' + content[p_index+3:]
        
    path.write_text(content, encoding='utf-8')
    print(f"Updated {name} successfully!")