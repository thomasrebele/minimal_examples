
# for importing/exporting data
import json
def to_json(obj):
    return json.dumps(obj, cls=json.JSONEncoder, indent=2)

def from_json_file(path):
    try:
        with open(path) as f:
            data = json.load(f)
            return data
            for i in data:
                return i
    except FileNotFoundError:
        return json.loads("{}")
    pass


