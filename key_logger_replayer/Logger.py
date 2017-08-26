import win32com
import sys
import datetime
import pythoncom, pyHook
import time
buffer = ''
time_old = time.time()
logging = False

INPATH = os.path.join('.', 'inputs')
OUTPATH = os.path.join('.', 'outputs')

def OnKeyboardEvent(event):
    global logging, time_old
    if int(event.Ascii == 81):
        logging = True
        time_old = time.time()
        return
    if logging:
        with open(os.path.join(INPATH, 'test.txt'), 'a') as f:
            time_new = time.time()
            f.writelines('{0}'.format((time_new - time_old) * 100) + ' ' + str(long(event.Ascii)) + '\n')
            time_old = time_new

while True:
    with open(os.path.join(INPATH, 'test.txt'), 'w') as f:
        pass
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()
