from typing import List
class Solution:
    def fizzbuzz(self, n: int) -> List[str]:
        return ["Fizz"*(d%3==0) + "Buzz"*(d%5==0) or str(d) for d in range(1, n+1)]

    def fizzbuzz2(self, n: int) -> List[str]:
        output = []
        for i in range(1, n+1):
            elem_to_append = ""
            if i%3 == 0:
                elem_to_append = "Fizz"
            if i%5 == 0:
                elem_to_append += "Buzz"
            if not elem_to_append:
                elem_to_append = str(i)
            output.append(elem_to_append)
        return output

if __name__ == "__main__":
    S = Solution()
    test_n = [3, 5, 15]
    expected = [
        ["1", "2", "Fizz"],
        ["1", "2", "Fizz", "4", "Buzz"],
        ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"],
    ]
    for n, exp in zip(test_n, expected):
        assert S.fizzbuzz(n) == exp, f"{S.fizzbuzz(n)} != {exp}"
        print("Success!")
