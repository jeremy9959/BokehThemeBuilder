import textwrap
import yaml
from bokeh.models.widgets import Button, PreText
from bokeh.layouts import column, grid, row
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
    layout.children[0].children[0] = P
    theme_yaml = {'attrs':{}}
    for div_name in Builders:
        theme_yaml['attrs'][div_name] = Builders[div_name].param_dict
    text = yaml.safe_dump(theme_yaml,width=50,indent=2)
    Report.update(text=text)


def make_plot(Builders):
    P = Plot(name="Plot", **Builders["Plot"].param_dict)
    P.add_glyph(
        ColumnDataSource({"x": [1, 2, 3], "y": [1, 2, 3]}),
        Line(x="x", y="y"),
        visible=False,
    )
    P.toolbar = Toolbar(name="Toolbar", **Builders["Toolbar"].param_dict)
    P.add_layout(
        Grid(dimension=0, **Builders["Grid"].param_dict, ticker=BasicTicker()),
        "center",
    )
    P.add_layout(
        Grid(dimension=1, **Builders["Grid"].param_dict, ticker=BasicTicker()),
        "center",
    )
    P.title = Title(**Builders["Title"].param_dict)
    P.add_layout(
        LinearAxis(
            ticker=BasicTicker(),
            formatter=BasicTickFormatter(),
            **Builders["Axis"].param_dict,
        ),
        "below",
    )
    P.add_layout(
        LinearAxis(
            ticker=BasicTicker(),
            formatter=BasicTickFormatter(),
            **Builders["Axis"].param_dict,
        ),
        "left",
    )
    return P


Print = Button(label="Activate")
Builders = {
    "Plot": ModelBuilder(Plot_Options),
    "Title": ModelBuilder(Title_Options),
    "Toolbar": ModelBuilder(Toolbar_Options),
    "Grid": ModelBuilder(Grid_Options),
    "Axis": ModelBuilder(Axis_Options),
}
Print.on_click(partial(button_handler, Builders))
plot = make_plot(Builders)
panels = {}
for n in Builders:
    panels[n] = Panel(child=column(Print, grid(Builders[n].widgets, ncols=3)), title=n)

Report = PreText(text="Style Yaml\n", name="report")
tabs = Tabs(tabs=list(panels.values()))
layout = column(row(plot, Report), tabs)
curdoc().add_root(layout)
