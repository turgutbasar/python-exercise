# TODO : Implement a context manager to access DbMock instance,
# Every time we finish context, commit operations automatically
class DbMock:
    def __init__(self):
        self.data = {}
        self.clone = {}
        self._commit_waiting = False

    def update_record(self, key, value):
        self.clone[key] = value
        self._commit_waiting = True

    def delete_record(self, key):
        if key in self.clone:
            self.clone.pop(key)
            self._commit_waiting = True

    def commit(self):
        self.data = dict(self.clone)
        self._commit_waiting = False
