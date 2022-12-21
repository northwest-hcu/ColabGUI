import IPython
from IPython.display import display, HTML, Javascript
from google.colab.output import eval_js, register_callback
from google.colab import drive 

drive.mount('/colabGUI')

class Button:
    def __init__(self, key, label='Push', font_color='black', bg_color='white'):
        self.key = key       # HTML element id
        self.type = 'Button'
        self.tags = list()    # HTML element class
        self.font_color = font_color
        self.bg_color = bg_color
        self.label = label

    def show(self):
        fp = open('./gui.js')
        content = fp.read()
        fp.close()
        display(HTML('<div id="colab_gui_main"></div><script>' + content + '</script>'))
        content = 'ColabGUIButton(' + self.key + ',' + self.label + ', {font_color:' + self.font_color + ', bg_color:' + self.bg_color + '})'
        eval_js(content)