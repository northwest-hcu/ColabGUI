import IPython, json
from IPython.display import display, HTML, Javascript
from google.colab.output import eval_js, register_callback
from google.colab import drive, output

# ドライブの読み込み(自分のドライブのホームにあるcolabGUIのディレクトリから参照)
drive.mount('/rootingColabGUI')
HOME_PATH = '../rootingColabGUI/MyDrive/colabGUI'
fp = open(HOME_PATH + '/ColabGUIButton.js', 'r')
colab_gui_button_js = fp.read()
fp.close()
fp = open(HOME_PATH + '/ColabGUIInput.js', 'r')
colab_gui_input_js = fp.read()
fp.close()
fp = open(HOME_PATH + '/ColabGUIRadio.js', 'r')
colab_gui_radio_js = fp.read()
fp.close()
fp = open(HOME_PATH + '/default.css', 'r')
default_css = fp.read()
fp.close()

# テスト動作関数
def testFunc():
  print('test done')

# 出力場所作成 + 必要情報の入力
display(HTML("<div id='colab_gui_main'></div>"))
display(HTML('<style>' + (default_css) + '</style>'))
display(HTML('<script>' + (colab_gui_button_js) + '</script>'))
display(HTML('<script>' + (colab_gui_input_js) + '</script>'))
display(HTML('<script>' + (colab_gui_radio_js) + '</script>'))


class ColabGUIButton:
  def __init__(self, key):
    self.key = key
    display(HTML("<script>const colabguibtn_{} = new ColabGUIButton('{}');</script>".format(self.key, self.key)))
  def attachEvent(self, event):
    f_name = event.__name__
    print(f_name)
    display(HTML("<script>colabguibtn_{}.setClickEvent('{}');</script>".format(self.key, 'n.' + f_name)))
    output.register_callback('n.' + f_name, event)
  def removeEvent(self, event):
    f_name = event.__name__
    display(HTML("<script>colabguibtn_{}.removeClickEvent('{}');</script>".format(self.key, 'n.' + f_name)))

class ColabGUIInput:
  def __init__(self, key, label = "Input >"):
    self.key = key
    self.label = label
    display(HTML("<script>const colabguiinput_{} = new ColabGUIInput('{}', '{}');</script>".format(self.key, self.key, self.label)))
  def getValue(self):
    js = "colabguiinput_{}.getValue();".format(self.key)
    value = eval_js(js)
    return value
  def setLabel(self, label):
    self.label = label
    js = "colabguiinput_{}.setLabel({});".format(self.key, self.label)
    eval_js(js)

class ColabGUIRadio:
  def __init__(self, key, labels = ["test1", "test2","t3"], values = ["result1", "result2","r3"]):
    self.key = key
    self.labels = labels
    self.values = values
    if len(self.labels) != len(self.values):
      print('Labels and values are not same count.')
      return
    display(HTML("<script>const colabguiradio_{} = new ColabGUIRadio('{}', {}, {});</script>".format(self.key, self.key, str(self.labels), str(self.values))))
  def getValue(self):
    js = "colabguiradio_{}.getValue();".format(self.key)
    value = eval_js(js)
    return value

cb = ColabGUIButton('test_btn')
ci = ColabGUIInput('test_input')
cr = ColabGUIRadio('test_radio')

cb.attachEvent(testFunc)
print(ci.getValue())
print(cr.getValue())

cb.removeEvent(testFunc)
cb.attachEvent(cr.getValue)
