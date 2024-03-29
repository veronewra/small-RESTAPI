cd into the main folder, and run `./run_app.sh "directory/of/your/choice"` to start the server.
Running `./user_interface.py` lets you explore the endpoints in an interactive environment. (Otherwise you can use the curl command) The commands available in the user interface are:

  * `--help`: lists the information about the commands

  * `list path/to/directory`: shows the contents of the directory. Passing "root" as the path displays the contents of the root directory.

  * `show path/to/file`: display the contents of the file 

  * To exit the program press CTRL+C

Users are only able to view directories and files under the root directory that was set when initializing the server, so all of the paths must be relative to that root directory. 

For example, say the root directory is set to be 'home/user/folder1', and folder1 contains a directory named dir and a file named foo. Users cannot view the contents of 'user' because it is not in the programs scope. Users could however view things in folder1 and all its subdirectories by entering something like `list dir` or `show foo`

To run some basic tests, you can run `python3 app.py test_root` to start the server, and then run `python3 tests.py`.
