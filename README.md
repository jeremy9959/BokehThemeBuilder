## BokehThemeBuilder


[bokeh](http://bokeh.org) is a library for generating interactive graphics and dashboards in python. 
Every component offers a myriad of customizing options, and I find it impossible to keep track of them.
This tool (very much under development) offers a graphical interface to those options. I imagine the user
working with this tool to prepare a plot format that they like, and then obtaining code from the tool
that they can include in whatever bokeh project they are working on.

As your theme evolves, the page will show yaml code to the right of your plot. 
You can download this yaml code by clicking the download button (creating the file ```theme.yaml```) or just
copy this yaml into a file to create a bokeh theme. [This blog post](https://blog.bokeh.org/posts/styling-bokeh)
explains how to use the theme file to style your plots.

This [valentines theme](themes/valentines.yaml) is an example created by this tool:

<center>
<img src="images/valentines.png" width=100>
</center>

<img src="images=theme.gif" width=300> 


The main.py file is a bokeh server app that loads the widgets.py and options.py modules.  You run it like this:
```
$ bokeh serve .
```
and navigate in your browser to localhost port 5006.

You can also try it directly from heroku by going to [the heroku app page](http://bokehthemebuilder.herokuapp.com).

The utils directory includes the file ```structure.py``` where you can find the ```BokehStructureGraph```
class. This can be used to analyze models and determine which attributes are available for customization.
Using this class on the simple figure

<img src="images/simple.png" width=200>

yields this interactive display:

<img src="images/peek.gif" width=300>

These two images were created in a jupyter notebook using this code:

```
from utils.structure import BokehStructureGraph
from bokeh.plotting import figure, show, output_notebook
output_notebook()
# draw the easy figure
f = figure(height=200,width=200)
f.line(x=[1,2,3],y=[1,2,3])
f.circle(x=[3,2,1],y=[1,2,3],size=10, color='red')
show(f)
# now draw the structure graph with interactive datatable
show(BokehStructureGraph(f).model)
```






