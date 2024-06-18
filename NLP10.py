import ast
import operator

variables = {'p': True, 'q': True, 'r': False}

operators = {
    ast.And: operator.and_,
    ast.Or: operator.or_,
    ast.Not: operator.not_,
    ast.BitAnd: operator.and_,
    ast.BitOr: operator.or_,
    ast.Invert: operator.not_
}

def evaluate(node, variables):
    if isinstance(node, ast.BoolOp):
        left = evaluate(node.values[0], variables)
        for value in node.values[1:]:
            right = evaluate(value, variables)
            left = operators[type(node.op)](left, right)
        return left
    elif isinstance(node, ast.UnaryOp):
        operand = evaluate(node.operand, variables)
        return operators[type(node.op)](operand)
    elif isinstance(node, ast.Name):
        return variables[node.id]
    elif isinstance(node, ast.Constant):
        return node.value
    else:
        raise ValueError(f"Unsupported node type: {type(node)}")

def parse_expression(expression, variables):
    tree = ast.parse(expression, mode='eval')
    return evaluate(tree.body, variables)

expressions = ["p and q", "p or r", "not p", "q and (r or p)"]

for expr in expressions:
    result = parse_expression(expr, variables)
    print(f"{expr} => {result}")
