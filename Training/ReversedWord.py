# Given a sentence, return a sentence with the words reversed


def reverse_expression(text):
    # METHOD 1
    print(" ".join(text.split()[::-1]))

    # METHOD 2
    reversed_text = text.split()
    reversed_text.reverse()
    print(" ".join(reversed_text))


reverse_expression("Third Second First")
