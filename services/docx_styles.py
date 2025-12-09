"""Bakeer Academy Word Document Styles (Future enhancement)"""

BAKEER_STYLES = {
    "title": {
        "font": "Calibri",
        "size": 36,
        "bold": True,
        "color": "#1F4E79"
    },
    "question": {
        "font": "Calibri",
        "size": 24,
        "bold": False,
        "color": "#000000"
    },
    "options": {
        "font": "Calibri",
        "size": 20,
        "bold": False,
        "color": "#2E75B6"
    },
    "answer": {
        "font": "Calibri",
        "size": 22,
        "bold": True,
        "color": "#008000"
    }
}

def apply_bakeer_style(paragraph, style_name):
    """Apply Bakeer Academy style to paragraph"""
    style = BAKEER_STYLES.get(style_name)
    if style:
        for run in paragraph.runs:
            run.font.name = style["font"]
            run.font.size = Pt(style["size"])
            run.font.bold = style["bold"]
