import IPython
from IPython.display import display, HTML
from google.colab.output import eval_js, register_callback

class Button:
    def __init__(self, key):
        self.key = key       # HTML element id
        self.type = 'Button'
        self.tags = list()    # HTML element class

    def show(self):
        content = '<div class="colab_gui" id="'
        content += self.key
        content += '">'
        content += '<div class="'
        content += ' '.join(self.tags)
        content += '">送信</div>'
        content += '</div>'

        display(HTML(content))