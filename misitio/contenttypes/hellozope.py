from Products.Five import BrowserView

class Hellozope(BrowserView):
    """
    clase que manipula la platilla de la vista.
    """
    
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return "hello"
