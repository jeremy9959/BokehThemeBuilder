import inspect
from bokeh.models.widgets import Button
from bokeh.layouts import column, grid
from bokeh.io import curdoc
from bokeh.model import collect_models
from bokeh.models.glyphs import Line
from bokeh.document import Document
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


def save_handler(
    plot_param_dict,
    toolbar_param_dict,
    grid0_param_dict,
    grid1_param_dict,
    title_param_dict,
    xaxis_param_dict,
    yaxis_param_dict,
):
    for kind in ["plot", "grid0", "grid1","toolbar", "title", "xaxis", "yaxis"]:
        print("{}_opts = ".format(kind), eval("{}_param_dict".format(kind)))


def button_handler(
    plot_param_dict,
    toolbar_param_dict,
    grid0_param_dict,
    grid1_param_dict,
    title_param_dict,
    xaxis_param_dict,
    yaxis_param_dict,
):
    print("Button!")
    P = make_plot(
        plot_param_dict,
        toolbar_param_dict,
        grid0_param_dict,
        grid1_param_dict,
        title_param_dict,
        xaxis_param_dict,
        yaxis_param_dict,
    )

    layout.children[0] = P


def make_plot(
    plot_param_dict,
    toolbar_param_dict,
    grid0_param_dict,
    grid1_param_dict,
    title_param_dict,
    xaxis_param_dict,
    yaxis_param_dict,
):
    P = Plot(name="plot", **plot_param_dict)
    P.add_glyph(ColumnDataSource({"x": [1, 2, 3], "y": [1, 2, 3]}), Line(x="x", y="y"))

    T = Toolbar(name="toolbar", **toolbar_param_dict)
    P.toolbar = T
    Grid0 = Grid(dimension=0, **grid0_param_dict, ticker=BasicTicker())
    Grid1 = Grid(dimension=1, **grid1_param_dict, ticker=BasicTicker())
    P.add_layout(Grid0, "center")
    P.add_layout(Grid1, "center")

    T = Title(**title_param_dict)
    P.title = T

    P.add_layout(
        LinearAxis(
            ticker=BasicTicker(), formatter=BasicTickFormatter(), **xaxis_param_dict
        ),
        "below",
    )
    P.add_layout(
        LinearAxis(
            ticker=BasicTicker(), formatter=BasicTickFormatter(), **yaxis_param_dict
        ),
        "left",
    )

    return P


Print = Button()
PlotBuilder = ModelBuilder(Plot_Options)
ToolbarBuilder = ModelBuilder(Toolbar_Options)
GridBuilder0 = ModelBuilder(Grid_Options)
GridBuilder1 = ModelBuilder(Grid_Options)
TitleBuilder = ModelBuilder(Title_Options)
Xaxis = ModelBuilder(Axis_Options)
Yaxis = ModelBuilder(Axis_Options)

title_param_dict, title_widgets = TitleBuilder.param_dict, TitleBuilder.widgets
plot_param_dict, toolbar_param_dict = PlotBuilder.param_dict, ToolbarBuilder.param_dict
plot_widgets, toolbar_widgets = PlotBuilder.widgets, ToolbarBuilder.widgets
grid0_param_dict, grid1_param_dict = GridBuilder0.param_dict, GridBuilder1.param_dict
grid0_widgets, grid1_widgets = GridBuilder0.widgets, GridBuilder1.widgets
xaxis_widgets, yaxis_widgets = Xaxis.widgets, Yaxis.widgets
xaxis_param_dict, yaxis_param_dict = Xaxis.param_dict, Yaxis.param_dict

print(xaxis_param_dict)

Print.on_click(
    partial(
        button_handler,
        plot_param_dict,
        toolbar_param_dict,
        grid0_param_dict,
        grid1_param_dict,
        title_param_dict,
        xaxis_param_dict,
        yaxis_param_dict,
    )
)

plot = make_plot(
    plot_param_dict,
    toolbar_param_dict,
    grid0_param_dict,
    grid1_param_dict,
    title_param_dict,
    xaxis_param_dict,
    yaxis_param_dict,
)

xgrid_panel = Panel(child=column(Print, grid(grid0_widgets, ncols=3)), title="xGrid")
ygrid_panel = Panel(child=column(Print, grid(grid1_widgets, ncols=3)), title="yGrid")
toolbar_panel = Panel(
    child=column(Print, grid(toolbar_widgets, ncols=3)), title="Toolbar"
)
title_panel = Panel(child=column(Print, grid(title_widgets, ncols=3)), title="Title")
xaxis_panel = Panel(child=column(Print, grid(xaxis_widgets, ncols=3)), title="xAxes")
yaxis_panel = Panel(child=column(Print, grid(yaxis_widgets, ncols=3)), title="yAxes")
plot_panel = Panel(child=column(Print, grid(plot_widgets, ncols=3)), title="Plot")
basic_tabs = [
    plot_panel,
    xgrid_panel,
    ygrid_panel,
    toolbar_panel,
    title_panel,
    xaxis_panel,
    yaxis_panel,
]
tabs = Tabs(tabs=basic_tabs)

save = Button()
save.on_click(
    partial(
        save_handler,
        plot_param_dict,
        toolbar_param_dict,
        grid0_param_dict,
        grid1_param_dict,
        title_param_dict,
        xaxis_param_dict,
        yaxis_param_dict,
    )
)

layout = column(plot, save, tabs)
curdoc().add_root(layout)
