def sito(n):
    numbers = [True for _ in range(n)]
    prime_numbers = []
    for i in range(2, len(numbers)):
        if i <= 1:
            numbers[i] = False
        else:
            if numbers[i]:
                prime_numbers.append(i)
                for j in range(i,len(numbers), i):
                    numbers[j] = False
    return prime_numbers
print(sito(int(input("Podaj ostatnią liczbę, aż do której chcesz zastosować sito Eratostenesa."))))
