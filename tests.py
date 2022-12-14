import os
import requests

# using the dummy directory "test_root" to test so that this 
# program works on any computer that has the whole "weavegrid" folder
# Note- I mostly did exploratory testing while writing the code, using 
# things like curl, running user_interface.py, and good ole print statements

BASE = "http://127.0.0.1:5000/"

# this is so program doesnt hang indefinitley if something goes wrong 
TIMEOUT = 5 #seconds


def test_good_dirs():
    good_dirs = ['root', 'dir1', '/dir1',
            'dir1/', '/dir1/', 'dir1/dir2', 'dir1/emptydir']

    for directory in good_dirs:
        response = requests.get(BASE + 'dir/' + directory, timeout=TIMEOUT)
        assert response.status_code == 200
    print("good dirs are good")


def test_good_files():
    good_files = ['file1.txt', '/file1.txt',
                 'dir1/file2', 'dir1/dir2/emptyFile',  
                 'dir1/dir2/resume_in_lateX']

    for file in good_files:
        response = requests.get(BASE + 'file/' + file, timeout=TIMEOUT)
        assert response.status_code == 200
    print("good files are good")


def test_bad_dirs():
    bad_dirs = ['', 'hello', 'this/is/not/a/real/directory/i/hope',
                    'file.txt', 'dir1/dir2/emptyfile']

    for directory in bad_dirs:
        response = requests.get(BASE + 'dir/' + directory, timeout=TIMEOUT )
        assert response.status_code == 404
    print("bad dirs throw proper errors")


def test_bad_files():
    bad_files = ['', 'foo', 'dir1', f'{os.getcwd}/testroot/file.txt']

    for file in bad_files:
        response = requests.get(BASE+ 'file/' + file, timeout=TIMEOUT)
        assert response.status_code == 404
    
    print("bad files throw proper errors")


test_good_dirs()
test_good_files()
test_bad_dirs()
test_bad_files()