import os
import sys

BYTES = 5

prompt = input("Would you like to encode or to decode a picture?\nE - for encode\nD - for decode\n")
if prompt == "E":
    picture = open(input("\nType the path to the picture\n"), "rb")
    picture_contents = picture.read()

    tags = 0
    tags_string = input("\nType numbers, divided by comma. Is this picture...\n" + open(os.path.join(os.getcwd(), "tags.txt"), "r").read() + "\n")
    for tag in tags_string.split(","):
        tags += pow(2, int(tag))

    pic = open(os.path.join(os.getcwd(), os.path.basename(picture.name)[0:-4] + ".pic"), "wb")

    pic.write(tags.to_bytes(pow(2, BYTES), sys.byteorder) + picture_contents)
    pic.flush()
    pic.close()

elif prompt == "D":
    picture = open(os.path.join(os.getcwd(), "pic.pic"), "rb")
    picture_contents = picture.read()

    tags_list = list()
    tags = int.from_bytes(picture_contents[0:32], sys.byteorder) #C:\Users\miles\Documents\pic.jpg
    for i in range(0, BYTES):
        if tags % 2 == 1:
            tags_list.append(i)
            tags -= 1
        tags >>= 1

    tags = list()
    for i in open(os.path.join(os.getcwd(), "tags.txt"), "r").read().split("\n"):
        if int(i[0]) in tags_list:
            tags.append(i[i.find(" - ")+3:])
    print("\nYour picture is " + ", ".join(tags[0:-1]) + " and " + tags[-1])

    pic = open(os.path.join(os.getcwd(), os.path.basename(picture.name)[0:-4] + ".jpg"), "wb")
    pic.write(picture_contents[32:])
    pic.flush()
    pic.close()

else:
    print("Wrong argument")
