# Introdução e Arquitetura do Soft

De inicio foi pedido para criar um jogo de uma roleta junto com uma certa estrutura de dados, como qualquer um software pensamos em dinamica e agilidade. O jogo parte de uma lista pre-definida de inicio e o usuario via CLI (O console/terminal) tentaria advinhar qual dos itens da lista seria sorteada aleatoriamente, com a construção de um menu interativo que rodaria em loop até o usuario desejar encerrar o Game e com um opção de aumentar dificuldade.
O aumento da dificuldade seria basicamente adicionar um item a lista, pois matematicamente, ao adicionar um item a mais a probabilidade de acerto seria menor. Pensando:

| Diff      | Probabilidade |
| :-------- | ------------: |
| 3 (begin) |   1/3 ≃ 33.3% |
| 4         |     1/4 ≃ 25% |
| 5         |     1/5 ≃ 20% |

> Nessa sequencia, vermos que a porcentagem de acerto diminuir com o aumento da lista (diff)

### Arquitetura do projeto

Utilizamos um metodo Clean Code apesar do projeto ser basico e pequeno.
A ideia era implementar uma logica de arquivos onde cada um tinha seu objetivo:

- **_main.py_** -> Responsavel por ser o I/O, ou melhor, falava com o terminal e o usuario chamando os metodos da roleta. O entry pointer do jogo ou aplicação.
- **_roleta.py_** -> Interagia com a lista e implementava os metodos para o funcionamento do jogo, sem ser resposanvel com a entrada do usuario.
- **_lista_** -> Aqui criamos a Estrtura de Dados! Não sabe que a roleta existe e muito menos o que o usuario digitou.
- **_const.py_** -> Criado por IA (LLM). Uma GUI dedicada e limpa para o usuario se divertir e não deixar isso tudo para o arquivo main.

---

# Estrutura de Dados

A decisão de implementar uma Lista Encadeada Circular baseou-se puramente em uma mecanica da roleta real. Uma vez que nesse tipo de Estrutura de Dados (ED) guardamos como referencia o Tail (Cauda: o ultimo item da lista) apontando para o primeiro criando uma especie de Ciclo, literalmente, um circulo onde o final sempre aponta para o inicio!

- **INSERÇÃO (enqueue)**: Como sabemos como referencia direta em memoria de quem é o último item da lista, quando desejamos inserir um novo nó ao final da lista (enqueue) teremos em tempo de execução (Big O) uma rapida inserção de O(1). Essa eficiencia é ótima para quando desejamos aumentar a lista diferente de uma lista onde sabemos apenas o inicio (Head), pois deveriamos passar por toda estrutura até o final tendo um tempo O(N) - N sendo a quantidade de elementos da lista.

- **First Item**: Apesar da lista se parecer com um circulo abstrato, onde não há um "Inicio" ou um "Fim".Contudo, na nossa ED essa demarcação é deduzida de forma implicita. Como guardamos sempre o ultimo elemento (_self.tail_) sabendo dessa informação descobriremos instantaneamente o primeiro nó acessando o ponteiro _self.tail.next_. Essa caracteristica garante que o tempo de remoção do primeiro item e ao acesso dele ocorra de forma instantanea em tempo O(1), sem a necessidade de manter duas variaveis de estado na classe.

---

# Traversal ou Risco de Loop infinito

> Uma breve explicação desse possivel **BUG**

Uns dos riscos de manipulação de uma lista circular é a ausencia de um ponteiro Nulo (None) demarcando o ultimo item (nó) dessa estrutura, o que pode causar um loop infinito na hora de leitura ou impressão, como nos metodos _getItemsList_ e _printList_.

Nessa situação dos metodos e da solução desse bug utilizei uma tecnica de marcação de referencia temporaria (variavel **current**).
A iteração acontece no primeiro nó _current = self.tail.next_ que avança sequencialmente (_current = current.next_). A condição de parada não verifica se o nó é NULO igual em uma Lista Encadeada Simples, mas sim quando a referencia do nó atual (_is_) voltou a ser identica ao nó de partida. Isso garante que a gente pecorra a lista completa em um 360 antes de dar um break de forma segura.

---

# Conclusão final e Lógica

Para simular uma roleta de verdade, o código do jogo une duas coisas: o tamanho da lista (dificuldade) e um sorteio (aleatoriedade).

- **A Dificuldade:** O nível de dificuldade é literalmente a quantidade de itens na roleta. Quanto mais nós (_Nodes_) adicionamos à lista, menor se torna a chance matemática de o jogador acertar.
- **O Giro Realista:** Se fizéssemos um sorteio simples com o tamanho da lista, a roleta andaria poucas casas e pararia de forma rápida e previsível. Para resolver isso e criar suspense na _interface_, o programa multiplica o tamanho atual da lista por um número sorteado entre 2 e 8 (`random.randint(diff * 2, diff * 8)`).

Isso força a roleta a dar de duas a oito voltas completas antes de parar no resultado final. Essa lógica só é possível e livre de erros justamente porque construímos uma _Lista Circular Encadeada_, permitindo que o ponteiro continue girando sem nunca esbarrar em um "fim" de fila, entregando um comportamento sistêmico muito mais realista.
