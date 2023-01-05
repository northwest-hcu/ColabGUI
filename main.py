import IPython
from IPython.display import display, HTML, Javascript
from google.colab.output import eval_js, register_callback
from google.colab import drive, output

drive.mount('/rootingColabGUI')
HOME_PATH = '../rootingColabGUI/MyDrive/colabGUI'
fp = open(HOME_PATH + '/gui.js', 'r')
gui_js = fp.read()
fp.close()
fp = open(HOME_PATH + '/default.css', 'r')
default_css = fp.read()
fp.close()

def testFunc():
  print('test done')

display(HTML("<div id='colab_gui_main'></div>"))
display(HTML('<style>' + (default_css) + '</style>'))
display(HTML('<script>' + (gui_js) + '</script>'))
output.register_callback('n.testFunc', testFunc)
eval_js("const c = new ColabGUIButton('test');c.setClickEvent('n.testFunc');")