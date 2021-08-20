from Journal import Journal
from PersistenceManager import PersistenceManager

if __name__ == '__main__':
    j = Journal()
    j.add_entry('I ate today')
    j.add_entry('I took a test')
    j.add_entry('I yelled')

    filename = "Journal.txt"
    j.remove_entry(1)
    PersistenceManager.save_to_file(file_content=j, filename=filename)