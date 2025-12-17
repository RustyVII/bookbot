import sys
import os
import urllib.request

from stats import number_of_symbols
from stats import countnumberofwords

USAGE = "Usage: python3 main.py <path_to_book>"

def read_local_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

def fetch_url(url):
    with urllib.request.urlopen(url) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")

def main():
    if len(sys.argv) != 2:
        print(USAGE)
        return 1

    arg = sys.argv[1]
    content = None
    if arg.startswith("http://") or arg.startswith("https://"):
        try:
            content = fetch_url(arg)
        except Exception as e:
            print(f"Failed to fetch URL: {e}")
            return 1
    else:
        # check absolute/relative path
        if os.path.isfile(arg):
            content = read_local_file(arg)
        else:
            # try in books/ directory
            books_dir = os.path.join(os.path.dirname(__file__), "books")
            candidate = os.path.join(books_dir, arg)
            if os.path.isfile(candidate):
                content = read_local_file(candidate)
            else:
                print(f"File not found: {arg}")
                print(USAGE)
                return 1
    countnumberofwords(content)
    number_of_symbols(content)
    return 0

if __name__ == '__main__':
    sys.exit(main())

