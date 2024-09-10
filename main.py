from src.model import criar_modelo, resolver_modelo, exibir_resultados
from src.instances_gen import gerar_instancias_aleatorias

# Função principal para testar todas as instâncias geradas
def main(n_instancias):
    instancias = gerar_instancias_aleatorias(n_instancias)
    
    for index, dados in enumerate(instancias):
        print(f"\nRodando instância {index + 1}...")
        cirurgias = dados['cirurgias']
        salas = dados['salas']
        tempo_cirurgia = dados['tempo_cirurgia']
        tempo_sala = dados['tempo_sala']
        custo_cirurgia = dados['custo_cirurgia']
        prioridade = dados['prioridade']
        especializacao_sala = dados['especializacao_sala']
        disponibilidade_medico = dados['disponibilidade_medico']
        tempo_preparacao = dados['tempo_preparacao']

        # Exibir detalhes da instância antes de resolver
        print(f"Número de cirurgias: {len(cirurgias)}")
        print(f"Número de salas cirúrgicas: {len(salas)}")
        print(f"Tempo de cirurgia (em horas): {tempo_cirurgia}")
        print(f"Tempo disponível nas salas (em horas): {tempo_sala}")
        print(f"Custo de cada cirurgia: {custo_cirurgia}")
        print(f"Prioridade das cirurgias: {prioridade}")
        print(f"Tempo de preparação entre cirurgias (em horas): {tempo_preparacao}")

        # Criar o modelo para a instância atual
        model = criar_modelo(cirurgias, salas, tempo_cirurgia, tempo_sala, custo_cirurgia, prioridade, especializacao_sala, disponibilidade_medico, tempo_preparacao)
        
        # Resolver o modelo
        model = resolver_modelo(model)
        
        # Verificar se o modelo foi resolvido com sucesso antes de exibir resultados
        if model:
            # Exibir os resultados
            exibir_resultados(model, cirurgias, salas, custo_cirurgia)
        else:
            print(f"Falha na resolução do modelo para a instância {index + 1}.")

# Executar o programa principal com 5 instâncias
if __name__ == '__main__':
    main(5)  # Aqui você define quantas instâncias deseja gerar e resolver