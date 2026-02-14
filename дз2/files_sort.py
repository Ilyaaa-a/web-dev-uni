import os

def sort_files(directory):
    if not os.path.isdir(directory):
        return []
    
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    groups = {}
    for file in files:
        ext = os.path.splitext(file)[1]
        groups.setdefault(ext, []).append(file)

    result = []
    for ext in sorted(groups):
        for file in sorted(groups[ext]):
            result.append(file)
    
    return result