import time

def main_date():
    today = time.strftime("%Y-%m-%d")

    text_file = open("date.txt", "w")
    text_file.write("\n\n\nFile importado dia : %s\n\n" % today)

    text_file.close()

if __name__ == "__main__":
    main_date()
