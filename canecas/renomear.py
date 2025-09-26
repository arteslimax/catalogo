import os
import re

def renomear_arquivos_sem_espaco(pasta):
    padrao = re.compile(r"(\d+)\s+(MOCKUPS)(\s*)(.*)", re.IGNORECASE)

    for nome_arquivo in os.listdir(pasta):
        caminho_antigo = os.path.join(pasta, nome_arquivo)

        if not os.path.isfile(caminho_antigo):
            continue

        correspondencia = padrao.match(nome_arquivo)

        if correspondencia:
            numero = correspondencia.group(1)
            prefixo = correspondencia.group(2)
            resto = correspondencia.group(4).lstrip()  # remove espaços extras à esquerda do resto

            # Remove espaço entre número e MOCKUPS e mantém espaço após MOCKUPS e número + resto
            nome_novo = f"{numero}{prefixo} {resto}"

            caminho_novo = os.path.join(pasta, nome_novo)
            print(f"Renomeando: '{nome_arquivo}' => '{nome_novo}'")
            os.rename(caminho_antigo, caminho_novo)

if __name__ == "__main__":
    pasta_trabalho = "./"
    renomear_arquivos_sem_espaco(pasta_trabalho)
