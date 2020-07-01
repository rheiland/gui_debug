import ipywidgets as widgets
import os
import glob
import shutil
import math
import datetime
import tempfile
from about import AboutTab
from pathlib import Path
import platform
import subprocess
from debug import debug_view

# create the tabs, but don't display yet
about_tab = AboutTab()

tab_height = 'auto'
#tab_layout = widgets.Layout(width='auto',height=tab_height, overflow_y='scroll',)   # border='2px solid black',
tab_layout = widgets.Layout(width='auto',height=tab_height)   # border='2px solid black',

titles = ['About']
tabs = widgets.Tab(children=[about_tab.tab,],
                   _titles={i: t for i, t in enumerate(titles)},
                   layout=tab_layout)

gui = widgets.VBox(children=[tabs,])