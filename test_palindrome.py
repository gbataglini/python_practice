from unittest import TestCase, main

from palindrome import palindrome


class TestPalindromeVars(TestCase):
    def test_word(self):
        result = palindrome('madam')
        self.assertEqual(result, True)

    def test_sentence(self):
        result = palindrome('murder for a jar of red rum')
        self.assertEqual(result, True)

    def test_casing(self):
        result = palindrome('Race CAR')
        self.assertEqual(result, True)


class TestNonPalindromes(TestCase):
    def test_not_palindrome(self):
        result = palindrome('not a palindrome')
        self.assertEqual(result, False)

    def test_nearly_palindrome(self):
        result = palindrome('madamm')
        self.assertEqual(result, False)


if __name__ == "__main__":
    main()
