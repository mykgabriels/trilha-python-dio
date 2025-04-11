from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando a Tv...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a Tv...")
        print("Desligada!")


class ControleAr(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar...")
        print("Ligado!")

    def desligar(self):
        print("Deligando o Ar...")
        print("Desligado!")


controle = ControleTv()
controle.ligar()
controle.desligar()

ar = ControleAr()
ar.ligar()
ar.desligar()
