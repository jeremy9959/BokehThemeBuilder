## BokehModelBuilder

<img src="images/ui.png" width=300/>

[bokeh](http://bokeh.org) is a library for generating interactive graphics and dashboards in python. 
Every component offers a myriad of customizing options, and I find it impossible to keep track of them.
This tool (very much under development) offers a graphical interface to those options. I imagine the user
working with this tool to prepare a plot format that they like, and then obtaining code from the tool
that they can include in whatever bokeh project they are working on.

As your theme evolves, the page will show a series of python statements of the form
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

You can also try it directly from heroku by going to [the heroku app page](http://bokehmodelbuilder.herokuapp.com).






