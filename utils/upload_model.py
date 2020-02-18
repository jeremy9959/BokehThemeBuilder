import bokeh
from bokeh.document import Document
from bokeh.models.widgets import FileInput
from bokeh.layouts import column,row
from bokeh.io import curdoc
from bokeh.io.doc import set_curdoc
import json
import base64

result = ""

def input_handler(attr, old, new):
    result = json.loads(base64.b64decode(new))
    D = Document().from_json(result)
    f = D.roots[0]
    D.clear()
    doc.clear()
    doc.add_root(column(file_in,row(f,M)))
    
file_in = FileInput(accept='.json')
file_in.on_change('value',input_handler)

doc = curdoc()
doc.add_root(file_in)

