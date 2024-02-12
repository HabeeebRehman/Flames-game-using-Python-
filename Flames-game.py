def remove_matching_letters(s1, s2):
    for i in s1:
        for j in s2:
            if i == j:
                s1.remove(i)
                s2.remove(j)
                return True
    return False

def flames_game():
    name1 = input()
    name2 = input()

    name1 = list(name1.lower().replace(" ", ""))
    name2 = list(name2.lower().replace(" ", ""))

    while remove_matching_letters(name1, name2):
        pass

    count = len(name1) + len(name2)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemies", "Siblings"]

    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[:split_index]
            result = right + left
        else:
            result = result[:len(result) - 1]

    print("Relationship status:", result[0])

flames_game()