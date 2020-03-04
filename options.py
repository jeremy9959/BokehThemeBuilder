FONT_SIZES = ["4pt", "6pt", "8pt", "10pt", "12pt", "16pt", "18pt", "24pt", "32pt"]
FONT_CHOICES = ["Helvetica", "Times", "Calibri", "Candara", "Arial", "Bookman"]
FONT_STYLES = ["normal", "bold", "italic", "bold_italic"]
DASH_PATTERNS = ["solid", "dashed", "dotted", "dotdash", "dashdot"]

Toolbar_Options = {
    "choices": {
        "logo": (["normal", "grey", "none"], ["normal", "grey", None]),
        "autohide": (["false", "true"], [False, True]),
    },
    "floats": {},
    "colors": {},
    "ints": {},
}

Plot_Options = {
    "choices": {
        "width_policy": (
            ["auto", "fixed", "fit", "min", "max"],
            ["auto", "fixed", "fit", "min", "max"],
        ),
        "height_policy": (
            ["auto", "fixed", "fit", "min", "max"],
            ["auto", "fixed", "fit", "min", "max"],
        ),
        "align": (["start", "center", "end"], ["start", "center", "end"]),
        "title_location": (
            ["above", "below", "left", "right"],
            ["above", "below", "left", "right"],
        ),
        "outline_line_dash": (
            ["solid", "dashed", "dotted", "dotdash", "dashdot"],
            ["solid", "dashed", "dotted", "dotdash", "dashdot"],
        ),
        "reset_policy": (["standard", "event_only"], ["standard", "event_only"]),
        "match_aspect": (["True", "False"], [True, False]),
        "sizing_mode": (
            [
                "stretch_width",
                "stretch_height",
                "stretch_both",
                "scale_width",
                "scale_height",
                "scale_both",
                "fixed",
            ],
            [
                "stretch_width",
                "stretch_height",
                "stretch_both",
                "scale_width",
                "scale_height",
                "scale_both",
                "fixed",
            ],
        ),
        "outline_line_join": (["miter", "round", "bevel"], ["miter", "round", "bevel"]),
        "disabled": (["True", "False"], [True, False]),
        "toolbar_location": (
            ["right", "above", "below", "left"],
            ["right", "above", "below", "left"],
        ),
        "outline_line_cap": (["butt", "round", "square"], ["butt", "round", "square"]),
        "visible": (["True", "False"], [True, False]),
        "hidpi": (["True", "False"], [True, False]),
        "toolbar_sticky": (["True", "False"], [True, False]),
        "output_backend": (["canvas", "svg", "webgl"], ["canvas", "svg", "webgl"]),
    },
    "ints": {
        "max_height": 0,
        "lod_interval": 300,
        "max_width": 0,
        "min_border_left": 0,
        "min_border_right": 0,
        "min_border_bottom": 0,
        "min_height": 0,
        "plot_height": 600,
        "lod_timeout": 500,
        "min_width": 0,
        "height": 0,
        "plot_width": 600,
        "min_border": 5,
        "width": 0,
        "frame_height": 0,
        "outline_line_dash_offset": 0,
        "lod_factor": 10,
        "lod_threshold": 2000,
        "min_border_top": 0,
        "frame_width": 0,
    },
    "floats": {
        "outline_line_width": 1,
        "background_fill_alpha": 1.0,
        "aspect_scale": 1.0,
        "border_fill_alpha": 1.0,
        "outline_line_alpha": 1.0,
    },
    "colors": {
        "border_fill_color": "#ffffff",
        "background_fill_color": "#ffffff",
        "outline_line_color": "#e5e5e5",
    },
}


Grid_Options = {
    "multi_choices": {},
    "colors": {
        "minor_grid_line_color": "#FFFFFF",
        "band_fill_color": "#FFFFFF",
        "band_hatch_color": "#FFFFFF",
        "grid_line_color": "#e5e5e5",
    },
    "choices": {
        "band_hatch_pattern": (
            [
                "blank",
                ".",
                "o",
                "-",
                "|",
                "+",
                '"',
                ":",
                "@",
                "/",
                "\\",
                "x",
                ",",
                "`",
                "v",
                ">",
                "*",
            ],
            [
                "blank",
                ".",
                "o",
                "-",
                "|",
                "+",
                '"',
                ":",
                "@",
                "/",
                "\\",
                "x",
                ",",
                "`",
                "v",
                ">",
                "*",
            ],
        ),
        "grid_line_cap": (["butt", "round", "square"], ["butt", "round", "square"]),
        "grid_line_join": (["bevel", "miter", "round"], ["bevel", "miter", "round"]),
        "minor_grid_line_cap": (
            ["butt", "round", "square"],
            ["butt", "round", "square"],
        ),
        "minor_grid_line_join": (
            ["bevel", "miter", "round"],
            ["bevel", "miter", "round"],
        ),
        "level": (
            ["underlay", "image", "glyph", "annotation", "overlay"],
            ["underlay", "image", "glyph", "annotation", "overlay"],
        ),
        "minor_grid_line_dash": (DASH_PATTERNS, DASH_PATTERNS),
        "grid_line_dash": (DASH_PATTERNS, DASH_PATTERNS),
    },
    "floats": {
        "grid_line_width": 1.0,
        "grid_line_alpha": 1.0,
        "minor_grid_line_width": 1.0,
        "band_fill_alpha": 0.0,
        "band_hatch_alpha": 1.0,
        "minor_grid_line_alpha": 1.0,
    },
    "ints": {
        "grid_line_dash_offset": 0,
        "minor_grid_line_dash_offset": 0,
        "band_hatch_scale": 12,
        "band_hatch_weight": 1,
        #        "dimension": 0,
        # set dimension in construction of grid to avoid confusion later
    },
}

Title_Options = {
    "colors": {
        "border_line_color": "#ffffff",
        "text_color": "#444444",
        "background_fill_color": "#ffffff",
    },
    "choices": {
        "border_line_cap": (["butt", "round", "square"], ["butt", "round", "square"]),
        "level": (
            ["underlay", "image", "glyph", "annotation", "overlay"],
            ["underlay", "image", "glyph", "annotation", "overlay"],
        ),
        "align": (["left", "right", "center"], ["left", "right", "center"]),
        "border_line_join": (["bevel", "miter", "round"], ["bevel", "miter", "round"]),
        "text_font_style": (FONT_STYLES, FONT_STYLES),
        "vertical_align": (["bottom", "top", "middle"], ["bottom", "top", "middle"]),
        "text_font_size": (FONT_SIZES, FONT_SIZES),
        "text_font": (FONT_CHOICES, FONT_CHOICES),
    },
    "floats": {
        "offset": 0.0,
        "border_line_alpha": 1.0,
        "background_fill_alpha": 1.0,
        "border_line_width": 1.0,
        "text_alpha": 1.0,
    },
    "strings": {"text": ""},
}

Axis_Options = {
    "choices": {
        "axis_label_text_baseline": (
            ["top", "middle", "bottom", "alphabetic", "hanging", "ideographic"],
            ["top", "middle", "bottom", "alphabetic", "hanging", "ideographic"],
        ),
        "major_label_orientation": (
            ["horizontal", "vertical"],
            ["horizontal", "vertical"],
        ),
        "major_tick_line_dash": (DASH_PATTERNS, DASH_PATTERNS),
        "axis_label_text_font_style": (FONT_STYLES, FONT_STYLES),
        "major_label_text_font_style": (FONT_STYLES, FONT_STYLES),
        "axis_line_join": (["miter", "round", "bevel"], ["miter", "round", "bevel"]),
        "axis_line_cap": (["butt", "round", "square"], ["butt", "round", "square"]),
        "axis_label_text_align": (
            ["left", "right", "center"],
            ["left", "right", "center"],
        ),
        "major_tick_line_cap": (
            ["butt", "round", "square"],
            ["butt", "round", "square"],
        ),
        "axis_line_dash": (DASH_PATTERNS, DASH_PATTERNS),
        "minor_tick_line_cap": (
            ["butt", "round", "square"],
            ["butt", "round", "square"],
        ),
        "minor_tick_line_dash": (DASH_PATTERNS, DASH_PATTERNS),
        "major_label_text_baseline": (
            ["top", "middle", "bottom", "alphabetic", "hanging", "ideographic"],
            ["top", "middle", "bottom", "alphabetic", "hanging", "ideographic"],
        ),
        "major_label_text_font_size": (FONT_SIZES, FONT_SIZES),
        "major_label_text_align": (
            ["left", "right", "center"],
            ["left", "right", "center"],
        ),
        "major_tick_line_join": (
            ["miter", "round", "bevel"],
            ["miter", "round", "bevel"],
        ),
        "level": (
            ["image", "underlay", "glyph", "annotation", "overlay"],
            ["image", "underlay", "glyph", "annotation", "overlay"],
        ),
        "minor_tick_line_join": (
            ["miter", "round", "bevel"],
            ["miter", "round", "bevel"],
        ),
        "axis_label_text_font_size": (FONT_SIZES, FONT_SIZES),
        "major_label_text_font": (FONT_CHOICES, FONT_CHOICES),
        "axis_label_text_font": (FONT_CHOICES, FONT_CHOICES),
    },
    "strings": {"axis_label": "Label"},
    "ints": {
        "axis_line_dash_offset": 0,
        "major_label_standoff": 5,
        "minor_tick_out": 4,
        "axis_label_standoff": 5,
        "minor_tick_line_dash_offset": 0,
        "major_tick_in": 2,
        "major_tick_line_dash_offset": 0,
        "major_tick_out": 6,
        "minor_tick_in": 0,
    },
    "floats": {
        "major_tick_line_alpha": 1.0,
        "major_tick_line_width": 1,
        "axis_line_width": 1,
        "minor_tick_line_alpha": 1.0,
        "axis_label_text_line_height": 1.2,
        "major_label_text_alpha": 1.0,
        "major_label_text_line_height": 1.2,
        "axis_line_alpha": 1.0,
        "minor_tick_line_width": 1,
        "axis_label_text_alpha": 1.0,
    },
    "colors": {
        "major_label_text_color": "#444444",
        "axis_label_text_color": "#444444",
        "axis_line_color": "black",
        "major_tick_line_color": "black",
        "minor_tick_line_color": "black",
    },
}

Line_Options = {
    "choices": {
        "line_cap": (["butt", "round", "square"], ["butt", "round", "square"]),
        "line_join": (["miter", "round", "bevel"], ["miter", "round", "bevel"]),
        "line_dash": (
            ["solid", "dashed", "dotted", "dotdash", "dashdot"],
            ["solid", "dashed", "dotted", "dotdash", "dashdot"],
        ),
    },
    "ints": {"line_dash_offset": 0},
    "floats": {"line_alpha": 1.0, "line_width": 1.0},
    "colors": {"line_color": "black"},
}

Text_Options = {
    "choices": {
        "text_baseline": (
            ["top", "middle", "bottom", "alphabetic", "hanging", "ideographic"],
            ["top", "middle", "bottom", "alphabetic", "hanging", "ideographic"],
        ),
        "text_font": (FONT_CHOICES, FONT_CHOICES),
        "text_font_style": (
            FONT_STYLES, 
            FONT_STYLES,
        ),
        "text_align": (["left", "right", "center"], ["left", "right", "center"]),
        "text_font_size": (
            FONT_SIZES,
            FONT_SIZES
        ),
    },
    "floats": {"text_line_height": 1.2, "text_alpha": 1.0},
    "colors": {"text_color": "#444444"},
}

Fill_Options = {"floats": {"fill_alpha": 1.0}, "colors": {"fill_color": "gray"}}
