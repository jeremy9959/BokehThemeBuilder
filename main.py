import yaml
from bokeh.models.widgets import Button, Div
from bokeh.models.callbacks import CustomJS
from bokeh.layouts import column, grid, row
from bokeh.io import curdoc
from bokeh.models.glyphs import Line, Circle, Text
from bokeh.models import Plot, Toolbar, Grid, Title, Panel, Tabs, Range1d
from bokeh.models.tickers import BasicTicker
from bokeh.models.sources import ColumnDataSource
from bokeh.models.formatters import BasicTickFormatter
from bokeh.models.axes import LinearAxis
from bokeh.transform import dodge
from functools import partial
from options import (
    Plot_Options,
    Toolbar_Options,
    Grid_Options,
    Title_Options,
    Axis_Options,
    Text_Options,
    Line_Options,
    Fill_Options,
)
from widgets import ModelBuilder


def make_app(doc):

    banner = "<H1><center>Bokeh Theme Builder</center></H1>"

    help_text = """<p><b>Instructions:</b> To use this tool, set the
    desired defaults using the widgets below and on the other tabs.
    As you proceed, push the activate button to preview your
    selections as they take effect on the plot shown.  </p> <p> As you
    make choices, yaml code for your developing theme will appear in
    this space.  Once you're satisfied, push the save button (which
    will appear once you get started) to download the yaml, or just
    copy the yaml into a theme file and load it into your bokeh
    app.</p> <p> The blog post <a
    href="https://blog.bokeh.org/posts/styling-bokeh"> Styling Bokeh
    Visualizations </a> explains how to use the theme file.</p>
    </p><p> See <a
    href="https://github.com/jeremy9959/BokehThemeBuilder"> the github
    repo </a> for the code for this app.</p> """

    js_code = """
    var text = source.text ;
    var file = new Blob([text.slice(5,-6)],{type:'text/plain'});
    var elem = window.document.createElement('a');
    elem.href = window.URL.createObjectURL(file);
    elem.download = 'theme.yaml';
    document.body.appendChild(elem);
    elem.click();
    document.body.removeChild(elem);
    """

    LineDataSource = ColumnDataSource(
        {"x": [-10, -8, -3, 1, 5, 14], "y": [6, -2, 3, -1, -3, 8]}
    )
    PointDataSource = ColumnDataSource(
        {"x": [-7, -2, 3, 7], "y": [4, -5, -2, 7], "name": ["JFK", "LBJ", "HRT", "FDR"]}
    )

    yaml_translation_key = {
        "Line": "line_defaults",
        "GlyphText": "text_defaults",
        "GlyphFill": "fill_defaults",
    }

    def button_handler(Builders):
        P = make_plot(Builders)
        layout.children[1].children[0] = P
        theme_yaml = {"attrs": {}}
        for div_name in Builders:
            if div_name in yaml_translation_key:
                theme_yaml[yaml_translation_key[div_name]] = Builders[
                    div_name
                ].param_dict
            else:
                theme_yaml["attrs"][div_name] = Builders[div_name].param_dict
        text = "<pre>" + yaml.safe_dump(theme_yaml, width=50, indent=2) + "</pre>"
        Save.disabled = False
        Save.visible = True
        Report.update(text=text)

    def make_plot(Builders):
        P = Plot(name="Plot", **Builders["Plot"].param_dict)
        P.x_range = Range1d(-15, 15)
        P.y_range = Range1d(-10, 10)
        P.add_glyph(LineDataSource, Line(x="x", y="y", **Builders["Line"].param_dict))
        P.add_glyph(
            PointDataSource,
            Circle(
                x="x",
                y="y",
                radius=0.3,
                **Builders["Line"].param_dict,
                **Builders["GlyphFill"].param_dict,
            ),
        )
        P.add_glyph(
            PointDataSource,
            Text(
                x=dodge("x", 0.4),
                y="y",
                text="name",
                **Builders["GlyphText"].param_dict,
            ),
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

    Builders = {
        "Plot": ModelBuilder(Plot_Options),
        "Title": ModelBuilder(Title_Options),
        "Toolbar": ModelBuilder(Toolbar_Options),
        "Grid": ModelBuilder(Grid_Options),
        "Axis": ModelBuilder(Axis_Options),
        "Line": ModelBuilder(Line_Options),
        "GlyphFill": ModelBuilder(Fill_Options),
        "GlyphText": ModelBuilder(Text_Options),
    }
    Report = Div(text=help_text, name="report")

    Print = Button(label="Activate", button_type="success", width=200)
    Print.on_click(partial(button_handler, Builders))

    Save = Button(
        label="Save as theme.yaml",
        button_type="success",
        width=200,
        disabled=True,
        visible=False,
    )
    Save.callback = CustomJS(args=dict(source=Report), code=js_code)

    plot = make_plot(Builders)
    panels = {}
    for n in Builders:
        panels[n] = Panel(
            child=column(Print, grid(Builders[n].widgets, ncols=3)), title=n
        )
    tabs = Tabs(tabs=list(panels.values()))

    Banner = Div(text=banner, name="banner", align="center")

    layout = column(Banner, row(plot, column(Save, Report)), tabs)
    doc.title = "Bokeh Theme Builder"
    doc.add_root(layout)


make_app(curdoc())
