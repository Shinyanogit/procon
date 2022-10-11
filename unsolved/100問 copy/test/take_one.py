import random, webbrowser

with open("links.txt") as f:
    links = f.readlines()
    raw_data = random.choice(links)
with open("links.txt", "w") as f:
    link_and_result = raw_data.split()
    webbrowser.open(link_and_result[0], new=0)
    print(link_and_result[0])
    the_index = links.index(raw_data)
    print(f"question number : {the_index+1}")
    result = input("result?(o,-,x)")
    links[the_index] = raw_data[:-1] + " " + result + "\n"
    f.write("".join(links))
