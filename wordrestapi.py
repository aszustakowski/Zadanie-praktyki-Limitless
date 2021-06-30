def add_word(wordlist, word):
    wordlist = wordlist + [word]

    return wordlist

def remove_word(wordlist, word):
    list_del = [i for i in wordlist if i != word]

    return list_del

def count_occurrence(wordlist, word):
    counter = wordlist.count(word)

    return counter

def repr_distinct_list(wordlist):
    return print(list(set(wordlist)))

def main():
    wordlist = ['TEST', 'BBB', "AAA"] #testowe dane

    while True:

        print("Co chcesz zrobić?: \n1 - dodaj słowo  \n2 - usuń słowo"
              "  \n3 - sprawdź liczbę wystąpień słowa  \n4 - pokaż kolekcję różnych słów \n5 - wyjdź")

        try:
            y = int(input("Akcja numer: "))

        except ValueError:
            print("Nie została podana liczba naturalna!")
            continue

        if y not in (1,2,3,4,5):
            print("Nie została podana liczba naturalna od 1 do 5!")
            continue

        elif y == 1:
            word = str(input("Wpisz słowo: ")).upper()

            if not word.isalpha():
                print("Wolno wpisać tylko litery!")

            else:
                wordlist = add_word(wordlist, word)

        elif y == 2:
            word = str(input("Wpisz słowo: ")).upper()

            if not word.isalpha():
                print("Wolno wpisać tylko litery!")

            else:
                wordlist_1 = remove_word(wordlist, word)

                if wordlist == wordlist_1:
                    print("Brak słowa w kolekcji!")
                else:
                    wordlist = wordlist_1

        elif y == 3:
            word = str(input("Wpisz słowo: ")).upper()

            if not word.isalpha():
                print("Wolno wpisać tylko litery!")

            else:
                counter = count_occurrence(wordlist, word)

                if counter == 0:
                    print("Brak słowa w kolekcji")

                else:
                    print(f"Słowo {word} występuje {counter} razy")

        elif y == 4:
            repr_distinct_list(wordlist)

        elif y == 5:
            break

if __name__ == "__main__":
    main()