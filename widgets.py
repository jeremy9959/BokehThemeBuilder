from bokeh.models.widgets import TextInput, ColorPicker, Select, CheckboxGroup
from functools import partial

class ModelBuilder:
    def __init__(self, Options):
        self.Options = Options
        self.param_dict = {}
        self.widgets = []

        try:
            for attribute, options in self.Options["choices"].items():
                chooser = self.make_choice(
                    options[0],
                    values=options[1],
                    default=0,
                    param=attribute,
                    param_dict=self.param_dict,
                )
                self.widgets.append(chooser)
        except KeyError:
            pass

        try:
            for attribute, options in self.Options["multi_choices"].items():
                chooser = self.make_multi_choice(
                    options[0],
                    options[1],
                    default=[0],
                    param=attribute,
                    param_dict=self.param_dict,
                )
                self.widgets.append(chooser)
        except KeyError:
            pass

        for kind, maker in [
                ("ints", self.make_int),
                ("floats", self.make_float),
                ("colors", self.make_color),
                ("strings", self.make_string),
        ]:
            try:
                for attribute, options in self.Options[kind].items():
                    chooser = maker(options, attribute, self.param_dict)
                    self.widgets.append(chooser)
            except KeyError:
                continue

        self.widgets = sorted(self.widgets,key=lambda x: x.name)
        
    def _choice_handler(self, param_dict, param, choices, values, attr, old, new):
        print("attr=", attr, "old=", old, "opt=", new, "who=", param)
        choice_dict = dict(zip(choices, values))
        self.param_dict[param] = choice_dict[new]

    def _multi_choice_handler(self, param_dict, param, choices, values, attr, old, new):
        print("attr=", attr, "old=", old, "opt=", new, "who=", param)
        active_list = [values[x] for x in new]
        self.param_dict[param] = active_list

    def _single_handler(self, param_dict, param, transform, attr, old, new):
        print("attr=", attr, "old=", old, "who=", param, "new=", new)
        self.param_dict[param] = transform(new)

    def make_choice(self, choices, values, default, param, param_dict):
        radio = Select(options=choices, value=choices[default], title=param,name=param)
        radio.on_change(
            "value",
            partial(self._choice_handler,  param_dict, param, choices, values),
        )
        return radio

    def make_multi_choice(self, choices, values, default, param, param_dict):
        checkbox = CheckboxGroup(labels=choices, inline=False,name=param)
        checkbox.on_change(
            "active",
            partial(
                self._multi_choice_handler, param_dict, param, choices, values
            ),
        )
        return checkbox

    def make_float(self, default, param, param_dict):
        area = TextInput(value=str(default), title=param,name=param)
        area.on_change(
            "value",
            partial(self._single_handler,  param_dict, param, lambda x: float(x)),
        )
        return area

    def make_int(self, default, param, param_dict):
        area = TextInput(value=str(default), title=param,name=param)
        area.on_change(
            "value",
            partial(self._single_handler,  param_dict, param, lambda x: int(x)),
        )
        return area

    def make_color(self, default, param, param_dict):
        picker = ColorPicker(color=default, title=param,name=param)
        picker.on_change(
            "color", partial(self._single_handler,  param_dict, param, lambda x: x)
        )
        return picker

    def make_string(self, default, param, param_dict):
        area = TextInput(value="Title", title=param,name=param)
        area.on_change(
            "value",
            partial(self._single_handler, param_dict, param, lambda x: x)
            )
        return area
