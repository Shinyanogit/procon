import random, webbrowser, pyperclip

with open("links.txt") as f:
    links = f.readlines()
    raw_data = random.choice(links)


def calc_percentage(rawdata):
    if " " in raw_data:
        result = rawdata.split()[1]
        num_o = result.count("o")
        num_ = result.count("-")
        num_x = result.count("x")
        return (num_o, num_, num_x)
    else:
        return (0, 0, 0)


with open("links.txt", "w") as f:
    link_and_result = raw_data.split()
    webbrowser.open(link_and_result[0], new=0)
    print(link_and_result[0])
    pyperclip.copy(link_and_result[0])
    the_index = links.index(raw_data)
    print(f"question number : {the_index+1}")
    a, b, c = calc_percentage(raw_data)
    print(f"result o:{a} -:{b} x:{c}")
    result = input("result?(o,-,x)")
    links[the_index] = raw_data[:-1] + " " + result + "\n"
    f.write("".join(links))
