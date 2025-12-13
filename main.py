def get_book_text():

        with open(frankenstein.txt,'r', encoding="utf-8") as f:
            file_contents = f.read()
        return file_contents
