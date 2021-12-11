import os

# directory = "Day "+i
parent_dir = "./"

# for i in range(100):
#     os.makedirs()

for i in range(100):
    directory = "Day "+str(i)
    path = os.path.join(parent_dir, directory)
    print (path)
    if not os.path.exists(path):
        os.mkdir(path)
