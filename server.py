import Pyro4
import ftplib

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, filename):
        HOSTNAME = "localhost"
        USERNAME = "samuel"
        PASSWORD = "samuel123"
        ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD) 
        ftp_server.encoding = "utf-8"
        
        with open(filename, "rb") as file: 
    
            ftp_server.storbinary(f"STOR {filename}", file)

        return  "Nome do arquivo: ", filename, "Diretório: ", ftp_server.dir(), ftp_server.quit()

def startServer():
    server = Server()
    daemon = Pyro4.Daemon()    #Espera e trata as requisições         
    ns = Pyro4.locateNS()
    uri = daemon.register(server)  
    ns.register("server", uri)   
    print("Ready. Object uri =", uri)
    daemon.requestLoop()                   

if __name__ == "__main__":
    startServer()