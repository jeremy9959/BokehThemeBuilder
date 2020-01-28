import textwrap
from bokeh.models.widgets import Button, PreText, Div
from bokeh.layouts import column, grid,row
from bokeh.io import curdoc
from bokeh.models.glyphs import Line
from bokeh.models import Plot, Toolbar, Grid, Title, Panel, Tabs
from bokeh.models.tickers import BasicTicker
from bokeh.models.sources import ColumnDataSource
from bokeh.models.formatters import BasicTickFormatter
from bokeh.models.axes import LinearAxis
from functools import partial
from options import (
    Plot_Options,
    Toolbar_Options,
    Grid_Options,
    Title_Options,
    Axis_Options,
)

from widgets import ModelBuilder


def button_handler(Builders):
    P = make_plot(Builders)
    layout.children[0] = P
    text = ""
    for div_name in Builders:
        for line in textwrap.wrap(
            div_name.upper()
            + "_OPTIONS = "
            + str(Builders[div_name].param_dict),
            break_long_words=False, break_on_hyphens=False
        ):
            text = text + line + "\n"
    M=doc.get_model_by_name('report')
    M.text = text

def make_plot(Builders):
    P = Plot(name="plot", **Builders["plot"].param_dict)
    P.add_glyph(
        ColumnDataSource({"x": [1, 2, 3], "y": [1, 2, 3]}),
        Line(x="x", y="y"),
        visible=False,
    )

    P.toolbar = Toolbar(name="toolbar", **Builders["toolbar"].param_dict)
    P.add_layout(Grid(dimension=0, **Builders["xgrid"].param_dict, ticker=BasicTicker()), "center")
    P.add_layout(Grid(dimension=1, **Builders["ygrid"].param_dict, ticker=BasicTicker()), "center")
    P.title = Title(**Builders["title"].param_dict)
    P.add_layout(
        LinearAxis(
            ticker=BasicTicker(), formatter=BasicTickFormatter(), **Builders["xaxis"].param_dict,
        ),
        "below",
    )
    P.add_layout(
        LinearAxis(
            ticker=BasicTicker(), formatter=BasicTickFormatter(), **Builders["yaxis"].param_dict,
        ),
        "left",
    )

    return P


Print = Button(label="Activate")
Builders = {
    "plot": ModelBuilder(Plot_Options),
    "toolbar": ModelBuilder(Toolbar_Options),
    "xgrid": ModelBuilder(Grid_Options),
    "ygrid": ModelBuilder(Grid_Options),
    "title": ModelBuilder(Title_Options),
    "xaxis": ModelBuilder(Axis_Options),
    "yaxis": ModelBuilder(Axis_Options),
}
Print.on_click(partial(button_handler, Builders))
plot = make_plot(Builders)
panels = {}
for n in Builders:
    panels[n] = Panel(
        child=column(
            Print,
            PreText(text=n.upper() + "_OPTIONS = ", name=n + "_div"),
            grid(Builders[n].widgets, ncols=3),
        ),
        title=n,
    )

doc=curdoc()
Report = PreText(text="",name="report")
tabs = Tabs(tabs=list(panels.values()))
layout = column(row(plot,Report), tabs)
doc.add_root(layout)
print(doc.get_model_by_name("report"))
