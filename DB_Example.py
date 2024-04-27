from InMemoryDB import InMemoryDB

inmemoryDB = InMemoryDB()

# Should return "Null" because A doesn't exist in the DB yet
inmemoryDB.get("A")

# Should throw an error because a transaction is not in progress
inmemoryDB.put("A", 5)

# Starts new transaction
inmemoryDB.begin_transaction()

# Sets value of A to 5, but it's not committed yet
inmemoryDB.put("A", 5)

# Should return null, because updates to A are not committed yet
inmemoryDB.get("A")

# Updates A's value to 6 within the transaction
inmemoryDB.put("A", 6)

# Commits open transaction
inmemoryDB.commit()

# Should return 6, that was the last value of A to be committed
inmemoryDB.get("A")

# Throws an error since there is no open transaction
inmemoryDB.commit()

# Throws an error since there is no open transaction
inmemoryDB.rollback()

# Should return null because B does not exist in the database
inmemoryDB.get("B")

# Starts new transaction
inmemoryDB.begin_transaction()

# Set key B’s value to 10 within the transaction
inmemoryDB.put("B", 10)

# Rollback the transaction - revert any changes made to B
inmemoryDB.rollback()

# Should return null because changes to B were rolled back
inmemoryDB.get("B")


