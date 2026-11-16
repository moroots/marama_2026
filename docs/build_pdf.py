"""Build docs/before-the-course.pdf from docs/before-the-course.md.

Run from anywhere:
    uv run --with weasyprint --with markdown-it-py docs/build_pdf.py
"""
import re, textwrap
from pathlib import Path
from markdown_it import MarkdownIt
from weasyprint import HTML

HERE = Path(__file__).resolve().parent
SRC, OUT = HERE / "before-the-course.md", HERE / "before-the-course.pdf"

CSS = """
@page { size: Letter; margin: 0.9in 0.75in 0.85in;
        @bottom-center { content: "MARAMA Python Tutorial 2026 \\00b7  Questions? mroots1@umbc.edu \\00b7  page " counter(page);
                         font: 9pt 'Noto Sans', 'DejaVu Sans', sans-serif; color: #555; } }
body { font: 10.5pt/1.5 'Roboto', 'Noto Sans', 'DejaVu Sans', sans-serif; color: #1c1c1c; }
h1 { background: linear-gradient(135deg, #1f4e79, #2f80ed 55%, #56ccf2); color: white; font-size: 21pt;
     padding: 20px 26px; border-radius: 14px; margin: 0 0 14px; }
h2 { background: linear-gradient(90deg, #2f80ed, #56ccf2); color: white; font-size: 14pt; padding: 10px 20px;
     border-radius: 10px; margin: 26px 0 12px; break-after: avoid; }
h3 { color: #1f4e79; font-size: 12pt; margin: 18px 0 6px; break-after: avoid; }
a { color: #1a6fd0; }
.box { border-left: 6px solid #2f80ed; background: #e6effc; padding: 4px 22px; border-radius: 8px; margin: 14px 0; break-inside: avoid; }
.box.why { border-left-color: #f2994a; background: #fdf0e2; }
pre { background: #f3f4f6; border: 1px solid #d0d7de; border-radius: 8px; padding: 10px 14px; font-size: 8.8pt;
      white-space: pre-wrap; word-wrap: break-word; break-inside: avoid; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 9pt; }
p code, li code, td code { background: #eef0f3; padding: 1px 4px; border-radius: 4px; }
table { border-collapse: collapse; width: 100%; margin: 10px 0; font-size: 9.8pt; }
th, td { border: 1px solid #c5cdd8; padding: 7px 10px; text-align: left; vertical-align: top; }
th { background: #e3edfb; }
tr { break-inside: avoid; }
blockquote { border-left: 4px solid #c5cdd8; margin: 10px 0; padding: 2px 14px; color: #333; }
hr { border: 0; border-top: 1px solid #c5cdd8; margin: 22px 0 10px; }
"""

html_body = MarkdownIt("commonmark", {"html": True}).enable("table").render(SRC.read_text(encoding="utf-8"))
# Code blocks inside list items can come out with uneven indentation; dedent each block.
html_body = re.sub(r"(<pre><code[^>]*>)(.*?)(</code></pre>)",
                   lambda m: m.group(1) + textwrap.dedent(m.group(2)) + m.group(3), html_body, flags=re.S)
html = f"<html><head><meta charset='utf-8'><title>Before the Course | MARAMA Python Tutorial 2026</title></head><body>{html_body}</body></html>"
HTML(string=html, base_url=str(HERE)).write_pdf(OUT, stylesheets=[__import__("weasyprint").CSS(string=CSS)])
print("wrote", OUT, f"({OUT.stat().st_size // 1024} KB)")
