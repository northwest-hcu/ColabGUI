import IPython
from IPython.display import display, HTML
from google.colab.output import eval_js, register_callback

class GUI:
    def __init__(self):
        self.widgets = dict()

    # set layout widget with unique key
    def setWidget(self, key, widget):
        self.widgets[key] = widget
    
    # initialize gui objects
    def initialize(self):
        content = '''
            <div id = "colab_gui_main"></div>
            <script href = "./gui.js"></script>
            '''
        display(HTML(content))
        
        for widget in self.widgets:
            widget.show()
