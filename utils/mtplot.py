import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Legend
from bokeh.models import DataRange1d
import json

annotation='''{"type": {"0": "tRNA", "1": "rRNA", "2": "tRNA", "3": "rRNA", "4": "tRNA", "5": "mRNA", "6": "tRNA", "7": "tRNA", "8": "tRNA", "9": "mRNA", "10": "tRNA", "11": "tRNA", "12": "tRNA", "13": "tRNA", "14": "tRNA", "15": "mRNA", "16": "tRNA", "17": "tRNA", "18": "mRNA", "19": "tRNA", "20": "mRNA", "21": "mRNA", "22": "mRNA", "23": "tRNA", "24": "mRNA", "25": "tRNA", "26": "mRNA", "27": "mRNA", "28": "tRNA", "29": "tRNA", "30": "tRNA", "31": "mRNA", "32": "mRNA", "33": "tRNA", "34": "mRNA", "35": "tRNA", "36": "tRNA"}, "start": {"0": 577, "1": 648, "2": 1602, "3": 1671, "4": 3230, "5": 3307, "6": 4263, "7": 4329, "8": 4402, "9": 4470, "10": 5512, "11": 5587, "12": 5657, "13": 5761, "14": 5826, "15": 5904, "16": 7446, "17": 7518, "18": 7586, "19": 8295, "20": 8366, "21": 8527, "22": 9207, "23": 9991, "24": 10059, "25": 10405, "26": 10470, "27": 10760, "28": 12138, "29": 12207, "30": 12266, "31": 12337, "32": 14149, "33": 14674, "34": 14747, "35": 15888, "36": 15956}, "end": {"0": 647, "1": 1601, "2": 1670, "3": 3229, "4": 3304, "5": 4262, "6": 4331, "7": 4400, "8": 4469, "9": 5511, "10": 5579, "11": 5655, "12": 5729, "13": 5826, "14": 5891, "15": 7445, "16": 7514, "17": 7585, "18": 8269, "19": 8364, "20": 8572, "21": 9207, "22": 9990, "23": 10058, "24": 10404, "25": 10469, "26": 10766, "27": 12137, "28": 12206, "29": 12265, "30": 12336, "31": 14148, "32": 14673, "33": 14742, "34": 15887, "35": 15953, "36": 16023}, "name": {"0": "MT-TF-201", "1": "MT-RNR1-201", "2": "MT-TV-201", "3": "MT-RNR2-201", "4": "MT-TL1-201", "5": "MT-ND1-201", "6": "MT-TI-201", "7": "MT-TQ-201", "8": "MT-TM-201", "9": "MT-ND2-201", "10": "MT-TW-201", "11": "MT-TA-201", "12": "MT-TN-201", "13": "MT-TC-201", "14": "MT-TY-201", "15": "MT-CO1-201", "16": "MT-TS1-201", "17": "MT-TD-201", "18": "MT-CO2-201", "19": "MT-TK-201", "20": "MT-ATP8-201", "21": "MT-ATP6-201", "22": "MT-CO3-201", "23": "MT-TG-201", "24": "MT-ND3-201", "25": "MT-TR-201", "26": "MT-ND4L-201", "27": "MT-ND4-201", "28": "MT-TH-201", "29": "MT-TS2-201", "30": "MT-TL2-201", "31": "MT-ND5-201", "32": "MT-ND6-201", "33": "MT-TE-201", "34": "MT-CYB-201", "35": "MT-TT-201", "36": "MT-TP-201"}, "length": {"0": 71, "1": 954, "2": 69, "3": 1559, "4": 75, "5": 956, "6": 69, "7": 72, "8": 68, "9": 1042, "10": 68, "11": 69, "12": 73, "13": 66, "14": 66, "15": 1542, "16": 69, "17": 68, "18": 684, "19": 70, "20": 207, "21": 681, "22": 784, "23": 68, "24": 346, "25": 65, "26": 297, "27": 1378, "28": 69, "29": 59, "30": 71, "31": 1812, "32": 525, "33": 69, "34": 1141, "35": 66, "36": 68}, "color": {"0": "pink", "1": "lightgray", "2": "pink", "3": "lightgray", "4": "pink", "5": "lightblue", "6": "pink", "7": "pink", "8": "pink", "9": "lightblue", "10": "pink", "11": "pink", "12": "pink", "13": "pink", "14": "pink", "15": "lightblue", "16": "pink", "17": "pink", "18": "lightblue", "19": "pink", "20": "lightblue", "21": "lightblue", "22": "lightblue", "23": "pink", "24": "lightblue", "25": "pink", "26": "lightblue", "27": "lightblue", "28": "pink", "29": "pink", "30": "pink", "31": "lightblue", "32": "lightblue", "33": "pink", "34": "lightblue", "35": "pink", "36": "pink"}}'''

_annotation = pd.DataFrame.from_dict(json.loads(annotation))


def mitoplot(y,title=None, color='blue'):
    '''Show data indexed by mitochondrial position on annotated plot. Positions are 0-based.
    Data should be an array of length 16569.  Blue is mRNA, pink is tRNA, gray is rRNA, white is
    non-coding regions of the mitochondrial genome -- reference RCRS.'''

    figure_options = dict(plot_width=1000,
                          plot_height=300,
                          tools="xpan,xwheel_zoom,reset",
                          background_fill_color='beige',
                          x_range=DataRange1d(bounds='auto', range_padding=0),
                          y_range=DataRange1d(range_padding=0),
                          toolbar_location='right')

    p1 = figure(title=title, **figure_options)
    p1.xgrid.visible = False
    p1.ygrid.visible = False

    quads = {}
    legend_items = []

    M = 1.4*np.max(y)

    for x in ['mRNA', 'tRNA', 'rRNA']:
        A = ColumnDataSource(_annotation[_annotation['type'] == x])
        quads[x] = p1.quad(left='start', right='end', bottom=0, top=M, source=A,  color='color')
        legend_items.append((x, [quads[x]]))

    dloop = p1.quad(left=0, right=0, bottom=-.2, top=M, color='beige')
    legend_items.append(('ctrl', [dloop]))

    legend_attrs = dict(orientation='horizontal',
                        margin=2,
                        padding=2,
                        spacing=5,
                        glyph_width=10,
                        label_text_font_size='8pt')

    legend = Legend(items=legend_items, **legend_attrs)

    p1.add_line(y,color=color)
    p1.add_layout(legend, 'center')

    return p1

