············if·(len(current_str)·==·max·*·2):
················return·output.append(current_str)
············if·(open·<·max):
················backtrack(current_str·+·"(",·max,·close,·open·+·1)
············if·(close·<·open):
················backtrack(current_str·+·")",·max,·close·+·1,·open)

········def·backtrack(current_str,·max,·close,·open):
        '''solution using backtracking'''
        output·=·[]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
3
