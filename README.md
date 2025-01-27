
## Lógica da geração dos dados

Visando simular como seria a geração dos dados de um Ecommerce real, os dados serão gerados em um loop que percorre dia a dia, gera dados, como inclusão de um cliente, a possibilidade de alteração dos dados do cliente, pedidos de compra e avaliação dos produtos.

Os produtos e categorias foram gerados inicialmente e, apenas os produtos e categorias serão incluídos de uma única vez ao início da geração dos dados. Todo o restante será gerado de forma aleatória dia a dia.

### Passo a passo da geração dos dados

1 - Produtos e categorias são gerados todos inicialmente.

2 - Gera um preço a cada mês (dentro de uma faixa de 10% em relação ao preço base forncecido) para os produtos.

A seguir, é executada a lógica para cada dia. A data de início e fim deste projeto foi estabelecida como 2020-01-01 e 2024-12-31 respectivamente:

3 - Gera uma quantidade de 0 a 5 clientes.

4 - Gera um endereço para os clientes gerados (consulta o banco, verifica os clientes existentes e retorna um endereço para cada um deles).

5 - Armazena na tabela associativa clientes-endereços as chaves estrangeiras da tabela cliente e tabela endereço.

6 - Sorteia uma chance 1% de algum cliente modificar seus dados (telefone, ou endereço). Caso seja o endereço, armazena novamente na tabela associativa.

7 - Cria de 0 a 10 pedidos. Consulta o banco de dados, sorteia um cliente, sorteia um endereço do cliente, sorteia de 1 a 5 produtos. Para cada item do pedido, sorteie uma chance de 25% de o cliente avaliar este produto.