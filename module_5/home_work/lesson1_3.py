class BlockErrors:

    def __init__(self, errors):
        self.errors = errors

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return True
        elif exc_type in self.errors:
            return True
        elif Exception in self.errors:
            return True
        else:
            return False
