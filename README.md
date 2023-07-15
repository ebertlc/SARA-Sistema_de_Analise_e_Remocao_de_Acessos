# S.A.R.A. - Sistema de Análise e Remoção de Acesso

Este é um código Python que implementa o Sistema de Análise e Remoção de Acesso (S.A.R.A.). O objetivo do sistema é automatizar o processo de análise e remoção de acesso de usuários com base em um conjunto de critérios.

## Pré-requisitos

Antes de executar este código, certifique-se de ter instalado as seguintes dependências:

- [Python](https://www.python.org) (versão 3.6 ou superior)
- [Selenium](https://selenium-python.readthedocs.io) (biblioteca Python para automação de navegador)
- [pandas](https://pandas.pydata.org) (biblioteca Python para manipulação de dados)
- Navegador Firefox (instalado e configurado)

Além disso, é necessário ter um arquivo no formato Excel (xlsx) contendo os usuários a serem analisados. O arquivo deve conter as seguintes colunas: 'EMAIL', 'NOME', 'TIPO_USUARIO', 'Ano_DT_ULTIMO_LOGIN'. O caminho do arquivo deve ser definido na variável `caminho_dataset`.

## Configuração

Antes de executar o código, você precisa configurar algumas informações:

- `email@dominio.com`: substitua pelo seu endereço de e-mail para fazer login no sistema.
- `senha`: substitua pela sua senha de acesso ao sistema.
- `C:\\caminho\\para\\usuarios_desabilitar.xlsx`: substitua pelo caminho completo do arquivo Excel contendo os usuários a serem analisados.

```python
usuario_login.send_keys('email@dominio.com')
senha_login.send_keys('senha')
usuarios = pd.read_excel('C:\\caminho\\para\\usuarios_desabilitar.xlsx')
```

## Executando o código

Após a configuração, você pode executar o código Python. Certifique-se de que todas as dependências estejam instaladas corretamente e que o navegador Firefox esteja em execução.

O código automatizará o processo de análise e remoção de acesso dos usuários. Ele fará login no sistema, pesquisará cada usuário no arquivo Excel, verificará se o usuário atende aos critérios especificados e, se necessário, desabilitará o acesso do usuário. O resultado da análise será salvo em um novo arquivo Excel.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar solicitações de pull request para aprimorar o sistema.

## Autores

Eber Lucas Cerqueira Elias
