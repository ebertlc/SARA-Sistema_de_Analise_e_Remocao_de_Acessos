from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

print('....................................................................................')
print('....................................................................................')
print('............... S.A.R.A. - Sistema de Análise e Remoção de Acesso ..................')
print('....................................................................................')
print('....................................................................................')

#....................................................................................
#................S.A.R.A. - Sistema de Análise e Remoção de Acesso...................
#....................................................................................

# Função para realizar o processo S.A.R.A.
def SARA():
    # Configurar o driver do Firefox
    driver = webdriver.Firefox()
    caminho_dataset = 'C:\\Users\\eber_\\Documents\\delveloper\\MIDR\\aquivos\\usuarios_desabilitar.xlsx'
    usuarios = base_usuarios(caminho_dataset)
    acessar_s2id(driver)
    login(driver)
    acesso_admin_usuarios(driver)

    # Iterar sobre cada usuário no dataframe
    for index, row in usuarios.iterrows():
        email = row['EMAIL']
        nome = row['NOME']
        tipo = row['TIPO_USUARIO']
        ano = row['Ano_DT_ULTIMO_LOGIN']

        # Verificar se o ano não é 2023
        if ano != 2023:
            pesquisar_usuario(email, driver)
            return_status = retorna_texto('formAdmCad:status2_label', driver)

            # Verificar se o status é "Habilitado"
            if return_status == 'Habilitado':
                return_nome_cadastrado = retorna_atributo('formAdmCad:j_idt129', driver)

                # Verificar se o nome cadastrado é igual ao nome do dataframe
                if nome == return_nome_cadastrado:
                    return_tipo = retorna_texto('formAdmCad:j_idt108_label', driver)

                    # Verificar se o tipo é igual ao tipo do dataframe
                    if return_tipo == tipo:
                        desabilitar_usuarios(driver)
                        atualizar_linha_planilha('ATT_SCRIPT', 'Ok', usuarios, index)
                    else:
                        atualizar_linha_planilha('ATT_SCRIPT', 'Análise', usuarios, index)
                else:
                    atualizar_linha_planilha('ATT_SCRIPT', 'Análise', usuarios, index)
            else:
                atualizar_linha_planilha('ATT_SCRIPT', 'Não Executado', usuarios, index)
        else:
            atualizar_linha_planilha('ATT_SCRIPT', 'Ativo', usuarios, index)

        print('---------------------------------------------------------------')
        print(f"Nome: {nome}")
        print('VERIFICADO')
        print('---------------------------------------------------------------')

    usuarios.to_excel('C:\\Users\\eber_\\Documents\\delveloper\\MIDR\\aquivos\\usuarios_desabilitar_att.xlsx', index=False)
    time.sleep(2)

    jhon(driver)
    return driver

# jhon Verifica de SARA fez o trabalho corretamente
def jhon(x):
    print('................ Execultando jhon ...................')
    driver = x
    caminho_dataset = 'C:\\Users\\eber_\\Documents\\delveloper\\MIDR\\aquivos\\usuarios_desabilitar_att.xlsx'
    usuarios = base_usuarios(caminho_dataset)

    # Iterar sobre cada usuário no dataframe
    for index, row in usuarios.iterrows():
        email = row['EMAIL']
        nome = row['NOME']
        tipo = row['TIPO_USUARIO']
        att = row['ATT_SCRIPT']

        # Verificar se a coluna ATT_SCRIPT é "Ok"
        if att == 'Ok':
            pesquisar_usuario(email, driver)
            return_status = retorna_texto('formAdmCad:status2_label', driver)

            # Verificar se o status é "Habilitado"
            if return_status == 'Habilitado':
                return_nome_cadastrado = retorna_atributo('formAdmCad:j_idt129', driver)

                # Verificar se o nome cadastrado é igual ao nome do dataframe
                if nome == return_nome_cadastrado:
                    return_tipo = retorna_texto('formAdmCad:j_idt108_label', driver)

                    # Verificar se o tipo é igual ao tipo do dataframe
                    if return_tipo == tipo:
                        desabilitar_usuarios(driver)
                        atualizar_linha_planilha('CHECK', 'Alterado', usuarios, index)
                    else:
                        atualizar_linha_planilha('CHECK', 'Análise', usuarios, index)
                else:
                    atualizar_linha_planilha('CHECK', 'Análise', usuarios, index)
            else:
                atualizar_linha_planilha('CHECK', 'Confere', usuarios, index)
        else:
            atualizar_linha_planilha('CHECK', 'Confere', usuarios, index)

        print('---------------------------------------------------------------')
        print(f"Nome: {nome}")
        print('VERIFICADO_novamente')
        print('---------------------------------------------------------------')

    usuarios.to_excel('C:\\Users\\eber_\\Documents\\delveloper\\MIDR\\aquivos\\usuarios_desabilitar_Check.xlsx', index=False)
    time.sleep(2)

    sair(driver)

# Função para acessar a página s2id
def acessar_s2id(driver):
    # Acessar a página de pesquisa
    driver.get('https://s2id.mi.gov.br/paginas/index.xhtml')
    botao_ok = driver.find_element(By.ID, "j_idt35")
    botao_ok.click()

# Função para fazer login
def login(driver):
    usuario_login = driver.find_element(By.ID, 'usuario')
    usuario_login.send_keys('eber.elias@mdr.gov.br')
    senha_login = driver.find_element(By.ID, 'j_idt56')
    senha_login.send_keys('Flasco@4528')
    botao_login = driver.find_element(By.ID, 'btnEnter')
    botao_login.click()

# Função para acessar a página de administração de usuários
def acesso_admin_usuarios(driver):
    admin_usuarios = driver.find_element(By.CSS_SELECTOR, '[title="Administração de Usuários"]')
    admin_usuarios.click()

# Função para carregar os usuários a partir de um arquivo
def base_usuarios(caminho):
    usuarios = pd.read_excel(caminho)
    print(usuarios.EMAIL)
    return usuarios

# Função para pesquisar um usuário
def pesquisar_usuario(nome, driver):
    email = nome
    # Preencher o campo de pesquisa com o nome do usuário
    time.sleep(2)
    campo_pesquisa = driver.find_element(By.ID, 'formAdmCad:busca_palavra_chave')
    campo_pesquisa.clear()
    campo_pesquisa.send_keys(email)
    time.sleep(2)
    # Clicar no botão de pesquisa
    botao_pesquisa = driver.find_element(By.ID, 'formAdmCad:btn_pesquisar')
    botao_pesquisa.click()
    time.sleep(2)
    tabela_linha = driver.find_element(By.CSS_SELECTOR, '[data-ri="0"]')
    tabela_celula = tabela_linha.find_element(By.CSS_SELECTOR, '[role="gridcell"]')
    tabela_celula.click()
    time.sleep(2)

# Função para desabilitar um usuário
def desabilitar_usuarios(driver):
    time.sleep(2)
    desabilitar = driver.find_element(By.ID, 'formAdmCad:j_idt238')
    desabilitar.click()
    time.sleep(2)
    confirmacao = driver.find_element(By.ID, 'formAdmCad:j_idt49')
    confirmacao.click()
    time.sleep(2)

# Função para retornar o texto de um elemento
def retorna_texto(id, driver):
    texto = id
    variavel = driver.find_element(By.ID, texto)
    return_variavel = variavel.text
    return return_variavel

# Função para retornar o atributo de um elemento
def retorna_atributo(id, driver):
    nome_cadastrado = driver.find_element(By.ID, id)
    return_nome_cadastrado = nome_cadastrado.get_attribute("value")
    return return_nome_cadastrado

# Função para atualizar a linha da planilha com um determinado valor
def atualizar_linha_planilha(Nm_coluna_tabela, value, nm_tabela, index):
    nm_tabela.at[index, Nm_coluna_tabela] = value

# Função para sair do sistema
def sair(driver):
    sair = driver.find_element(By.ID, 'sair')
    sair.click()

# Executar a função SARA
print("................ Execultando S.A.R.A. ...................")
SARA()