import os, json

def load_cfg():
    with open("config.json","r",encoding="utf-8") as f:
        return json.load(f)

def append_json(path, item, keep_last=720):
    arr = []
    if os.path.exists(path):
        try:
            arr = json.load(open(path,"r",encoding="utf-8"))
        except Exception:
            arr = []
    arr.append(item)
    arr = arr[-keep_last:]
    tmp = path + ".tmp"
    with open(tmp,"w",encoding="utf-8") as f:
        json.dump(arr, f, indent=2)
    os.replace(tmp, path)
