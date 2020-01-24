from bokeh.models.scales import LogScale, LinearScale

Plot_Options = {
    "choices": {
        "height_policy": (
            ["auto", "fixed", "fit", "min", "max"],
            ["auto", "fixed", "fit", "min", "max"],
        ),
        "width_policy": (
            ["auto", "fixed", "fit", "min", "max"],
            ["auto", "fixed", "fit", "min", "max"],
        ),
        "x_scale": (["Linear", "Log"], [LinearScale(), LogScale()]),
        "y_scale": (["Linear", "Log"], [LinearScale(), LogScale()]),
        "title_location": (
            ["above", "below", "left", "right"],
            ["above", "below", "left", "right"],
        ),
        "outline_line_cap": (["butt", "round", "square"], ["butt", "round", "square"]),
        "outline_line_join": (["miter", "round", "bevel"], ["miter", "round", "bevel"]),
        "sizing_mode": (
            [
                "stretch_both",
                "stretch_width",
                "stretch_height",
                "scale_width",
                "scale_height",
                "scale_both",
                "fixed",
            ],
            [
                "stretch_both",
                "stretch_width",
                "stretch_height",
                "scale_width",
                "scale_height",
                "scale_both",
                "fixed",
            ],
        ),
        "toolbar_location": (
            ["above", "below", "left", "right"],
            ["above", "below", "left", "right"],
        ),
    },
    "floats": {
        "background_fill_alpha": 1.0,
        "border_fill_alpha": 1.0,
        "outline_line_alpha": 1.0,
        "outline_line_width": 1.0,
    },
    "ints": {
        "frame_height": None,
        "frame_width": None,
        "min_border": 5,
        "min_border_bottom": None,
        "min_border_left": None,
        "min_border_right": None,
        "min_border_top": None,
        "outline_line_dash_offset": 0,
        "plot_height": 600,
        "plot_width": 600,
    },
    "colors": {
        "background": "#ffffff",
        "background_fill_color": "#ffffff",
        "border_fill_color": "#ffffff",
        "outline_line_color": "#e5e5e5",
    },
}
