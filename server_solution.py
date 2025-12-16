word = "ERROR"

with open("server_log.txt", "r" , encoding="utf-8") as file, open("errors_only.txt", "w", encoding="utf-8") as new_file:
    counter = 0
    for line in file:
        if word in line:
            print(line.strip())
            counter+=1
            new_file.write(line)
print(counter)