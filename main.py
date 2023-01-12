import IPython, time, pprint
from IPython.display import display, HTML, Javascript
from google.colab.output import eval_js, register_callback
from google.colab import drive, output

drive.mount('/rootingColabGUI')
HOME_PATH = '../rootingColabGUI/MyDrive/colabGUI'
fp = open(HOME_PATH + '/ColabGUIButton.js', 'r')
colab_gui_button_js = fp.read()
fp.close()
fp = open(HOME_PATH + '/ColabGUIInput.js', 'r')
colab_gui_input_js = fp.read()
fp.close()
fp = open(HOME_PATH + '/default.css', 'r')
default_css = fp.read()
fp.close()

valStore = dict()

def testFunc():
  print('test done')

def testGetter(key, value):
  global valStore
  valStore[key] = value

def getValue(key):
  global valStore
  js = "document.querySelector('#" + key + " .input_text').getValue();"
  print(js)
  eval_js(js)
  return valStore[key]

display(HTML("<div id='colab_gui_main'></div>"))
display(HTML('<style>' + (default_css) + '</style>'))
display(HTML('<script>' + (colab_gui_button_js) + '</script>'))
display(HTML('<script>' + (colab_gui_input_js) + '</script>'))
output.register_callback('n.testFunc', testFunc)
output.register_callback('n.testGetter', testGetter)

display(HTML("<script>const c_btn = new ColabGUIButton('test_btn');c_btn.setClickEvent('n.testFunc');</script>"))
display(HTML("<script>const c_input = new ColabGUIInput('test_input');</script>"))

print(getValue('testInput'))
