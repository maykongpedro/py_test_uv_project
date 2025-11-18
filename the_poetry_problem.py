# Resolução do problema de maneira direta

## 1. Importar bibliotecas
import pyomo.environ as pyo

## 2. Importar e definir solver
solver = pyo.SolverFactory("glpk")

## 3. Declarar modelo
modelo = pyo.ConcreteModel()

## 4. Declarar Variáveis de decisão
modelo.x1 = pyo.Var(within=pyo.NonNegativeReals)
modelo.x2 = pyo.Var(within=pyo.NonNegativeReals)

## 5. Declarar função objetivo
modelo.z = pyo.Objective(expr=90 * modelo.x1 + 120 * modelo.x2, sense=pyo.maximize)

## 6. Declarar restrições
modelo.restricao_tempo_disp = pyo.Constraint(expr=2 * modelo.x1 + 3 * modelo.x2 <= 180)
modelo.restricao_area_pinus = pyo.Constraint(expr=modelo.x1 <= 40)
modelo.restricao_area_nativas = pyo.Constraint(expr=modelo.x2 <= 50)

## 7. Resolver modelo
modelo.pprint()
resultado = solver.solve(modelo)


## 8. Exportar resultados
resultado.write

print("\n===== RESULTADOS DO MODELO =====")
print(f"Status da otimização: {resultado.solver.status}")
print(f"Condição de término: {resultado.solver.termination_condition}")
print(f"Receita máxima (z) = R${pyo.value(modelo.z):.2f}")
print(f"Área manejada de Pinus (x1) = {modelo.x1():.2f} hectares")
print(f"Área manejada de Nativa (x2) = {modelo.x2():.2f} hectares")
