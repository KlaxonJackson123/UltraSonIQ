#!/usr/bin/env python3
import os
import zipfile
import shutil

ARCHIVE_FOLDER = "./patches"
EXTRACT_FOLDER = "./_tmp_patch_extract"

def apply_patch(zip_path):
    print(f"Applying patch: {zip_path}")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_FOLDER)

    patch_root = os.listdir(EXTRACT_FOLDER)[0]
    patch_content_path = os.path.join(EXTRACT_FOLDER, patch_root)

    for item in os.listdir(patch_content_path):
        s = os.path.join(patch_content_path, item)
        d = os.path.join(".", item)
        if os.path.exists(d):
            print(f"Updating: {item}")
        else:
            print(f"Adding: {item}")
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    
    shutil.rmtree(EXTRACT_FOLDER)
    print("Patch applied successfully.")

def main():
    patches = sorted(f for f in os.listdir(ARCHIVE_FOLDER) if f.endswith(".zip"))
    for patch in patches:
        apply_patch(os.path.join(ARCHIVE_FOLDER, patch))

if __name__ == "__main__":
    main()
