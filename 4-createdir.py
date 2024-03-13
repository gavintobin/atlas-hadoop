#!/usr/bin/env python3
'''task 1'''


from snakebite.client import Client

def createdir(l):
    '''create dir'''
    client = Client('localhost', 8020)

    try:
        for directory in l:
            client.mkdir(directory)
            print(f"Created directory: {directory}")
    except Exception as e:
        print(f"Error creating directories: {e}")
