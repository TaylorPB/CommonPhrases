
print(" ################ Welcome ################")



print(" 1. Japanese \n 2. Russia \n 3. Korean")


Language = input(" Please select one")

Language = int(Language)

if Language == 1:
    print(" You have picked Japanese")

    Phrase = input("Please enter a phrase")
    if "Hello" or "hello" in Phrase:
         print(" Ko-ni-chi-wa: こんにちは ")
    else: "print 404"


elif Language == 2:
    print(" You have picked Russian")

    PhraseR = input(" Please enter a phrase")
    if "Hello" or "hello" in PhraseR:
            print("Privyet: Привет")




elif Language == 3:
    print(" You have picked Korean")

    PhraseK=input(" Please enter a phrase")
    if "Hello" or "hello " or "Hi" or "hi" in PhraseK:
        print("ahn-nyung-ha-se-yo: 안녕하세요")