import sys
import argparse

def wc(files, count_lines=True, count_words=True, count_characters=True):
    total_lines = 0
    total_words = 0
    total_characters = 0

    for file_path in files:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                lines = content.count('\n')
                words = len(content.split())
                characters = len(content)

                if count_lines:
                    total_lines += lines
                if count_words:
                    total_words += words
                if count_characters:
                    total_characters += characters

                if count_lines and not count_words and not count_characters:
                    print(f"{lines}\t{file_path}")
                elif count_words and not count_lines and not count_characters:
                    print(f"{words}\t{file_path}")
                elif count_characters and not count_lines and not count_words:
                    print(f"{characters}\t{file_path}")
                else:
                    print(f"{lines}\t{words}\t{characters}\t{file_path}")

        except FileNotFoundError:
            print(f"wc: {file_path}: No such file or directory")
            return 1  # File not found error

        except Exception as e:
            print(f"wc: Error: {e}")
            return 2  # Other errors

    if len(files) > 1 and (count_lines or count_words or count_characters):
        if count_lines and not count_words and not count_characters:
            print(f"{total_lines}\ttotal")
        elif count_words and not count_lines and not count_characters:
            print(f"{total_words}\ttotal")
        elif count_characters and not count_lines and not count_words:
            print(f"{total_characters}\ttotal")
        else:
            print(f"{total_lines}\t{total_words}\t{total_characters}\ttotal")

    return 0  # Success

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Word count utility with flags.")
    parser.add_argument('-l', '--lines', action='store_true', help='Count lines only')
    parser.add_argument('-w', '--words', action='store_true', help='Count words only')
    parser.add_argument('-c', '--characters', action='store_true', help='Count characters only')
    parser.add_argument('files', nargs='+', help='List of files to process')

    args = parser.parse_args()

    sys.exit(wc(args.files, count_lines=args.lines, count_words=args.words, count_characters=args.characters))
