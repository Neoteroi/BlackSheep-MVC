from blacksheep.server.controllers import Controller, get


class Home(Controller):

    @get()
    def index(self):
        # NB: since the view function is called without parameters, the name is obtained from the
        # calling request handler ('index')
        return self.view()  # <-- returns by default /views/home/index.html

    @get(...)  # <-- Since ellipsis is used here, the route takes the name of the request handler: '/about'
    def about(self):
        return self.view()  # <-- returns by default /views/home/about.html


