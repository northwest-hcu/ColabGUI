import IPython
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

def testFunc():
  print('test done')

def testGetter(arg):
  print(arg)
  return arg

def testActInput():
  display(HTML('<script>c_input.getValue();</script>'))

display(HTML("<div id='colab_gui_main'></div>"))
display(HTML('<style>' + (default_css) + '</style>'))
display(HTML('<script>' + (colab_gui_button_js) + '</script>'))
display(HTML('<script>' + (colab_gui_input_js) + '</script>'))
output.register_callback('n.testFunc', testFunc)
output.register_callback('n.testGetter', testGetter)
display(HTML("<script>const c_btn = new ColabGUIButton('test_btn');c_btn.setClickEvent('n.testFunc');</script>"))
display(HTML("<script>const c_input = new ColabGUIInput('test_input');c_input.getValue();const c_btn2 = new ColabGUIButton('test_btn2');c_btn2.setClickEvent('c_input.getValue');</script>"))
# const 定義が迷子
# idで管理？
time.sleep(2)
testActInput()

