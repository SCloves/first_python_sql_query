import time

today = time.strftime("%Y-%m-%d")

text_file = open("date.txt", "w")
text_file.write("\n\n\nFile importado dia : %s" % today)

text_file.close()
