import random

# Função para gerar n instâncias aleatórias
def gerar_instancias_aleatorias(n_instancias):
    instancias = []
    
    for _ in range(n_instancias):
        n_cirurgias = random.randint(3, 6)  # Número de cirurgias entre 3 e 6
        n_salas = random.randint(2, 4)  # Número de salas entre 2 e 4
        
        cirurgias = list(range(1, n_cirurgias + 1))
        salas = list(range(1, n_salas + 1))
        
        tempo_cirurgia = {i: random.randint(1, 5) for i in cirurgias}  # Duração da cirurgia entre 1 e 5 horas
        tempo_sala = {j: random.randint(5, 10) for j in salas}  # Duração disponível da sala entre 5 e 10 horas
        
        custo_cirurgia = {i: random.randint(100, 300) for i in cirurgias}  # Custo de cada cirurgia entre 100 e 300
        prioridade = {i: random.randint(1, 3) for i in cirurgias}  # Prioridade da cirurgia de 1 a 3
        
        especializacao_sala = {j: ['geral'] for j in salas}  # Todas as salas são de especialização geral
        disponibilidade_medico = {(i, j): 1 for i in cirurgias for j in salas}  # Todos os médicos estão disponíveis para todas as cirurgias
        
        tempo_preparacao = random.uniform(0.5, 1)  # Tempo de preparação entre 0.5 e 1 hora
        
        instancia = {
            'cirurgias': cirurgias,
            'salas': salas,
            'tempo_cirurgia': tempo_cirurgia,
            'tempo_sala': tempo_sala,
            'custo_cirurgia': custo_cirurgia,
            'prioridade': prioridade,
            'especializacao_sala': especializacao_sala,
            'disponibilidade_medico': disponibilidade_medico,
            'tempo_preparacao': tempo_preparacao
        }
        
        instancias.append(instancia)
    
    return instancias