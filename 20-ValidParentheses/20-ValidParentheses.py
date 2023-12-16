                elif top == '{' and char == '}':
                    continue
                if top == '(' and char == ')':
                    top = stack.pop()
            if char in [')', '}', ']']:
                continue
                stack.append(char)
            if char == '(' or char == '{' or char == '[':
        for char in s:
        stack = []
    def isValid(self, s: str) -> bool:
                try:
                except IndexError:
                    return False
"
