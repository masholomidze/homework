academy = input("გოაში სწავლობ?: ")
if academy != "კი":
    print("კაი, თუ პროგრამირების აკადემიას ეძებ გოაში შემოდი😉")

if academy == "კი":
    question = int(input("მერამდენე ჯგუფში ხარ?: "))

    if question == 13:
        question2 = input("არის გაბრიელი შენი მენტორი?: ")

        if question2 == "კი":
            print("სწორია, მეც გაბრიელი მასწავლის")

        else:
            print("რატომ იტყუები? შენ არ ხარ ჯგუფ 13-ში!!")




