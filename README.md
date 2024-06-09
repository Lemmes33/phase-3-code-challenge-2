# Object Relations Code Challenge - Articles

For this assignment, we'll be working with a Article domain.

We have three models: `Aothor`, `Article`, and `Magazine`.

For our purposes, a `Author` has many `Articles`, a `Magazine` has many `Articles`s,
and a `Article` belongs to a `Author` and to a `Magazine`.

`Author` - `Magazine` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory. Then run
`pipenv shell` to jump into the shell.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has `pytest` tests available to you. Run
`pytest` at any time from within your virtual environment.

We've provided you with another tool that you can use to test your code. To use
it, run `python debug.py` from the command line. This will start a `ipdb`
session with your classes defined. You can test out the methods that you write
here. You can add code to the `debug.py` file to define variables and create
sample instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

---

## Deliverables

Write the following properties and methods in the classes in the files provided.
Feel free to build out any helper methods if needed.

### Initializers and Properties

#### Author

- `Author __init__(self, name, hometown)`
  - Author is initialized with a name and hometown
- `Author property name`
  - Returns the Author's name
  - Names must be of type `str`
  - Must be greater than zero characters
  - Should **be able** to change after the Author is instantiated
- `Author property hometown`
  - Returns the Author's hometown
  - Hometowns must be of type `str`
  - Must be greater than zero characters
  - Should **not be able** to change after the Author is instantiated
  - _hint: hasattr()_

#### Magazine

- `Magazine __init__(self, name, city)`
  - Magazine is initialized with a name and city
- `Magazine property name`
  - Returns the Magazine's name
  - names must be of type `str`
  - Must be greater than zero characters
  - Should **be able** to change after the Magazine is instantiated
- `Magazine property city`
  - Returns the Magazine's city
  - Cities must be of type `str`
  - Must be greater than zero characters
  - Should **be able** to change after the Magazine is instantiated

#### Article

- `Article __init__(self, date, Author, Magazine)`
  - Article is initialized with a date, a `Author` instance, and `Magazine` instance
- `Article property date`
  - Returns the Article's date
  - Dates must be of type `str`
  - Must be greater than zero characters
  - Should **be able** to change after the Article is instantiated

### Object Relationship Methods and Properties

#### Article

- `Article Author`
  - Returns the `Author` instance for this Article
  - Must be of type `Author`
  - Should **be able** to change after the Article is instantiated
- `Article Magazine`
  - Returns the `Magazine` instance for this Article
  - Must be of type `Magazine`
  - Should **be able** to change after the Article is instantiated

#### Magazine

- `Magazine Articles()`
  - Returns a list of all the Articles for the Magazine
  - Articles must be of type `Article`
  - Returns `None` if there are no Articles for that Magazine
- `Magazine Authors()`
  - Returns a **unique** list of all the Authors for the Magazine
  - Authors must be of type `Author`
  - Returns `None` if there are no Articles for that Magazine

#### Author

- `Author property Articles()`
  - Returns a list of all the Articles that the Author has played in
  - Articles must be of type `Article`
  - Returns `None` if there are no Articles for that Author
- `Author property Magazines()`
  - Returns a **unique** list of all the Magazines that the Author has played in
  - Magazines must be of type `Magazine`
  - Returns `None` if there are no Articles for that Author

### Aggregate and Association Methods

#### Article

- `Article hometown_show()`
  - Returns `True` if the Article is in the Author's hometown
  - Returns `False` if it is not
- `Article introduction()`
  - Returns a string with the Author's introduction for this Article
  - An introduction is in the form:
    `"Hello {insert city name here}!!!!! We are {insert Author name here} and we're from {insert hometown here}"`

#### Author

- `Author play_in_Magazine(Magazine, date)`
  - Takes a `Magazine` instance and a date as arguments
  - Creates and returns a new Article object for the Author in that Magazine on that
    date
- `Author all_introductions()`
  - Returns a list of strings representing all the introductions for this Author
  - Each introduction is in the form
    `"Hello {insert city name here}!!!!! We are {insert Author name here} and we're from {insert hometown here}"`
  - Returns `None` if there are no Articles

### Bonus: Aggregate and Association Method

#### Magazine

- `Magazine Article_on(date)`
  - Takes a date (string) as argument
  - Finds and returns the first Article object on that date at that Magazine
  - Returns `None` if there is no Article on that date at that Magazine
  - Uncomment lines 136-146 in the Magazine_test file

### Bonus: For any invalid inputs raise an `Exception`.

- First, **comment out** the following lines
  - **Author_test.py**
    - lines 26-27, 39-40, 60-62, 65-66, 82-83
  - **Article_test.py**
    - lines 27-28, 43-44, 65-66, and 100-101
  - **Magazine_test.py**
    - lines 24-25, 37-38, 60-61, and 73-74
- Then, **uncomment** the following lines in the test files
  - **Author_test.py**
    - lines 30-31, 43-44, 69-70, 73-74, and 86-87
  - **Article_test.py**
    - lines 31-32, 47-48, 71-72, and 106-107
  - **Magazine_test.py**
    - lines 28-29, 41-42, 64-65, and 77-78
# phase-3-code-challenge-2
