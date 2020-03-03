from notebook import *


if __name__ == "__main__":
    # Testing for object
    note = Note  # create an object
    print(note.__doc__)
    print(note, type(note))  # object class
    print(isinstance(note, object))  # we prove that note is object
    print(dir(Note))
    print(dir(note))

    # Testing attributes
    note = Note("Hello World", 'hello')
    print(note.memo, note.tags)  # memo and task are the attributes of class Note
    print(note.__getattribute__)
    print(type(note.memo))

    # Testing class methods
    note = Note("Hello World", 'Hello')
    print(note.match(note.tags))
    print(type(Note.match), type(note.match))

    # Testing __init__ & __str__ methods
    print(note.__init__)
    print(note)
