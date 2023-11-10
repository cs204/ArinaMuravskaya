def convert(s):
    if s.find(":)")!=-1:
              s=s.replace(":)","\U0001F642")
    if s.find(":(")!=-1:
              s=s.replace(":(","\U0001F641")
    return s

def main():
    s=input()
    print(convert(s))

main()
