class PersistenceManager:
    @staticmethod
    def save_to_file(file_content, filename):
        file = open(filename, 'w')
        file.write(str(file_content))
        file.close()