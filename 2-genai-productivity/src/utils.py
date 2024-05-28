import ast
import operator

import numpy as np


class Calculator:
    def __init__(self):
        self.operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.BitXor: operator.xor,
        }

    def eval_expr(self, expr):
        try:
            # Parse the expression
            node = ast.parse(expr, mode='eval').body
            return self._eval(node)
        except Exception as e:
            return str(e)

    def _eval(self, node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return self.operators[type(node.op)](self._eval(node.left), self._eval(node.right))
        else:
            raise ValueError(f"Unsupported operation: {node}")


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
