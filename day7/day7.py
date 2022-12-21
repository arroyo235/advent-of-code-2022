file = open("input.txt", "r")
# file = open("input0.txt", "r")


class Node:

    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size


class Directory(Node):

    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent
        self.size = 0
        self.files = []

    def getSize(self):
        size = self.size
        for i in self.files:
            if (isinstance(i, Directory)):
                size += i.getSize()
            else:
                size += i.size
        return size

    def addDirectory(self, name: str):
        new_dir = Directory(name, self)
        self.files.append(new_dir)
        return new_dir


class File(Node):

    def __init__(self, filename: str, size, parent: Directory):
        self.name = filename
        self.size = int(size)
        self.parent = parent
        if (len(filename.split(".")) >= 2):
            self.type = filename.split(".")[1]

    def getSize(self):
        return self.size

    def addFile(self, name: str, size: int, parent: Directory):
        File(name, size, parent)


root = Directory("/home")
cwd = root
dirs = []
dirs.append(root)

for i in file.read().split("\n"):
    if (i.split(" ")[0] == "$"):
        if (i == "$ cd /"):
            cwd = root
        elif (i.split(" ")[1] == "ls"):  # $ ls
            pass
        else:
            if (i.split(" ")[2] == ".."):  # $ cd ..
                cwd = cwd.parent
            else:  # $ cd [dirname]
                # dirname = cwd.name + "/" + i.split(" ")[2]
                cwd = cwd.addDirectory(i.split(" ")[2])
                dirs.append(cwd)
    elif (i.split(" ")[0] == "dir"):
        pass  # dir [dirname]
    else:
        cwd.files.append(File(i.split(" ")[1], i.split(" ")[0], cwd))  # [dirsize] [dirname]


def print_directory_tree(directory, indentation=''):
    # Calculate the size of the directory by adding the sizes of its files and subdirectories

    # directory_size = sum(file.size for file in directory.files if isinstance(file, File))
    # directory_size += sum(subdirectory.getSize() for subdirectory in directory.files if isinstance(subdirectory, Directory))
    if (directory.name == "/home"):
        directory.getSize()

    print(indentation + directory.name + " (dir, " + str(directory.getSize()) + ")")
    # print(directory.name + " : " + str(directory.getSize()))

    for file in directory.files:
        if (isinstance(file, File)):
            # print(indentation + "  " + file.name + " (file, " + str(file.size) + ")")
            pass
        else:
            # for subdirectory in directory.files:
            print_directory_tree(file, indentation + "  ")


total_sum = 0
def sum_sizes(directory):
    global total_sum
    for subdir in directory.files:
        if (isinstance(subdir, Directory)):
            sum_sizes(subdir)
            temp_sum = subdir.getSize()
            if (temp_sum <= 100000):
                total_sum += temp_sum
    return total_sum


# print_directory_tree(root)
# PART 1
print("PART 1")
print(sum_sizes(root))

# PART 2
print("PART 2")
total_space = 70000000
least_size = 30000000
used_space = root.getSize()

min_to_delete = used_space - (total_space-least_size)
dir_selected_size = root
valid_dirs = []

for dir in dirs:
    if(dir.getSize() > min_to_delete):
        valid_dirs.append(dir.getSize())

print(min(valid_dirs))