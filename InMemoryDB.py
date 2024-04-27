class InMemoryDB:

    def __init__(self):
        self.prevVersion = {}
        self.curVersion = {}
        self.notCommitted = {}
        self.transaction = False

    def get(self, key: str):
        print(self.curVersion.get(key, "Null"))
        return
    
    def put(self, key: str, val: int):
        if (not self.transaction):
            print("Error: A transaction has not been initiated")
            return
        self.notCommitted[key] = val
        return

    def begin_transaction(self):
        self.transaction = True
        return

    def commit(self):
        if (not self.transaction):
            print("Error: A transaction has not been initiated")
            return
        self.prevVersion = self.curVersion
        self.curVersion = self.notCommitted
        self.transaction = False
        return

    def rollback(self):
        if (not self.transaction):
            print("Error: A transaction has not been initiated")
            return
        self.notCommitted = self.curVersion
        return