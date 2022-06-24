

def timeConversion(s):
    time_conversion_dict = {
        "1": "13",
        "2": "14",
        "3": "15",
        "4": "16",
        "5": "17",
        "6": "18",
        "7": "19",
        "8": "20",
        "9": "21",
        "10": "22",
        "11": "23",
        "12": "00"}

    if s[(len(s)-2):(len(s)-1)] == "PM":
        print("True")
        for i in time_conversion_dict:
            print(i)
            if s[0:1] == i:
                print("Match")
            #     s[0:1] == v
            #     print(s[0:1])


s = "02:05:45PM"

timeConversion(s)

