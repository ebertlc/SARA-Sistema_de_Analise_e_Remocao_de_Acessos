**S.A.R.A. - Sistema de Análise e Remoção de Acesso**

Este é o código-fonte do S.A.R.A. (Sistema de Análise e Remoção de Acesso), um sistema automatizado para análise, desabilitação e verificação de usuários do S2iD(Sistema Integrado de Informações Sobre Desastres) versão 3.8.3.

**Recursos e Funcionalidades**

- Utiliza a biblioteca Selenium para automatizar interações em um navegador web.
- Carrega uma lista de usuários a partir de um arquivo Excel.
- Realiza login e acessa a página de administração de usuários no sistema.
- Verifica critérios para cada usuário na lista:
  - Ano do último login anterior a 2023.
  - Status do usuário é "Habilitado".
  - Nome cadastrado é igual ao nome do usuário na lista.
  - Tipo do usuário é igual ao tipo na lista.
- Desabilita os usuários que atendem aos critérios.
- Atualiza a planilha Excel com os resultados da análise.
- Executa a função "jhon" para verificar se as ações de desabilitação foram executadas corretamente.
 - Salva os resultados em novos arquivos Excel.

**Requisitos de Instalação e Configuração**

- Instale o Python (versão compatível com o código).
- Instale as dependências necessárias:
  - selenium
  - pandas
- Certifique-se de ter o driver adequado para o navegador utilizado (por exemplo, o driver do Firefox).

**Como Usar**

1. Configure o caminho do arquivo Excel contendo a lista de usuários a serem analisados.
2. Informe na função login o nome de usuario e senhas do cadastrador do sistema.
3. Execute o código.
4. Acompanhe o processo de análise, desabilitação e verificação na saída do terminal.
5. Os resultados serão salvos em novos arquivos Excel.


**Contribuições**

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar solicitações de pull request para aprimorar o sistema.

**Autores**

Eber Lucas Cerqueira Elias
