import ftplib
session=ftplib.FTP('127.0.0.1','kw4h','ydy888')
myfile=open("d:\\tmp\\pytest\\file1.txt","rb")
session.storbinary("Store toto.txt",myfile)
myfile.close()
session.quit()
