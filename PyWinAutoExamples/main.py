from pywinauto.application import Application
import os

app = Application(backend="uia").start(os.path.dirname(os.path.abspath(__file__)) + '\\WpfApp1.exe')
print('\n'.join([str(x) for x in app.top_window().children()]))
print('---')
app.top_window().print_control_identifiers()
app.top_window().child_window(title='Exit', control_type="Button").print_control_identifiers()

#child_window(title="Exit", auto_id="exit", control_type="Button")
app.diag.exit.click()

#app.kill()

# describe the window inside Notepad.exe process
#dlg_spec = app.MainWindow
# wait till the window is really open
#actionable_dlg = dlg_spec.wait('visible')