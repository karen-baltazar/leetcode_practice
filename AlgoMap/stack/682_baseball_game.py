class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Hint: Use a list to simulate a stack where each element represents a score round.
        record = []

        for op in operations:
            if op == "+":
                record.append(record[-2] + record[-1])
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))

        return sum(record)
