#!/usr/bin/env python3
'''task 1'''
def download(l):
    '''snakebite'''
    import subprocess

    target_directory = "/tmp"


    for hdfs_path in l:

        local_path = f"{target_directory}/{hdfs_path.split('/')[-1]}"


        try:
            subprocess.run(["hdfs", "dfs", "-get", hdfs_path, local_path], check=True)
            print(f"Downloaded {hdfs_path} to {local_path}")
        except subprocess.CalledProcessError:
            print(f"Error downloading {hdfs_path}")
