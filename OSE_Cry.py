from cryptography.fernet import Fernet        
class cryptography_Fernet():

    def get_key(self):
        return Fernet.generate_key()
        
    def transform_bytes(self,str):#key ve şifrelenmiş yapının bayt formatında olması lazım
        return bytes(str,'utf-8')    

    def encrypt_msg(self,msg,key):
        fernet=Fernet(key)
        return fernet.encrypt(msg)

    def decrypt_msg(self,msg,key):
        fernet=Fernet(key)
        return fernet.decrypt(msg)

