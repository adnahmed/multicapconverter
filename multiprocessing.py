class multipocessing:  # Fake multiprocessing, not multiprocessing at all
    def __init__(self, target, args):
        self.target = target
        self.args = args

    @staticmethod
    def Process(target, args):
        return multiprocessing(target, args)

    def start(self):
        self.target(*self.args)

    def join(self):
        pass
