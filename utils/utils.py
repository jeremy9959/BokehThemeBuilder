from bokeh.models import *
import pandas as pd


# some constants of use later
fonts = ["helvetica", "arial", "calibri"]
font_sizes = ["10pt", "12pt", "16pt", "24pt", "32pt"]
dash_patterns = ["solid", "dashed", "dotted", "dotdash", "dashdot"]


def obj_props_to_df2(obj):
    """Returns a pandas dataframe of the properties of a bokeh model, each row having
    an attribute, its type (a bokeh property), and the docstring."""
    obj_dict = obj.properties_with_values()
    types = [obj.lookup(x) for x in obj_dict.keys()]
    docs = [getattr(type(obj), x).__doc__ for x in obj_dict.keys()]
    return pd.DataFrame.from_dict(
        {
            "props": list(obj_dict.keys()),
            "values": list(obj_dict.values()),
            "types": types,
            "doc": docs,
        }
    )


def disassemble(object):
    """Given an instance of a bokeh model, takes a stab at constructing a dict that can
    be used in options.py to set options for that model.  Not perfect, so reports its failures."""
    D = {"choices": {}, "strings": {}, "ints": {}, "floats": {}, "colors": {}}
    ct = 0
    axis_df = obj_props_to_df2(object)
    for x in axis_df.iterrows():
        attr, kind, value = x[1]["props"], str(x[1]["types"]), x[1]["values"]
        if kind[:4] == "Bool":
            options = ["True", "False"]
            D["choices"].update({attr: (options, [True, False])})
            ct += 1
            continue
        if kind[:4] == "Enum":
            options = kind[5:-1].split(",")
            options = [x.strip().strip("'") for x in options]
            D["choices"].update({attr: (options, options)})
            ct += 1
            continue
        if kind[:4] == "Numb":
            try:
                D["floats"].update({attr: value["value"]})
            except TypeError:
                D["floats"].update({attr: None})
            except KeyError:
                print("trouble with ", attr, kind, value)
                continue
            ct += 1
            continue
        if kind[:3] == "Int" or kind[:6] == "NonNeg":
            try:
                D["ints"].update({attr: int(value)})
            except TypeError:
                D["ints"].update({attr: 0})
            ct += 1
            continue
        if kind[:4] == "Colo":
            try:
                D["colors"].update({attr: value["value"]})
            except TypeError:
                D["colors"].update({attr: None})
            ct += 1
            continue
        if kind[:4] == "Floa":
            try:
                D["floats"].update({attr: float(value)})
            except TypeError:
                D["floats"].update({attr: float(0.0)})
            ct += 1
            continue
        if kind[:5] == "FontS":
            D["choices"].update({attr: (font_sizes, font_sizes)})
            ct += 1
            continue
        if kind[:4] == "Stri":
            D["strings"].update({attr: str(value)})
            ct += 1
            continue
        if kind[:4] == "Dash":
            D["choices"].update({attr: (dash_patterns, dash_patterns)})
            ct += 1
            continue
        if kind[:4] == "Perc":
            D["floats"].update({attr: float(value)})
            ct += 1
            continue
        if kind.find("Instance") < 0:
            print("cant handle {} of type {}".format(attr, kind))
    print("found {} items".format(ct))
    return D


def explode(F):
    """Given a model, creates a dictionary of options dicts for each submodel referenced
    in the original model.  Keys are model class name concatenated with model instance id"""
    E = {}
    for x in F.references():
        E[x.__class__.__name__ + x.id] = disassemble(x)
    return E


