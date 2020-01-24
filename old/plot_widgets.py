from bokeh.models.widgets import TextInput, ColorPicker, Select
from functools import partial
from plot_options import Plot_Options


def choice_handler(param_dict, param, choices, values, attr, old, new):
    print("attr=", attr, "old=", old, "opt=", new, "who=", param)
    choice_dict = dict(zip(choices, values))
    param_dict[param] = choice_dict[new]


def single_handler(param_dict, param, transform, attr, old, new):
    print("attr=", attr, "old=", old, "who=", param, "new=", new)
    param_dict[param] = transform(new)


def make_choice(choices, values, default, param, param_dict):
    radio = Select(options=choices, value=choices[default], title=param)
    radio.on_change(
        "value", partial(choice_handler, param_dict, param, choices, values)
    )
    return radio


def make_float(default, param, param_dict):
    area = TextInput(value=str(default), title=param)
    area.on_change(
        "value", partial(single_handler, param_dict, param, lambda x: float(x))
    )
    return area


def make_int(default, param, param_dict):
    area = TextInput(value=str(default), title=param)
    area.on_change(
        "value", partial(single_handler, param_dict, param, lambda x: int(x))
    )
    return area


def make_color(default, param, param_dict):
    picker = ColorPicker(color=default, title=param)
    picker.on_change("color", partial(single_handler, param_dict, param, lambda x: x))
    return picker


def plot_widgets_maker(param_dict):
    widgets = []
    for attribute, options in Plot_Options["choices"].items():
        chooser = make_choice(
            options[0],
            values=options[1],
            default=0,
            param=attribute,
            param_dict=param_dict,
        )
        widgets.append(chooser)

    for kind, maker in [
        ("ints", make_int),
        ("floats", make_float),
        ("colors", make_color),
    ]:
        for attribute, options in Plot_Options[kind].items():
            chooser = maker(options, attribute, param_dict)
            widgets.append(chooser)

    return param_dict, widgets
