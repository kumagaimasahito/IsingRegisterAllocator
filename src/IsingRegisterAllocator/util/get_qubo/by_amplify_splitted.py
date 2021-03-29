from amplify import BinaryPoly, gen_symbols, sum_poly, BinaryQuadraticModel
from amplify.constraint import equal_to, penalty

def by_amplify_splitted(list_dependent_variables, num_registers, allocation):
    num_variables = len(list_dependent_variables)
    q = gen_symbols(BinaryPoly, num_variables, num_registers)

    # 各変数を1つのレジスタに割り当てるOne-het制約
    const_onehot = [
        equal_to(sum_poly([q[i][r] for r in range(num_registers)]), 1)
        for i in range(num_variables)
    ]

    # レジスタスピルを減らすために，依存関係のある変数同士が同一のレジスタに割り当てられない制約
    const_spill = [
        penalty(q[i][r] * q[j][r])
        for i in range(num_variables)
        for j in list_dependent_variables[i]
        if i < j
        for r in range(num_registers)
    ]

    # ある変数が割り当てられるレジスタがわかっている時，必ずそのレジスタに割り当てられるようにする制約
    const_assign = [
        penalty(q[i][r])
        for i, x in allocation.items()
        for r in range(num_registers)
        if r != x
    ]

    constraints = sum(const_onehot)
    if len(const_spill) != 0:
        constraints += sum(const_spill)
    if len(const_assign) != 0:
        constraints += sum(const_assign)
    return {
        "qubits" : q,
        "model" : BinaryQuadraticModel(constraints)
    }
