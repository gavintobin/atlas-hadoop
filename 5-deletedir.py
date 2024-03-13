#!/usr/bin/env python3
'''task 1'''

def deletedir(l):
    '''delete dir'''
    import subprocess

    for dir_path in l:
        try:
            subprocess.run(["hdfs", "dfs", "-rm", "-r", dir_path], check=True)
            print(f"Deleted directory: {dir_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error deleting directory {dir_path}: {e}")
