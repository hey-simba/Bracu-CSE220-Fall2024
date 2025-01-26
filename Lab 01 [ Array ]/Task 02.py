

# Task 02: Discard Cards

def discardCards(cards, t):
    for i in range(len(cards)):
        if cards[i] == None:
            cards[i] = 0

    size = 0

    for i in range(len(cards)):
        if cards[i] != 0:
            size += 1
        else:
            break

    counter = 1
    i = 0

    while i < size:
        if cards[i] != t:
            i += 1
        else:
            if counter % 2 == 0:
                i += 1
            else:
                for j in range(i, size - 1):
                    cards[j] = cards[j + 1]
                cards[size - 1] = 0
                size -= 1
            counter += 1

    return cards




print("///  Task 02: Discard Cards  ///")
cards = np.array([1,3,7,2,5,2,2,2,0])
returned_value = discardCards(cards, 2)
print(f'Task 2: {returned_value}') # This should print [1,3,7,5,2,2,0,0,0]
unittest.output_test(returned_value, np.array([1,3,7,5,2,2,0,0,0]))

cards = np.array([5,5,5,0,0])
returned_value = discardCards(cards, 5)
print(f'Task 2: {returned_value}') # This should print [5,0,0,0,0]
unittest.output_test(returned_value, np.array([5,0,0,0,0]))