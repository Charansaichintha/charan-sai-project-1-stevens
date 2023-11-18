import json
import argparse
import sys

def gronify(data, parent_key=''):
    if isinstance(data, dict):
        print(f"{parent_key} = {{}}")
        for key, value in data.items():
            gronify(value, parent_key + '.' + str(key) if parent_key else str(key))
    elif isinstance(data, list):
        print(f"{parent_key} = []")
        for i, value in enumerate(data):
            gronify(value, parent_key + '.' + str(i) if parent_key else str(i))
    else:
        print(f"{parent_key} = {json.dumps(data)}")

def main():
    parser = argparse.ArgumentParser(description='Mimic the gron command for JSON data.')
    parser.add_argument('--obj', metavar='base_object', help='Specify the base object name (default: json)', default='json')
    parser.add_argument('json_source', metavar='json_file', nargs='?', help='Path to the JSON file. If not provided, read from stdin.')

    args = parser.parse_args()

    try:
        if args.json_source:
            with open(args.json_source, 'r') as file:
                json_data = json.load(file)
        else:
            json_data = json.load(sys.stdin)

        gronify(json_data, args.obj)
        sys.exit(0)  # Success
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)  # General error

if __name__ == "__main__":
    main()
