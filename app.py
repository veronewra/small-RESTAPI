from flask import Flask, abort
from flask_restful import Resource, Api
import os
from collections import defaultdict

class RootDirRelativeResource(Resource):
    def __init__(self, root_dir):
        super().__init__()
        self.root_dir = root_dir

    # makes sure that all paths are expanded and vars are resolved (like `root`)
    def parse_path(self, path):
        path = path.strip()
        if path == 'root':
            return self.root_dir

        return self.root_dir + '/' + os.path.expanduser(path)


class Directory(RootDirRelativeResource):
    def __init__(self, root_dir, contents):
        super().__init__(root_dir)
        self.contents = contents

    def get(self, path):

        path = self.parse_path(path)

        if not os.path.isdir(path):  
            abort(404, description=f'\'{path}\' is not a directory\n')
            
        return {'contents of directory:': self.contents[path]}, 200
            

class File(RootDirRelativeResource):
    def __init__(self, root_dir):
        super().__init__(root_dir)

    def get(self, path):

        path = self.parse_path(path)

        if not os.path.isfile(path):
            abort(404, description=f'\'{path}\' is not a file.\n')

        with open(path) as f:
            return {'contents of file:': f.readlines()}


# returns a directory containing all of the contents 
# under the passed directory. Key is global path, value is
# a list or a dict for directories or files respectivley.
def get_dir_contents(dir_path):
    # returns a dictionary containing information about a file
    def get_file_info(file_path):
        info = os.stat(file_path)
        return {
                'owner': info.st_uid,
                'size': f'{info.st_size} bytes',
                'permissions': info.st_mode
                }

    content = defaultdict(list)
    for root, dirs, files in os.walk(dir_path):
        for dir_name in dirs:
            content[root].append(dir_name)
        for file_name in files:
            if os.path.isfile(root+'/'+file_name):
                content[root].append(
                    {file_name: get_file_info(root + '/' + file_name)})

    return content

def validate_dir(dir_string):
    if not os.path.isdir(dir_string):
        raise ValueError(f"{dir_string} is not a valid directory\n")

#this function is what flask looks for to run the app
def create_app(root_dir):
    app = Flask(__name__)
    api = Api(app)
    validate_dir(root_dir)
    contents = get_dir_contents(root_dir)
    api.add_resource(Directory, '/dir/<path:path>', resource_class_kwargs={"root_dir": root_dir, "contents": contents})
    api.add_resource(File, '/file/<path:path>', resource_class_kwargs={"root_dir": root_dir})
    return app

