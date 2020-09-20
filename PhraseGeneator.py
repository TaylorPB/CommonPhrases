
import sys

def main():
    print("################ Welcome ################ ")
    print(" 1. Japanese \n 2. Germen \n 3. Korean \n 4. French")
    Option = ["Yes", "yes", "YES"]

    Ph = ["Hello", "hi" , "Hi", "hello", "My name is"]


    Language = input("Please select a language")
    Language = int(Language)

    if Language== 1:
        print(" You picked Japanese")
        print("1 . Hello \n 2. How are you \n 3. Good Evening \n 4. Good Morning \n 5. My Name is \n 6. I'm From America \n 7. Thank you \n 8. You're Welcome \n 9. Excuse me/Sorry \n 10. I don't Understand \n 11. Take Care \n 12. Can you Repeat that  \n 13. I Dont Understand Japanese \n 14. I'm sorry \n 15. Do you speak English? \n 16. Where is _____ \n 17. Thank you for the meal \n 18. How much? \n 19. Yes \n 20. No                                                                                                                                            "





              )
        print(" How to say it - how it's read")
        PhraseJ = input(" Please pick a phrase from the list")

        PhraseJ = int( PhraseJ)


        if 1==  PhraseJ:
            print( "Ko-ni-chi-wa: こんにちは")


        if 2 ==  PhraseJ:
            print("O-gen-ki desu ka? お元気ですか")

        if 3 == PhraseJ:
            print(" Kon-ban-wa こんにちは")

        if 4 ==  PhraseJ:
            print("O-hai-yo go-za-i-masu おはよう ございます")

        if 5 == PhraseJ:
            print("Wa-ta-shi-no na-ma-e wa ______ desu 私の名前は＿＿です")

        if 6 == PhraseJ:
            print(" Wa ta shi wa A-mer-i-ka ka-ra ki-ma-shi-ta 私 は アメリカ から 来ました ")

        if 7 == PhraseJ:
            print("A-ri-ga-to-u go-za-i-ma-su ありがとうございます")

        if 8 == PhraseJ:
            print("Dou it-a-shi-ma-shite どう致しまして")

        if 9 == PhraseJ:
            print("Su-mi-ma-sen すみません")

        if 10 == PhraseJ:
            print("Wa-ka-ri-ma-sen わかりません ")

        if 11 == PhraseJ:
            print("O-gen-ki de おげんきで")

        if 12 == PhraseJ:
            print("Mou ichido onegai shimasu もう一度お願いします")

        if 13 == PhraseJ:
            print("Ni-hon-go ga wa-ka-ri-ma-sen 日本語がわかりません")

        if 14 == PhraseJ:
            print("Go-men na-sai ごめんなさい")

        if 15 == PhraseJ:
            print("eigo wo ha-na-se-masu ka?")

        if 16 == PhraseJ:
            print("__place____ wa doko desu ka ___place___ はどこですか")

        if 17 == PhraseJ:
            print("Go-chi-so-u-sama de-shi-ta ごちそうさまでした ")

        if 18 == PhraseJ:
            print("i-ku-ra desu ka いくらですか")

        if 19 == PhraseJ:
            print("ha-i はい")

        if 20 == PhraseJ:
            print("i-ie いいえ")













    elif Language== 2:
        print(" You picked Germen")


        print("1. Hello \n 2. Good Morning \n 3. I'm From America \n 4. Where is the train station \n 5. I am lost \n 6. Excuse me\Sorry \n 7. Thank you very much \n 8. No thank you \n 9. I'm Sorry \n 10. Do you speak English \n 11. I don't speak Germen \n 12. I don't understand \n 13. May I see a map \n 14. No problem \n 15. Nice to meet you \n 16. How are you \n 17. I'm fine Thank you  \n 18. My name is _____  \n 19. Take Care \n 20. Good Bye  " )

        PhraseG = input(" Please enter a phrase from the list above")
        PhraseG = int(PhraseG)

        if 1== PhraseG:
            print("Hallo! ")

        if 2== PhraseG:
            print("Guten Morgen!")

        if 3== PhraseG:
            print("Ich komme aus Amerika")

        if 4== PhraseG:
            print("Wo ist der Bahnhof?")

        if 5== PhraseG:
            print("Ich habe mich verlaufen")

        if 6== PhraseG:
            print("Entschuldigung!")


        if 7== PhraseG:
            print("Vielen Dank")

        if 8== PhraseG:
            print("Nein, Danke")

        if 9== PhraseG:
            print("Es tut mir leid")


        if 10== PhraseG:
            print("Sprechen Sie Englisch?")

        if 11== PhraseG:
            print("Ich spreche nicht viel Deutsch")

        if 12== PhraseG:
            print("Ich verstehe nicht")

        if 13== PhraseG:
            print("Darf ich mir einen Stadtplan ansehen?")

        if 14== PhraseG:
            print("Kein problem")

        if 15== PhraseG:
            print("Freut mich, dich kennenzulernen")

        if 16== PhraseG:
            print("Wie geht es Ihnen?  ")

        if 17== PhraseG:
            print("Gut, danke")

        if 18== PhraseG:
            print("Ich heisse ___name___")

        if 19== PhraseG:
            print("Machs gut")

        if 20== PhraseG:
            print("Auf Wiedersehen")


    elif Language == 3:
        print(" You picked Korean")
        print(" How to say it : How to read it")
        print("1. Hello \n 2. Nice to meet you \n 3. How are you \n 4. My name is ____name____ \n 5. Thank you \n 6. You're Welcome \n 7. Excuse me \n 8. I'm sorry \n 9. I'm lost \n 10. Do you know where ____ ? \n 11. I don't understand \n 12. Do you speak English \n 13.  Where is the bathroom \n 14. How much is it? \n 15. Help \n 16. Good-Bye \n 17. I don't speak well Korean \n 18. It's Okay \n 19. Have a great meal \n 20. The meal was good")


        PhraseK = input(" Please pick a phrase from above")
        PhraseK = int(PhraseK)

        if 1== PhraseK:
            print("ahn-nyung-ha-se-yo: 안녕하세요")

        if 2 == PhraseK:
            print("Bahn-gap-seup-ni-da: 반갑습니다")

        if 3 == PhraseK:
            print("Uh-dduh-keh  ji-neh-seh-yo?: 어떻게 지내세요 ")
        if 4 == PhraseK:
            print("Eh  ee-reum-un _____ :제 이름은")
        if 5 == PhraseK:
            print("Gam-sa-ham-ni-da: 감사합니다 ")

        if 6 == PhraseK:
            print("Chun-mahn-eh-yo: 천만에요")

        if 7 == PhraseK:
            print("Shil-leh-hap-nee-da: 실례합니다 ")

        if 8 == PhraseK:
            print("Weh-sung-hap-nee-da: 죄송합니다 ")

        if 9 == PhraseK:
            print("Gil-eul  ilh-uht-suh-yo: 길을 잃었어요 ")

        if 10 == PhraseK:
            print(" Uh-di-eehn-ji  ah-seh-yo? _____ :어디인지 아세요?")

        if 11 == PhraseK:
            print("Jal mo-reu-geht-neh-yo: 잘 모르겠네요 ")

        if 12 == PhraseK:
            print(" Yung-uh  hal  su-eet-suh-yo?: 영어 할 수 있어요")

        if 13 == PhraseK:
            print("Hwa-jang-shil-ee  uh-di-eh-yo?: 화장실이 어디예요? ")

        if 14 == PhraseK:
            print("Uhl-mah-eh-yo?: 얼마에요")

        if 15 == PhraseK:
            print(" Doh-oah-ju-seh-yo!: 도와주세요")

        if 16 == PhraseK:
            print("Ahn-nyung: 안녕 ")

        if 17 == PhraseK:
            print("Hahn-guhk-mal  jal  moht-heh-yo: 한국말 잘 못해요")

        if 18 == PhraseK:
            print("Gwaen-chanh-ah-yo: 괜찮아")

        if 19 == PhraseK:
            print("Jal meok-ge-sseum-ni-da: 잘 먹겠습니다")

        if 20 == PhraseK:
            print("Jal meo-geo-sseum-ni-da: 잘 먹었습니다")







    elif Language == 4:
        print(" You picked French")


        print("1. Hello \n 2. Nice to meet you \n 3. How are you \n 4. I'm well \n 5. Thank \n 6. Excuse me/Sorry 7. \n 8. I'm Lost \n 9.Help \n 10. How much is it/ How much does that cost \n 11. Where is the toilet \n 12. My name is______ \n 13. Yes \n 14. No \n 15. Good bye \n 16. See you soon! \n 17.  Where is____ \n 18. Could you repeat that please? \n 19. I am sick \n 20. What time is is it? ")
        print("How to say it  - [ actual word] ")
        PhraseF = input(" Please enter a phrase from the list ")

        PhraseF = int(PhraseF)

        if 1== PhraseF:
            print("Bonjour")

        if 2== PhraseF:
            print("On shon tay - [Enchanté(e)!]")

        if 3== PhraseF:
            print("a va - [Ça va?]")

        if 4== PhraseF:
            print(" juh vay byan  -  [je vais bien ]")

        if 5== PhraseF:
            print("mair see byan - [Merci bien]")

        if 6== PhraseF:
            print("eh skyoo zay mwah - [Excusez-moi ]")

        if 7== PhraseF:
            print("parlay voo fron ong glay - [Parlez-vous anglais?]")

        if 8== PhraseF:
            print("juh swee pair doo - [Je suis perdu]")

        if 9== PhraseF:
            print("oh suhcoor - [Au secours!]  ")

        if 10== PhraseF:
            print("say kom byan, sa coot kom byan - [C’est combien? / Ça coûte combien?]  ")

        if 11== PhraseF:
            print("oo ay lah sal duh ban - [Où est la salle de bains]")

        if 12== PhraseF:
            print(" juh mappel____name___ [Je m’appelle _____name____]")

        if 13== PhraseF:
            print("Wee [Oui]")

        if 14== PhraseF:
            print("Noh [Non]")


        if 15== PhraseF:
            print("oh ruh vwah [Au revoir!]")

        if 16== PhraseF:
            print("ah byan toe [À bientôt! ]")

        if 17== PhraseF:
            print("ooh eh _____place____ [Où est___place__]")

        if 18== PhraseF:
            print("18. pooh-ree-ey-vooh rey-pey-tey, seel vooh pleh? [Pourriez-vous répéter, s’il vous plaît?]")

        if 19== PhraseF:
            print("zhuh swee mah-lahd [Je suis malade.]")

        if 20== PhraseF:
            print("ehl uhr eh-teel? [Quelle heure est-il ?]")




       





    else:
        print(" Sorry the Language you have select is not avaliable at this time")




    choice = input(" Would you like to try again?\n 1. for yes \n 2. for no")
    choice = int(choice)
    if 1 == choice:
        main()


    elif 2== choice:
        quit()




    else:
        quit()


main()


