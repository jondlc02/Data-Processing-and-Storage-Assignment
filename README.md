## How to Run

An example file for utilizing the `InMemoryDB` class has been included in the repository called `DB_Example.py`. The file includes commands from the figure in the assignment page as well as how to attach the class to a Python file.

### Running the Example File (`DB_Example.py`)

To run the example file, follow these steps:

1. Ensure that `InMemoryDB.py` and `DB_Example.py` are in the same directory.
2. Open a terminal or command prompt.
3. Navigate to the directory containing both files.
4. Run the following command:

    python DB_Example.py

### Creating a New File Using `InMemoryDB` Class

To create a new file using the `InMemoryDB` class, follow these steps:

1. Create a new `.py` file with any name you choose.
2. At the beginning of the file, include the following line:

    from InMemoryDB.py import InMemoryDB

3. You can now create an instance of the DB with the following line of code:

    <Name of the DB> = InMemoryDB()

### Running Your File

To run the file you created, follow these steps:

1. Save the file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing both files.
4. Run the following command, replacing `<Name of Your File>` with the name of your file:

    python <Name of Your File>.py

---

There are a few ways this assignment could be altered into an "official" assignment. One change I suggest would be
to limit the applicable languages for this assignment to only use SQL or something similar. Limiting to only one
language would make grading easier too because then you could create a single file to test the student's submissions.
SQL is a widely sought after skill in the current job market, and working with the language at least a little could
better prepare students for the future.