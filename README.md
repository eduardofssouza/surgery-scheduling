# Otimização de Alocação de Cirurgias com Pyomo

Este projeto utiliza o **Pyomo**, um pacote de otimização em Python, para resolver problemas fictício simples de alocação de cirurgias em salas cirúrgicas. O modelo considera diversas variáveis, como custos, prioridades, tempos de cirurgia, e a disponibilidade de médicos e salas. O objetivo é minimizar os custos totais enquanto atende às restrições de tempo e disponibilidade dos recursos hospitalares.

## Funcionalidades

- **Geração Automática de Instâncias**: O código gera instâncias artificiais aleatórias de problemas de alocação de cirurgias, permitindo testes em diferentes cenários. O usuário pode especificar quantas instâncias deseja gerar.
- **Modelo de Otimização**: Utiliza o Pyomo e o solver GLPK para resolver o problema de alocação, garantindo a melhor distribuição de cirurgias nas salas, minimizando os custos.
- **Resultados Detalhados**: Após a resolução de cada instância, o código exibe a alocação das cirurgias nas salas, o valor da função objetivo e o custo total das cirurgias.
- **Formulação Matemática Completa**: A descrição inclui a formulação matemática do modelo, facilitando a compreensão e possíveis extensões futuras.

## Formulação Matemática

### Índices

- $\( I \)$: Conjunto de cirurgias, $\( I = \{1, 2, \dots, n\} \)$
- $\( J \)$: Conjunto de salas cirúrgicas, $\( J = \{1, 2, \dots, m\} \)$

### Parâmetros

- $\( c_i \)$: Custo associado à cirurgia $\( i \in I)$
- $\( p_i \)$: Prioridade da cirurgia $\( i \in I)$
- $\( t_i \)$: Tempo necessário para a cirurgia $\( i \in I)$
- $\( T_j \)$: Tempo disponível na sala $\( j \in J)$
- $\( s_j \)$: Especialização da sala $\( j \in J)$ (e.g., 'geral', 'cardíaca', etc.)
- $\( d_{i,j} \)$: Disponibilidade do médico para a cirurgia $\( i \in I)$ na sala $\( j \in J)$ (1 se disponível, 0 caso contrário)
- $\( \delta \)$: Tempo de preparação entre cirurgias

### Variáveis de Decisão

- $\( x_{i,j} \)$: Variável binária que assume valor 1 se a cirurgia $\( i \in I )$ é alocada à sala $\( j \in J)$, ou 0, caso contrário.

### Função Objetivo

Minimizar o custo total ponderado das cirurgias:

![image](https://github.com/user-attachments/assets/f9f2b522-c327-432c-96f6-8855344a6d98)

### Restrições

1. **Alocação Única de Cirurgias**: Cada cirurgia deve ser alocada a exatamente uma sala.

   ![image](https://github.com/user-attachments/assets/ff252d59-ce00-498d-a59d-c35b138d6830)

2. **Capacidade das Salas**: O tempo total das cirurgias alocadas a uma sala, mais o tempo de preparação entre elas, não deve exceder a disponibilidade da sala.
  
   ![image](https://github.com/user-attachments/assets/f8e8c222-4563-4524-8ebc-70272fec079f)

3. **Especialização das Salas**: Uma cirurgia só pode ser alocada a uma sala que possui a especialização adequada.

![image](https://github.com/user-attachments/assets/f4a49f61-428c-4226-be3f-a7b164cc499a)

4. **Disponibilidade dos Médicos**: Uma cirurgia só pode ser alocada a uma sala se o médico estiver disponível.

  ![image](https://github.com/user-attachments/assets/62b466d8-f9a3-40eb-a04b-03b1276007c9)

### Implementação no Pyomo

O modelo acima é implementado utilizando o Pyomo, onde as variáveis de decisão são definidas como binárias, e as restrições são implementadas conforme descrito. O solver GLPK é utilizado para encontrar a solução ótima.

## Como Funciona

1. **Geração de Dados**: O código gera aleatoriamente cirurgias e salas com parâmetros como tempo de cirurgia, tempo de preparação, custos e prioridades.
2. **Criação do Modelo**: Um modelo de programação inteira mista é construído com as variáveis e restrições que garantem a viabilidade da alocação das cirurgias.
3. **Solução**: O modelo é resolvido usando o solver GLPK.
4. **Exibição de Resultados**: A solução encontrada é apresentada, mostrando quais cirurgias foram alocadas a quais salas e o custo total da alocação.

## Requisitos

- Python 3.11
- Pyomo
- Solver GLPK

## Como Usar

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/eduardofssouza/surgery-scheduling.git
   ```
2. **Instale as dependências**:
   ```bash
   pip install pyomo
   ```
   Certifique-se de que o solver GLPK está instalado e acessível em seu ambiente de desenvolvimento.
   
3. **Execute o código principal**:
   ```bash
   python main.py
   ```

4. **Personalize as Instâncias**: Modifique o número de instâncias geradas diretamente no código ou personalize os parâmetros para adaptar o modelo às suas necessidades.

## Exemplo de Saída

```
Rodando instância 1...
Número de cirurgias: 4
Número de salas cirúrgicas: 3
Tempo de cirurgia (em horas): {1: 2, 2: 4, 3: 3, 4: 1}
Tempo disponível nas salas (em horas): {1: 8, 2: 7, 3: 6}
Custo de cada cirurgia: {1: 150, 2: 220, 3: 170, 4: 130}
Prioridade das cirurgias: {1: 2, 2: 3, 3: 1, 4: 2}
Tempo de preparação entre cirurgias (em horas): 0.7

Alocação de cirurgias:
Cirurgia 1 está alocada à Sala 1
Cirurgia 2 está alocada à Sala 3
Cirurgia 3 está alocada à Sala 2
Cirurgia 4 está alocada à Sala 1

Valor da função objetivo: 1320.0
Custo total das cirurgias: 670
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias e correções.

---
