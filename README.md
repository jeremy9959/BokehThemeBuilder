## BokehModelBuilder

<table>
<tr><td><img src="bokeh_sample.png" width=200 /></td><td><img src="twisted_bokeh.png" width=200/> </td></tr>
</table>

[bokeh](http://bokeh.org) is a library for generating interactive graphics and dashboards in python. 
Every component offers a myriad of customizing options, and I find it impossible to keep track of them.
This tool (very much under development) offers a graphical interface to those options. I imagine the user
working with this tool to prepare a plot format that they like, and then obtaining code from the tool
that they can include in whatever bokeh project they are working on.

As your theme evolves for a given tab, that tab will display a python statement of the form
```
PLOT_OPTIONS = {'background_fill_alpha':'#efefef',...}
```
You can copy these into a file [following the strategy outlined in this post](https://blog.bokeh.org/posts/styling-bokeh).
to create a "styling dictionary."


The trial.py file is a bokeh server app that loads the widgets.py and options.py modules.  You run it like this:
```
$ bokeh serve trial.py
```
and navigate in your browser to localhost port 5006.



<img src="ui.png" width=300/>


