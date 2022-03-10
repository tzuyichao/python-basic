class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n/2)
        else:
            return 2 + min(self.integerReplacement((n-1)/2), self.integerReplacement((n+1)/2))


if __name__ == '__main__':
    solution = Solution()
    print(f'solution.integerReplacement(8): {solution.integerReplacement(8)}')
    print(f'solution.integerReplacement(7): {solution.integerReplacement(7)}')