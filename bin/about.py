from ipywidgets import Output
from IPython.display import display, HTML

class AboutTab(object):

    def __init__(self):
        # self.tab = Output(layout={'height': '900px'})
        # self.tab = Output(layout={height=’85%’,min_height=’350px’})
        self.tab = Output(layout={'height': 'auto'})

        # WHY? -good works; -bad, doesn't
        # self.tab.append_display_data(HTML(filename='doc/about-good.html'))
        self.tab.append_display_data(HTML(filename='doc/about-bad.html'))
        
