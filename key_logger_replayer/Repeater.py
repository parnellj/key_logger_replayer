from __future__ import division

import os
import time
import win32com
import sys
import datetime
import pythoncom, pyHook
import win32com.client as comclt

INPATH = os.path.join('.', 'inputs')
OUTPATH = os.path.join('.', 'outputs')

def get_strokes():
    with open(os.path.join(INPATH, 'test.txt'), 'r') as f:
        mylist = [(float(i.split(' ')[0]), int(i.split(' ')[1][:-1])) for i in f]
    return mylist

def OnKeyboardEvent(event):
    if int(event.Ascii) == 81:
        times = get_strokes()
        print times
        for t, k in times:
            time.sleep(t / 100)
            wsh.SendKeys(chr(k))
    return True

wsh = comclt.Dispatch("Wscript.Shell")

if __name__ == '__main__':
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()
