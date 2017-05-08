from Processor import Processor


class ProcessingManager:
    class __ProcessingManager:
        def __init__(self, arg):
            self.val = arg
            Processor()

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):
        if not ProcessingManager.instance:
            ProcessingManager.instance = ProcessingManager.__ProcessingManager(arg)
        else:
            ProcessingManager.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)
