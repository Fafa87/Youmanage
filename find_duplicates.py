import json
import time

import fire
import hashlib
from glob import glob
from pathlib import Path
from tqdm import tqdm


def calculate_hash(filepath):
    with open(filepath, "rb") as file:
        data = file.read()
    sha1 = hashlib.sha1(data).hexdigest()
    md5 = hashlib.md5(data).hexdigest()
    return f"{sha1}@{md5}"


def prepare_hashionary(*filepaths, root_dir=None, save_path=None, known_path=None):
    res = {}
    if root_dir is not None:
        root_dir = Path(root_dir)
        all_files = glob(str(root_dir / "**" / "*.*"), recursive=True)
        filepaths = list(filepaths) + all_files

    if known_path is not None:
        res = load_hashionary(known_path)
        print(f"Loaded {len(res)} known hashes.")

    filepaths_wrapped = tqdm(filepaths, "Calculating hashes:")
    for filepath in filepaths_wrapped:
        filepaths_wrapped.set_description("Processing %s" % filepath)
        if filepath not in res:
            res[filepath] = calculate_hash(filepath)

    if save_path is not None:
        save_hashionary(res, save_path)
    return res


def save_hashionary(hashionary, save_path):
    with open(save_path, "w") as file:
        json.dump(hashionary, file, indent=4, sort_keys=True)


def load_hashionary(load_path):
    with open(load_path, "r") as file:
        return json.load(file)


def reverse_hashionary(hashionary):
    return {v: k for k, v in hashionary.items()}


def check_against_base(new_root, base_path, verbose=1):
    hash_base = load_hashionary(base_path)
    new_hashes = prepare_hashionary(root_dir=new_root)

    base_hash_to_path = reverse_hashionary(hash_base)
    new_hash_to_path = reverse_hashionary(new_hashes)

    for new_hash, new_path in new_hash_to_path.items():
        if new_hash in base_hash_to_path:
            print(f"File {new_path} was found as {base_hash_to_path[new_hash]} - same hash: {new_hash}.")
        else:
            print(f"File {new_path} is a new file - new hash: {new_hash}.")

if __name__ == "__main__":
    fire.Fire()
