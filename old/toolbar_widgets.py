from bokeh.models.widgets import TextInput, ColorPicker, Select, CheckboxGroup
from functools import partial
from toolbar_options import Toolbar_Options


def choice_handler(param_dict, param, choices, values, attr, old, new):
    print("attr=", attr, "old=", old, "opt=", new, "who=", param)
    choice_dict = dict(zip(choices, values))
    param_dict[param] = choice_dict[new]


def multi_choice_handler(param_dict, param, choices, values, attr, old, new):
    print("attr=", attr, "old=", old, "opt=", new, "who=", param)
    active_list = [values[x] for x in new]
    param_dict[param] = active_list


def single_handler(param_dict, param, transform, attr, old, new):
    print("attr=", attr, "old=", old, "who=", param, "new=", new)
    param_dict[param] = transform(new)


def make_choice(choices, values, default, param, param_dict):
    radio = Select(options=choices, value=choices[default], title=param)
    radio.on_change(
        "value", partial(choice_handler, param_dict, param, choices, values)
    )
    return radio


def make_multi_choice(choices, values, default, param, param_dict):
    checkbox = CheckboxGroup(labels=choices, inline=False)
    checkbox.on_change(
        "active", partial(multi_choice_handler, param_dict, param, choices, values)
    )
    return checkbox


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


def toolbar_widgets_maker(param_dict):
    widgets = []
    for attribute, options in Toolbar_Options["choices"].items():
        chooser = make_choice(
            options[0],
            values=options[1],
            default=0,
            param=attribute,
            param_dict=param_dict,
        )
        widgets.append(chooser)

    for attribute, options in Toolbar_Options["multi_choices"].items():
        print(attribute, options)
        chooser = make_multi_choice(
            options[0], options[1], default=[0], param=attribute, param_dict=param_dict
        )
        widgets.append(chooser)

    for kind, maker in [
        ("ints", make_int),
        ("floats", make_float),
        ("colors", make_color),
    ]:
        for attribute, options in Toolbar_Options[kind].items():
            chooser = maker(options, attribute, param_dict)
            widgets.append(chooser)

    return param_dict, widgets
