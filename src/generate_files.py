import os, shutil

def generate_files(source: str, destination: str):
#    print(f"attempting to generate files from source: {source} and destination: {destination}") if not os.path.exists(source): raise FileNotFoundError("source does not exsts")
    if os.path.isfile(destination):
        raise ValueError("destination must be a dir")
    if os.path.isdir(source):
#        print(f"{source} is a directory")
        if os.path.exists(destination):
#            print(f"destination exists")
            shutil.rmtree(destination)
#            print(f"removed {destination}")
        os.mkdir(destination)
#        print(f"made directory {destination}")
        list_dir = os.listdir(source)
        for name in list_dir:
            generate_files(os.path.join(source, name), os.path.join(destination, name))
    else:
        shutil.copy(source, destination)
#        print(f"copied {source} to {destination}")
