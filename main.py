
import time

from const import MSG_BEM_VINDO, MSG_MENU, MSG_DERROTA, MSG_VITORIA
from roleta import Roleta
from listCircleLinkeded import CircleLinkedList 

roleta_list = CircleLinkedList()
roleta = Roleta(roleta_list)

def menu():

    print(MSG_BEM_VINDO)

    while True:

        print(MSG_MENU)

        try:
            choice = int(input("Escolha uma opção: "))
        except ValueError:
            print("\nOpção inválida. Por favor, escolha um número entre 1 e 3.")
            continue

        if choice < 1 or choice > 3:
            print("\nOpção inválida. Por favor, escolha um número entre 1 e 3.")
            continue
        
        if choice == 1:

            roleta.print_items_roleta()

            user_guess = input("Digite seu palpite: ").strip().upper()

            if not user_guess or user_guess not in roleta_list.getItemsList():
                print("\nPalpite inválido. Por favor, escolha um item existente na roleta.")
                continue

            result = roleta.play()

            time.sleep(2)

            if user_guess == result:
                print(MSG_VITORIA)
            else:
                print(MSG_DERROTA)

            print(f"A roleta parou em: {result}")

        elif choice == 2:
            new_item = input("Digite o novo item para a roleta: ").strip().upper()

            if not new_item:
                print("\nItem inválido. Por favor, digite um item não vazio.")
                continue

            roleta.update(new_item)

        elif choice == 3:
            print("\nObrigado por jogar! Até a próxima!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha um número entre 1 e 3.")
            continue

if __name__ == "__main__":
    menu()