import os
import re

while True:
    caminho = input("Digite o caminho da pasta:")

    if os.path.exists(caminho):
        formatacao = os.path.normpath(caminho).replace("\\" , "\\\\")
        print("Caminho Válido! Iniciando Automação...")
    
        def limpar():
            for nome_arquivo in os.listdir(caminho):
                if nome_arquivo.endswith(".cbz"):
                    new_name = re.sub(r"_[a-z0-9]{6,8}(?=\.cbz)", "" , nome_arquivo)
                
                    if new_name != nome_arquivo:
                        old_path = os.path.join(caminho, nome_arquivo)
                        new_path = os.path.join(caminho, new_name)
                    
                        try:
                            os.rename(old_path, new_path)
                            print(f"Renomeado!{nome_arquivo} -> {new_name}")
                        except:
                            print(f"Erro: {new_name} já existe. Pular arquivo...")
                        
        if __name__ == "__main__":
            limpar()

    else:
        print("O caminho inserido é inválido. Tente novamente...")
        
    print("1 - Executar novamente")
    print("2 - Encerrar")
    
    resposta = int(input(""))
    
    if resposta == 1:
        continue
    if resposta == 2:
        break


