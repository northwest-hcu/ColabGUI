import IPython
from IPython.display import display, HTML
from google.colab.output import eval_js, register_callback

class GUI:
    def __init__(self):
        self.widgets = list()
    def initialize(self, widget, content):
        content = '''
            <div id="gui_main"></div>
            <script></script>
            '''
        
