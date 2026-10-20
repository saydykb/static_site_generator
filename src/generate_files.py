import os, shutil

def generate_files(source_path: str, dest_path: str):
    if not os.path.exists(source_path):
        raise ValueError(f"{source_path} does not exist")
#    print(f"attempting to generate files from source: {source} and destination: {destination}") if not os.path.exists(source): raise FileNotFoundError("source does not exsts")
    if os.path.isfile(dest_path):
        raise ValueError("destination must be a dir")
    if os.path.isdir(source_path):
#        print(f"{source} is a directory")
        if os.path.exists(dest_path):
#            print(f"destination exists")
            shutil.rmtree(dest_path)
#            print(f"removed {destination}")
        os.mkdir(dest_path)
#        print(f"made directory {destination}")
        list_dir = os.listdir(source_path)
        for name in list_dir:
            generate_files(os.path.join(source_path, name), os.path.join(dest_path, name))
    else:
        shutil.copy(source_path, dest_path)
#        print(f"copied {source} to {destination}")
