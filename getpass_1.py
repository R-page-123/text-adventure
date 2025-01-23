def getPword(attempt):
    while attempt < 3:
        if attempt == 1:
            pword = input("enter pass: ")
            if (len(pword) >= 6) and (len(pword) <= 8):
                if pword == "qwerty":
                    print("correct")
                else:
                    attempt = attempt + 1
            else:
                print("pass is not a valid length")
                attempt = attempt + 1
        else:
            pword = input("enter pass again: ")
            if (len(pword) >= 6) and (len(pword) <= 8):
                if pword == "qwerty":
                    print("correct")
                else:
                    attempt = attempt + 1
            else:
                print("pass is not a valid length")
                attempt = attempt + 1
    else:
        print("not enough attempts")