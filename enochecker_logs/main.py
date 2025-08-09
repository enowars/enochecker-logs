import sys
import json
import datetime

def main():
    line = sys.stdin.readline()
    while line:
        line = line.strip()
        if line.startswith("##ENOLOGMESSAGE "):
            _, loginfo_json = line.split(" ", 1)
            loginfo = json.loads(loginfo_json)
            prefix = datetime.date.strftime(loginfo["timestamp"], "%T:%f")
            print(prefix,":", loginfo["message"])
        else:
            print(">> " + line)
        line = sys.stdin.readline()

if __name__ == "__main__":
    main()
