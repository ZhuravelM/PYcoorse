def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file


file1_name = "TF7_1.txt"
file2_name = "TF7_2.txt"

# а) створення TF7_1
file_1_w = Open(file1_name, "w")

if file_1_w != None:
    text = "The flight number 1717 is postponed for 40 minute, the boarding will start at 5 a.m."
    file_1_w.write(text)
    print("Information was successfully added to TF7_1.txt!")
    file_1_w.close()
    print("File TF7_1.txt was closed!")

# б) обробка TF7_1 і створення TF7_2
file_1_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_1_r != None and file_2_w != None:
    content = file_1_r.read()
    words = content.replace(',', '').replace('.', '').replace('!', '').replace('?', '').split()
    doubled = []

    for word in words:
        for i in range(len(word) - 1):
            if word[i].lower() == word[i + 1].lower():
                doubled.append(word)
                break

    if len(doubled) > 0:
        for w in doubled:
            file_2_w.write(w + "\n")
    else:
        file_2_w.write("No words with doubled letters found.\n")

    file_1_r.close()
    file_2_w.close()
    print("Files were closed!")

# в) читання TF7_2 і виведення
print("Words with doubled letters:")
file_3_r = Open(file2_name, "r")

if file_3_r != None:
    for line in file_3_r.read().splitlines():
        print(line)
    file_3_r.close()
    print("File TF7_2.txt was closed!")