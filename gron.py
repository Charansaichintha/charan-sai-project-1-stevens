import json
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

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Usage: python gron_mimic.py [json_file]")
        sys.exit(1)

    if len(sys.argv) == 2:
        json_source = sys.argv[1]
        try:
            with open(json_source, 'r') as file:
                json_data = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{json_source}' not found.")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in '{json_source}': {e}")
            sys.exit(1)
    else:
        # Read from standard input
        try:
            json_data = json.load(sys.stdin)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from stdin: {e}")
            sys.exit(1)

    gronify(json_data)
    sys.exit(0)  # Success
