file = open("input.txt", "r")

str_input = file.readline()
str0 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
str1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
str2 = "nppdvjthqldpwncqszvftbrmjlhg"
str3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
str4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

num = 14


def find_marker(line):
    i = 0
    for w in range(0, len(line)):
        temp = line[w:w + num]
        x = filter(lambda x: temp.count(x) >= 2, temp)
        if (len(' '.join(set(x))) == 0):
            return temp, w + num


print(find_marker(str0))
print(find_marker(str1))
print(find_marker(str2))
print(find_marker(str3))
print(find_marker(str4))
print(find_marker(str_input))