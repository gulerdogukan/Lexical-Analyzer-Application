class File:
    # This method is opening the external file for reading, and I'm using the handling exception, that handle
    # OSError, which give error and print the msg below, in case that the file does not exit or the disk is full.
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            file = open(self.file_name, 'r', encoding='utf-8')
        except OSError:
            print("Something Wrong!!, Couldn't access the file.")

    def read_from_file(self):
        input_token = []
        file = open(self.file_name, 'r', encoding='utf-8')
        for line in file:
            line_info = line.split()
            input_token.extend(line_info)
        file.close()
        return input_token
