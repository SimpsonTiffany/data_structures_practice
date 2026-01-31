# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# TIMED CHALLENGE PROMPT:
# 13. Balanced Symbols
# Check if the brackets in a string are balanced.
# Input: "{[()]}" -> Output: True
# Input: "{[(])}" -> Output: False


def is_balanced(s):
    """
    Returns True if the brackets in s are balanced, otherwise False.
    Supported brackets: () [] {}
    Ignores all non-bracket characters.
    """
    if not isinstance(s, str):
        return False

    pairs = {")": "(", "]": "[", "}": "{"}
    openers = set(pairs.values())
    stack = []

    for ch in s:
        if ch in openers:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    # Basic tests
    print(is_balanced("{[()]}"))  # True
    print(is_balanced("{[(])}"))  # False
    print(is_balanced("()[]{}"))  # True
    print(is_balanced("([{}])"))  # True
    print(is_balanced("((("))  # False
    print(is_balanced(""))  # True (nothing to mismatch)

    # Edge cases
    print(is_balanced("no brackets"))  # True (ignores non-brackets)
    print(is_balanced("{[a+(b*c)]}"))  # True (ignores letters/operators)
    print(is_balanced("]"))  # False
    print(is_balanced(None))  # False
    print(is_balanced(12345))  # False


# Reflection (200–300 words):
# For this timed challenge, I chose a stack because the problem follows last-in, first-out logic.
# Every time I see an opening bracket like “(”, “[”, or “{”, I push it onto the stack. When I see a
# closing bracket, I check whether it matches the most recent opening bracket (the top of the stack).
# If it doesn’t match or the stack is empty, the string is not balanced. This approach is reliable
# because the only valid match for a closing bracket is the most recent unmatched opener.
#
# The 30-minute time limit shaped my decision by pushing me toward the most direct, standard solution
# instead of overengineering. I used a dictionary to map closing brackets to their matching openers,
# which kept the logic simple and reduced mistakes under pressure. I also chose to ignore non-bracket
# characters so the function can handle realistic inputs like code snippets, not just pure bracket strings.
#
# The biggest trade-off I made under time pressure was focusing on correctness and clarity rather than
# building extra features like detailed error messages or reporting the index of the failure. In an interview,
# I’d mention those enhancements as a follow-up improvement. Overall, this felt like good ROI practice because
# it reinforced the habit of quickly identifying the right data structure, writing clean code, and validating
# it with edge cases—exactly what technical interviews reward.
