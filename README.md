# gui_debug

## UPDATE: see https://github.com/jupyter-widgets/ipywidgets/issues/1791

![Alt text](why_scroll.jpg?raw=true "Why the scrollbar")

Why does this tab become scrollable when "too much" text is in my .html? Refer bin/about.py:
```
        # self.tab.append_display_data(HTML(filename='doc/about-good.html'))
        self.tab.append_display_data(HTML(filename='doc/about-bad.html'))
```
