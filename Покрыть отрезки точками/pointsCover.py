
def pointCover(lines):
    lines.sort()
    points = set()
    del_list = list()
    while len(lines) > 0:
        s = lines[-1][0]
        for line in lines:
            if s in range(line[0], line[1] + 1):
                del_list.append(line)
        for line in del_list:
            lines.remove(line)
        del_list.clear()
        points.add(s)
    print(len(points))
    for p in points:
        print(p)


def main():
    lines = list()
    count = int(input())
    while count > 0:
        line = list()
        length = 2
        count -= 1
        while length > 0:
            line.append(int(input()))
            length -= 1
        lines.append(line)
    pointCover(lines)


main()
