from bokeh.models import *


def recur_show(obj):
    for x in obj.properties_with_refs():
        if not isinstance(getattr(obj,x),list):
            try:
                print(x,getattr(obj,x).references())
            except AttributeError:
                continue
        else:
            if len(getattr(obj,x))>0:
                print(x,end="\t")
            for z in getattr(obj,x):
                print(z,end="\t")
                recur_show(z)
                

def show_basics(obj):
    for x in (obj.properties()-obj.properties_with_refs()):
        print(x,getattr(obj,x))
        
        
        
def obj_props_to_df(obj):
    obj_dict = obj.properties_with_values()
    types = [obj.lookup(x) for x in obj_dict.keys()]
    return pd.DataFrame.from_dict({'props':list(obj_dict.keys()), 'values':list(obj_dict.values()),'types':types})

def obj_props_to_df2(obj):
    tp = type(obj)
    obj_dict = obj.properties_with_values()
    types = [obj.lookup(x) for x in obj_dict.keys()]
    docs = [getattr(type(obj),x).__doc__ for x in obj_dict.keys()]
    return pd.DataFrame.from_dict({'props':list(obj_dict.keys()), 'values':list(obj_dict.values()),'types':types,'doc':docs})


D = {"choices":{},"strings":{},"ints":{},"floats":{},"colors":{}}
fonts = ['helvetica','arial','calibri']
font_sizes = ['10pt','12pt','16pt','24pt','32pt']
dash_patterns = ['solid', 'dashed', 'dotted', 'dotdash', 'dashdot']


def disassemble(object):
    ct=0
    axis_df = obj_props_to_df2(object)
    for x in axis_df.iterrows():
        attr, kind, value = x[1]['props'],str(x[1]['types']), x[1]['values']
        if kind[:4] == "Bool":
            options=['True','False']
            D['choices'].update({attr:(options,[True, False])})
            ct+=1
            continue
        if kind[:4]=="Enum":
            options = kind[5:-1].split(',')
            options = [x.strip().strip("'") for x in options]
            D['choices'].update({attr:(options,options)})
            ct+=1
            continue
        if kind[:4]=="Numb":
            D['floats'].update({attr:value['value']})
            ct+=1
            continue
        if kind[:3]=="Int" or kind[:6]=="NonNeg":
            try:
                D['ints'].update({attr:int(value)})
            except TypeError:
                D['ints'].update({attr:0})
            ct+=1
            continue
        if kind[:4]=="Colo":
            try:
                D['colors'].update({attr:value['value']})
            except:
                D['colors'].update({attr:None})
            ct+=1
            continue
        if kind[:4]=="Floa":
            try:
                D['floats'].update({attr:float(value)})
            except TypeError:
                D['floats'].update({attr:float(0.0)})
            ct+=1
            continue
        if kind[:5]=="FontS":
            D['choices'].update({attr:(font_sizes,font_sizes)})
            ct+=1
            continue
        if kind[:4]=="Stri":
            D['strings'].update({attr:str(value)})
            ct+=1
            continue
        if kind[:4]=="Dash":
            D['choices'].update({attr:(dash_patterns,dash_patterns)})
            ct+=1
            continue
        print('cant handle {} of type {}'.format(attr,kind))
    print('found {} items'.format(ct))
    return D
