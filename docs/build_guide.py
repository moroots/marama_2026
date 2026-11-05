"""Build docs/before-the-course.html from docs/before-the-course.md.

The Markdown is the single source. On GitHub it reads as plain text with
bold titles; this script adds the notebook's styled boxes (same four colors).

    pip install markdown weasyprint
    python docs/build_guide.py          # writes the .html and the .pdf
"""
import re
import sys
from pathlib import Path
import markdown

HERE = Path(__file__).parent
FULL = (HERE / "before-the-course.md").read_text(encoding="utf-8")


def render(src):

    # box kind -> (border, background, text-safe)
    KINDS = {
        "goal":    ("#2f80ed", "rgba(47,128,237,.12)"),
        "turn":    ("#f2994a", "rgba(242,153,74,.15)"),
        "discuss": ("#9b51e0", "rgba(155,81,224,.13)"),
        "why":     ("#27ae60", "rgba(39,174,96,.13)"),
        "watch":   ("#eb5757", "rgba(235,87,87,.13)"),
    }

    # let Markdown render inside the <div class="..."> wrappers
    src = re.sub(r'<div class="(box \w+|legend)">', r'<div class="\1" markdown="1">', src)
    src = src.replace('<details>', '<details markdown="1">')
    body = markdown.markdown(src, extensions=["tables", "fenced_code", "md_in_html", "sane_lists"])

    for kind, (c, bg) in KINDS.items():
        body = body.replace(
            f'<div class="box {kind}">',
            f'<div style="border-left:7px solid {c};background:{bg};padding:6px 18px;margin:14px 0;'
            f'border-radius:8px;line-height:1.5">')
    body = body.replace('<div class="legend">',
        '<div style="text-align:center;padding:8px 14px;margin:14px 0;border:1px dashed #8884;border-radius:8px">')

    # banners for H1, bars for H2
    body = re.sub(r"<h1>(.*?)</h1>",
        r'<h1 style="background:linear-gradient(135deg,#1f4e79,#2f80ed 55%,#56ccf2);color:#fff;'
        r'padding:22px 28px;border-radius:14px;margin:30px 0 10px;font-size:1.8em">\1</h1>', body)
    body = re.sub(r"<h2>(.*?)</h2>",
        r'<h2 style="background:linear-gradient(90deg,#2f80ed,#56ccf2);color:#fff;padding:9px 18px;'
        r'border-radius:10px;margin:28px 0 8px;font-size:1.25em">\1</h2>', body)
    # TBD markers stand out
    body = re.sub(r"<strong>(\[TBD[^<]*)</strong>",
        r'<strong style="background:#fff3b0;color:#222;padding:0 5px;border-radius:4px">\1</strong>', body)

    page = f"""<!doctype html>
    <html lang="en"><head><meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Before the Course | MARAMA Python Tutorial 2026</title>
    <style>
     body{{font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;line-height:1.55;
          max-width:820px;margin:0 auto;padding:16px;color:#1c1c1e;background:#fff}}
     table{{border-collapse:collapse;width:100%;margin:12px 0}}
     th,td{{border:1px solid #8886;padding:7px 10px;text-align:left;vertical-align:top}}
     th{{background:rgba(47,128,237,.12)}}
     pre{{background:#f4f6f8;border:1px solid #d8dde3;border-radius:8px;padding:12px;overflow-x:auto}}
     code{{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.92em}}
     :not(pre)>code{{background:#f0f2f5;padding:1px 5px;border-radius:4px}}
     details{{border:1px solid #8886;border-radius:8px;padding:8px 14px;margin:12px 0}}
     summary{{cursor:pointer}}
     a{{color:#1a6fd6}}
     @media (prefers-color-scheme:dark){{
      body{{background:#16181c;color:#e6e8eb}}
      pre{{background:#22262c;border-color:#3a3f47}}
      :not(pre)>code{{background:#2a2f36}}
      a{{color:#7ab7ff}}
     }}
    </style></head><body>
    {body}
    </body></html>"""


    return page

(HERE / "before-the-course.html").write_text(render(FULL), encoding="utf-8")
print("wrote before-the-course.html")

# ---- PDF (WeasyPrint). Answers fold is opened and moved to its own page. ----
try:
    from weasyprint import HTML
except ImportError:
    sys.exit("html written; install weasyprint to also build the PDF")
print_css = """
<style>
 @page { size: Letter; margin: 0.7in 0.7in 0.8in;
   @bottom-center { content: "MARAMA Python Tutorial 2026 · Questions? mroots1@umbc.edu · page " counter(page);
                    font: 9pt sans-serif; color: #666 } }
 body { max-width: none; padding: 0; font-size: 10.5pt }
 h1 { break-before: page; } h1:first-of-type { break-before: auto; }
 h1, h2, h3 { break-after: avoid; }
 div, table, pre, tr { break-inside: avoid; }
 details { break-before: page; }
 pre { white-space: pre-wrap; word-break: break-word; }
 a { color: #1a6fd6; }
</style></head>"""
for name, text in (("before-the-course.pdf", FULL),):
    pdf_page = render(text).replace("</head>", print_css, 1).replace("<details>", "<details open>")
    HTML(string=pdf_page, base_url=str(HERE)).write_pdf(HERE / name)
    print("wrote", name)
