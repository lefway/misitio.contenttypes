from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.publisher.browser import BrowserPage
from Products.Five.browser import BrowserView

class Helloviewlet(BrowserView):
    """
    clase que manipula la platilla de la vista.
    """
    template = ViewPageTemplateFile('helloviewlet.pt')

    def __init__(self, context, request, view, manager):
        self.context = context
        self.request = request
        self.__parent__ = view

    def update(self):
        self.message = "hello mensaje desde hellowiewlet.py"
