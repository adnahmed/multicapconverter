class Dict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        if key in self.data:
            del self.data[key]
        else:
            raise KeyError(key)

    def __contains__(self, key):
        return key in self.data

    def get(self, key, default=None):
        return self.data.get(key, default)

    def keys(self):
        return list(self.data.keys())

    def values(self):
        return list(self.data.values())

    def items(self):
        return list(self.data.items())

    def __len__(self):
        return len(self.data)

    def __str__(self):
        items = [f'"{key}": {value}' for key, value in self.items()]
        return "{" + ", ".join(items) + "}"

    def clear(self):
        self.data.clear()

    def copy(self):
        new_dict = Dict()
        new_dict.data = self.data.copy()
        return new_dict

    def update(self, other_dict):
        if isinstance(other_dict, Dict):
            self.data.update(other_dict.data)
        else:
            for key, value in other_dict.items():
                self.data[key] = value