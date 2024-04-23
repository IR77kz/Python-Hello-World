class HelloWorld:
    def __init__(self) -> None:
        self.hello = "Hello"
        self.world = "World"

    def send(self):
        if self:
            return "{}, {}!".format(self.hello, self.world)
        return "Hello, World! (Can't init <HelloWorld> class)"
