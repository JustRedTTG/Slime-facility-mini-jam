import pickle, os

def save(file,*args):
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'wb') as f:
        pickle.dump(args, f)

def load(file):
    args = []
    with open(file,"rb") as f:
        args = pickle.load(f)
    return args