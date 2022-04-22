def reverse(s):
    words = s.split()
    reversed_list = []

    for word in words:
        letters = []
        nonletter = []

        for index, char in enumerate(word):
            if char.isalpha():
                letters.append(char)
            if not char.isalpha():
                nonletter.append((index, char))

        letters = letters[::-1]

        for item in nonletter:
            letters.insert(*item)

        letters_string = "".join(letters)

        reversed_list.append(letters_string)

    reversed_text_string = " ".join(reversed_list)
    return reversed_text_string


if __name__ == '__main__':
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("rt5k ern!", "kt5r nre!"),
        ("", ""),
    ]

    for text, reversed_text in cases:
        assert reverse(text) == reversed_text

