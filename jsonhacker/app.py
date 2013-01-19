import logging
import wx

class JsonHacker(wx.App):
    APP_NAME = "JSON Hacker"
    PACKAGE = "json-hacker"
    
    def __init__(self, *args, **kwargs):
        wx.App.__init__(self, *args, **kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug("wxPython "+wx.version())
        self._init_frame()
        
    def _init_frame(self):
        self.frame = wx.Frame(None, wx.ID_ANY, self.APP_NAME)
        self.frame.Show(True)
    
