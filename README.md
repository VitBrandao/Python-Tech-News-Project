# Boas-vindas ao repositório do Tech News
---

# Requisitos obrigatórios

## 1 - Crie a função `fetch`
local: `tech_news/scraper.py`

Antes de fazer scrape, precisamos de uma página! Esta função será responsável por fazer a requisição HTTP ao site e obter o conteúdo HTML.
Alguns cuidados deverão ser tomados: como a nossa função poderá ser utilizada várias vezes em sucessão, na nossa implementação devemos nos assegurar que um [Rate Limit](https://app.betrybe.com/course/computer-science/redes-e-raspagem-de-dados/raspagem-de-dados/ab38ab4e-bdbd-4984-8987-1abf32d85f26/conteudos/4edde8f1-9d55-4c98-a593-e3043848a127/alguns-problemas/) será respeitado.

- A função deve receber uma URL
- A função deve fazer uma requisição HTTP `get` para esta URL utilizando a função `requests.get`
- A função deve retornar o conteúdo HTML da resposta.
- A função deve respeitar um Rate Limit de 1 requisição por segundo; Ou seja, caso chamada múltiplas vezes, ela deve aguardar 1 segundo entre cada requisição que fizer.
**Dica:** Uma forma simples de garantir que cada requisição seja feita com um intervalo mínimo de um segundo é utilizar `time.sleep(1)` antes de cada requisição. (Existem outras formas mais eficientes.)
- Caso a requisição seja bem sucedida com `Status Code 200: OK`, deve ser retornado seu conteúdo de texto;
- Caso a resposta tenha o código de status diferente de `200`, deve-se retornar `None`;
- Caso a requisição não receba resposta em até 3 segundos, ela deve ser abandonada (este caso é conhecido como "Timeout") e a função deve retornar None.

📌 Você vai precisar definir o _header_ `user-agent` para que a raspagem do blog da Trybe funcione corretamente. Para isso, preencha com o valor `"Fake user-agent"` conforme exemplo abaixo:

```python
{ "user-agent": "Fake user-agent" }
```

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>

  Abra um terminal Python importando estas funções através do comando:

  `python3 -i tech_news/scraper.py`

  Agora invoque as funções utilizando diferentes parâmetros.
  Exemplo: 

  ```python
  html = fetch(url_da_noticia)
  scrape_noticia(html)
  ```
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - A função utiliza o método get() da biblioteca requests

  - A função executada com uma URL correta retorna o conteúdo html

  - A função, sofrendo timeout, retorna None

  - A função retorna None quando recebe uma resposta com código diferente de 200

  - A função respeita o rate limit

</details>

## 2 - Crie a função `scrape_novidades`
local: `tech_news/scraper.py`

Para conseguirmos fazer o scrape da página de uma notícia, primeiro precisamos de links para várias páginas de notícias. Estes links estão contidos na página inicial do blog da Trybe (https://blog.betrybe.com). 

Esta função fará o scrape da página Novidades para obter as URLs das páginas de notícias. Vamos utilizar as ferramentas que aprendemos no curso, como a biblioteca Parsel, para obter os dados que queremos de cada página.

- A função deve receber uma string com o conteúdo HTML da página inicial do blog
- A função deve fazer o scrape do conteúdo recebido para obter uma lista contendo as URLs das notícias listadas.
    - ⚠️ *Atenção:* **NÃO** inclua a notícia em destaque da primeira página, apenas as notícias dos cards.
- A função deve retornar esta lista.
- Caso não encontre nenhuma URL de notícia, a função deve retornar uma lista vazia.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>

  Abra um terminal Python importando estas funções através do comando:
  
  `python3 -i tech_news/scraper.py`
  
  Agora invoque as funções utilizando diferentes parâmetros. Exemplo: 

  ```python
  html = fetch(url_da_noticia)
  scrape_novidades(html)
  ```
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - A função retorna os dados esperados quando chamada com os parâmetros corretos

  - A função retorna uma lista vazia quando chamada com parâmetros incorretos

</details>

## 3 - Crie a função `scrape_next_page_link`
local: `tech_news/scraper.py`

Para buscar mais notícias, precisaremos fazer a paginação, e para isto, vamos precisar do link da próxima página. Esta função será responsável por fazer o scrape deste link.

- A função deve receber como parâmetro uma `string` contendo o conteúdo HTML da página de novidades (https://blog.betrybe.com)
- A função deve fazer o scrape deste HTML para obter a URL da próxima página.
- A função deve retornar a URL obtida.
- Caso não encontre o link da próxima página, a função deve retornar `None`

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - A função retorna os dados esperados quando chamada com os parâmetros corretos

  - A função retorna None quando chamada com os parâmetros incorretos

</details>

## 4 - Crie a função `scrape_noticia`
local: `tech_news/scraper.py`

Agora que sabemos pegar páginas HTML, e descobrir o link de notícias, é hora de fazer o scrape dos dados que procuramos! 

- A função deve receber como parâmetro o conteúdo HTML da página de uma única notícia
- A função deve, no conteúdo recebido, buscar as informações das notícias para preencher um dicionário com os seguintes atributos:
  - `url` - link para acesso da notícia.
  - `title` - título da notícia.
  - `timestamp` - data da notícia, no formato `dd/mm/AAAA`.
  - `writer` - nome da pessoa autora da notícia.
  - `comments_count` - número de comentários que a notícia recebeu.
    - Se a informação não for encontrada, salve este atributo como `0` (zero)
  - `summary` - o primeiro parágrafo da notícia.
  - `tags` - lista contendo tags da notícia.
  - `category` - categoria da notícia.

- Exemplo de um retorno da função com uma notícia fictícia:

```json
{
  "url": "https://blog.betrybe.com/novidades/noticia-bacana",
  "title": "Notícia bacana",
  "timestamp": "04/04/2021",
  "writer": "Eu",
  "comments_count": 4,
  "summary": "Algo muito bacana aconteceu",
  "tags": ["Tecnologia", "Esportes"],
  "category": "Ferramentas",
}
  ```

📌 Muita atenção aos tipos dos campos, por exemplo, `tags` é uma lista, enquanto que `comments_count` é numérico e `category` é uma string.

📌 Os textos coletados em `title` e `summary` podem conter alguns caracteres vazios ao final. O teste espera que esses caracteres sejam removidos.

📌 Para o campo `comments_count`, como há poucas notícias com comentários, utilizem [esta notícia](https://blog.betrybe.com/carreira/passos-fundamentais-para-aprender-a-programar/) como referência para scrape desta informação.

📌 **É bom saber que** ao fazer scraping na vida real, você está sempre "refém" de quem construiu o site. Por exemplo, pode ser que nem toda notícia tenha **exatamente** o mesmo HTML/CSS e você precise de criatividade para contornar isso. 

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - Será verificado se a função retorna o conteúdo correto e no formato correto, dada uma página de notícia exemplo.

</details>

---

#### <strong>👍 Terminou o requisito 4?</strong>
Parabéns! Este é o requisito mais longo do projeto, e também a funcionalidade central do nosso tech-news. Faça um break, tome uma água, e #vamoquevamo para os próximos requisitos!

---


## 5 - Crie a função `get_tech_news` para obter as notícias!
local: `tech_news/scraper.py`

Agora, chegou a hora de aplicar todas as funções que você acabou de fazer. Com estas ferramentas prontas, podemos fazer nosso scraper mais robusto com a paginação.

- A função deve receber como parâmetro um número inteiro `n` e buscar as últimas `n` notícias do site.
- Utilize as funções `fetch`, `scrape_novidades`, `scrape_next_page_link` e `scrape_noticia` para buscar as notícias e processar seu conteúdo.
- As notícias buscadas devem ser inseridas no MongoDB; Para acessar o banco de dados, importe e utilize as funções que já temos prontas em `tech_news/database.py`
- Após inserir as notícias no banco, a função deve retornar estas mesmas notícias.

📌 De aqui em diante, usaremos o MongoDB.

Rodar MongoDB via Docker: `docker-compose up -d mongodb` no terminal. 
Para mais detalhes acerca do mongo com o docker, olhe o arquivo `docker-compose.yml`

Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:
Ubuntu: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/  
MacOS:  https://docs.mongodb.com/guides/server/install/
  
Com o banco de dados rodando, o nosso módulo conseguirá acessá-lo sem problemas. Importe o módulo `tech_news/database.py` e chame as funções contidas nele.
Não altere as funções deste módulo; elas serão utilizadas nos testes.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- A função `create_news` do `tech_news/database.py` foi chamada corretamente

- A função retorna a quantidade correta de notícias

</details>

## 6 - Crie a função `search_by_title`
local: `tech_news/analyzer/search_engine.py`

Agora que temos meios de popular nosso banco de dados com notícias, podemos começar a fazer as buscas! Esta função irá fazer buscas por título.

- A função deve receber uma string com um título de notícia
- A função deve buscar as notícias do banco de dados por título
- A função deve retornar uma lista de tuplas com as notícias encontradas nesta busca. 
Exemplo: 
```python
[
  ("Título1_aqui", "url1_aqui"),
  ("Título2_aqui", "url2_aqui"),
  ("Título3_aqui", "url3_aqui"),
]
```
- A busca deve ser _case insensitive_
- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

📌 Lembre-se; para acesso ao banco de dados importe `db` definido no módulo `tech_news/database.py`.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  Abra um terminal Python importando esta função através do comando
  
  `python3 -i tech_news/analyzer/search_engine.py`
  
  Agora invoque a função utilizando diferentes parâmetros. Exemplo:
  
  `search_by_title("Algoritmos")`.

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - Será validado que é possível buscar uma notícia pelo título com sucesso

  - Será validado que ao buscar por um título que não existe, o retorno deve ser uma lista vazia

  - Será validado que é possível buscar uma notícia com sucesso, tanto pelo título em maiúsculas como em minúsculas.

</details>


## 7 - Crie a função `search_by_date`
local: `tech_news/analyzer/search_engine.py`

Esta função irá buscar as notícias do banco de dados por data.

- A função deve receber como parâmetro uma data no formato ISO `AAAA-mm-dd`
- A função deve buscar as notícias do banco de dados por data.
- A função deve ter retorno no mesmo formato do requisito anterior.
- Caso a data seja inválida, ou esteja em outro formato, uma exceção `ValueError` deve ser lançada com a mensagem `Data inválida`.
- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

📌 Lembre-se: A função recebe uma data no formato ISO `AAAA-mm-dd`, mas no banco a data está salva no formato `dd/mm/AAAA`. **Dica:** Lembrem-se de como trabalhamos com datas nos projetos anteriores.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  Abra um terminal Python importando esta função através do comando
  
  `python3 -i tech_news/analyzer/search_engine.py`
  
  Agora invoque a função utilizando diferentes parâmetros. Exemplo:
  
  `search_by_date("2021-04-04")`

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - Será validado que é possível buscar uma notícia pela data com sucesso

  - Será validado que ao buscar por uma data que não existe, o retorno deve ser uma lista vazia

  - Sera validado que ao buscar por uma data com formato inválido, deve lançar um erro `ValueError` com a mensagem `Data inválida`.

</details>

## 8 - Crie a função `search_by_tag`,
local: `tech_news/analyzer/search_engine.py`

Esta função irá buscar as notícias por tag.

- A função deve receber como parâmetro o nome da tag completo.
- A função deve buscar as notícias do banco de dados por tag.
- A função deve ter retorno no mesmo formato do requisito anterior.
- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.
- A busca deve ser _case insensitive_

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  Abra um terminal Python importando esta função através do comando:
  
  `python3 -i tech_news/analyzer/search_engine.py`
  
  Agora invoque a função utilizando diferentes parâmetros.
  Exemplo:
  
  `search_by_tag("Tecnologia")`.

</details>


<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - Será validado que é possível buscar uma notícia pela tag com sucesso

  - Será validado que ao buscar por uma tag que não existe, o retorno deve ser uma lista vazia

  - Será validado que é possível buscar uma notícia tanto pela tag em maiúsculas como em minúsculas

</details>

## 9 - Crie a função `search_by_category`
local: `tech_news/analyzer/search_engine.py`

Esta função irá buscar as notícias por categoria.

- A função deve receber como parâmetro o nome da categoria completo.
- A função deve buscar as notícias do banco de dados por categoria.
- A função deve ter retorno no mesmo formato do requisito anterior.
- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.
- A busca deve ser _case insensitive_

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  
  Abra um terminal Python importando esta função através do comando:
  
  `python3 -i tech_news/analyzer/search_engine.py`
  
  Agora invoque a função utilizando diferentes parâmetros. Exemplo:
  
  `search_by_category("Ferramentas")`.
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - Será validado que é possível buscar uma notícia pela categoria com sucesso

  - Será validado que ao buscar por uma categoria que não existe, o retorno deve ser uma lista vazia

  - Será validado que é possível buscar uma notícia tanto pela categoria em maiúsculas como em minúsculas

</details>