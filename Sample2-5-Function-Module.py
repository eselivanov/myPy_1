# import module from the file named odbchelper.py under the same project
import odbchelper

# define dictionary of parameters
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}

# call function from module odbchelper with dictionary of parameters
print odbchelper.buildConnectionString(params)

# call function for the doc string - every function has this attribute
print odbchelper.buildConnectionString.__doc__

import sys # import built-in module; sys is an object and path - its attribute
print sys.path # print system search path for modules

# add new directory to the search path
#sys.path.append('/my/new/path')
