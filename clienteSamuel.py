import Pyro4
import ftplib

HOSTNAME = "localhost"
USERNAME = "samuel"
PASSWORD = "samuel123"
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
ftp_server.encoding = "utf-8"

opcao = 0
while opcao != 4:
    print("---" * 20)
    print ("""
    1.Listar arquivos
    2.Baixar arquivo
    3.Enviar arquivo
    4.Exit/Quit
    """)
    
    opcao = int(input("O que você quer fazer? "))
      
    if opcao == 1:
      print("\n" + '\033[32m' + 'ARQUIVOS DISPONÍVEIS NO SERVIDOR: ' + '\033[0;0m' + '\033[42m' + HOSTNAME + '\033[0;0m'+ "\n") 
      ftp_server.dir() 
      
    elif opcao == 2:
      filename = input("\n" + "Qual o nome do aquivo desejado? " )
      server = Pyro4.Proxy("PYRONAME:server")
      print(server.welcomeMessage(filename))
      with open(filename, "wb") as file:
        ftp_server.retrbinary(f"RETR {filename}", file.write)
        file = open(filename, "r")
        print("\n" + "Conteúdo do arquivo baixado: ", file.read())
        
    elif opcao == 3:
      filename = input("\n" + "Qual o nome do aquivo a ser enviado? ").strip()
      with open(filename, "rb") as file: 
        ftp_server.storbinary(f"STOR {filename}", file)
      
      print("Arquivo enviado ao servidor: " + filename)
      
    elif opcao == 4:
        ftp_server.quit()
        
    else:
        print("\n" + '\033[31m' + "Opção inválida. Tente novamente!" + '\033[0;0m' )
        print("\n" + '=-=' * 20)
        
      
ftp_server.quit()


