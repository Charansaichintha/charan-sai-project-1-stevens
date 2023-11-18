import sys

def wc(file_path=None):
    try:
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                lines = content.count('\n')
                words = len(content.split())
                characters = len(content)
                print(f"{lines}\t{words}\t{characters}\t{file_path}")
        else:
            content = sys.stdin.read()
            lines = content.count('\n')
            words = len(content.split())
            characters = len(content)
            print(f"{lines}\t{words}\t{characters}")

        return 0  # Success

    except FileNotFoundError:
        print(f"wc: {file_path}: No such file or directory")
        return 1  # File not found error

    except Exception as e:
        print(f"wc: Error: {e}")
        return 2  # Other errors

if __name__ == "__main__":
    if len(sys.argv) == 2:
        sys.exit(wc(sys.argv[1]))
    elif len(sys.argv) == 1:
        sys.exit(wc())
    else:
        print("Usage: python wc.py [file_path]")
        sys.exit(2)  # Incorrect usage
