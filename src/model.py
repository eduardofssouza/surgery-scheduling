from pyomo.environ import *

# Função para criar o modelo
def criar_modelo(cirurgias, salas, tempo_cirurgia, tempo_sala, custo_cirurgia, prioridade, especializacao_sala, disponibilidade_medico, tempo_preparacao):
    model = ConcreteModel()

    model.x = Var(cirurgias, salas, within=Binary)

    def obj_rule(model):
        return sum(prioridade[i] * custo_cirurgia[i] * model.x[i, j] for i in cirurgias for j in salas)
    model.obj = Objective(rule=obj_rule, sense=minimize)

    model.cirurgia_agendada_uma_sala = Constraint(cirurgias, rule=lambda model, i: sum(model.x[i, j] for j in salas) == 1)

    model.tempo_sala_com_preparacao = Constraint(salas, rule=lambda model, j: sum(tempo_cirurgia[i] * model.x[i, j] for i in cirurgias) + tempo_preparacao * (sum(model.x[i, j] for i in cirurgias) - 1) <= tempo_sala[j])

    def especializacao_adequada_rule(model, i, j):
        return model.x[i, j] <= (1 if 'geral' in especializacao_sala[j] else 0)
    model.especializacao_adequada = Constraint(cirurgias, salas, rule=especializacao_adequada_rule)

    model.medico_disponivel = Constraint(cirurgias, salas, rule=lambda model, i, j: model.x[i, j] <= disponibilidade_medico[(i, j)])

    return model

# Função para resolver o modelo
def resolver_modelo(model):
    solver = SolverFactory('glpk')
    result = solver.solve(model)
    
    # Verificar o status do solver
    if result.solver.termination_condition == TerminationCondition.optimal:
        return model
    elif result.solver.termination_condition == TerminationCondition.infeasible:
        print("Modelo inviável!")
    else:
        print(f"Modelo não resolveu. Status: {result.solver.termination_condition}")
    
    return None  # Retorna None se não houver solução viável


# Função para exibir os resultados se o resultado for viável
def exibir_resultados(model, cirurgias, salas, custo_cirurgia):
    # Verifica se o modelo foi resolvido com uma solução viável
    if not model:
        print("Nenhum resultado a exibir, o modelo não foi resolvido corretamente.")
        return  # Se o modelo for None, passa e não imprime nada
    
    # Se for viável, imprime os resultados
    print("\nAlocação de cirurgias:")
    custo_total = 0
    for i in cirurgias:
        for j in salas:
            if value(model.x[i, j]) == 1:
                print(f"Cirurgia {i} está alocada à Sala {j}")
                custo_total += custo_cirurgia[i]
    
    print(f"\nValor da função objetivo: {value(model.obj)}")
    print(f"Custo total das cirurgias: {custo_total}")