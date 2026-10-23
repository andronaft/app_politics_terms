"""Renders every <app>/privacy.md and <app>/terms.md to HTML and writes the index.
Add an app: create a folder with privacy.md and terms.md, run `python3 tools/build.py`, commit."""
import html, pathlib, markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<style>body{{font:16px/1.6 -apple-system,system-ui,Segoe UI,Roboto,sans-serif;max-width:760px;margin:0 auto;padding:32px 20px;color:#0e1b33;background:#fff}}
h1{{line-height:1.2}}a{{color:#2f7bff}}@media(prefers-color-scheme:dark){{body{{background:#0a1224;color:#eaf1ff}}}}</style>
</head><body>{body}</body></html>"""

apps = []
for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith(('.', 'tools'))):
    docs = []
    for name in ('privacy', 'terms'):
        md = d / f'{name}.md'
        if not md.exists():
            continue
        text = md.read_text()
        title = text.splitlines()[0].lstrip('# ').strip()
        (d / name).mkdir(exist_ok=True)
        (d / name / 'index.html').write_text(PAGE.format(title=html.escape(title), body=markdown.markdown(text)))
        docs.append((name, title))
    if docs:
        apps.append((d.name, docs))

items = ''.join(
    f'<li><b>{html.escape(app)}</b>: ' + ', '.join(f'<a href="{app}/{n}/">{html.escape(t)}</a>' for n, t in docs) + '</li>'
    for app, docs in apps)
(ROOT / 'index.html').write_text(PAGE.format(title='App policies', body=f'<h1>App policies and terms</h1><ul>{items}</ul>'))
print('built', [a for a, _ in apps])
