"""
Faça um programa que leia um nome de usuário e a sua senha e mostre uma 
mensagem de erro caso a senha seja igual ao nome do usuário.
"""

from getpass import getpass

class PotentialVulnerability(Exception): pass


def validate_password():
    print("\nRetorna um erro caso usuário e senha sejam iguais\n")

    try:
        _user = input("Inserir o usuário: ")
        _pass = getpass("Inserir a senha: ")
        if _user == _pass:
            raise PotentialVulnerability()
    except KeyboardInterrupt:
        print("\nOperação abortada pelo usuário\n")
        return
    except PotentialVulnerability:
        print("\nPotencial vulnerabilidade (senha igual ao usuário)\n")
    

if __name__ == "__main__":
    validate_password()