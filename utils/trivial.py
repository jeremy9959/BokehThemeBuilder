import bokeh
from bokeh.layouts import row
from bokeh.io import curdoc
from bokeh.document import Document
import json

with open('document.json') as f:
    d = f.read()

D = Document().from_json_string(d)
f = D.roots[0]
D.clear()

curdoc().add_root(f)

