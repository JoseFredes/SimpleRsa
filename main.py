p = 0
q = 0
posible_results = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!, "
public_key = 0
secret_key = 0
plain_text = ""
encrypted_text = ""
word = ""
key_word = ""
key_number = 1

while True:
    p, q = input(" Ingresar P y Q  (Ej: 1 2)\n").split(" ")
    p = int(p)
    q = int(q)
    n = p * q
    z = (p-1) * (q-1)

    for i in range(1, 10000):
        if 0 != z % i:
            public_key = round(i)
            break

    for j in range(0, 10000):
        d = 1 + (j * z)
        d2 = d / public_key
        if 0 == d % public_key:
            secret_key = round(d2)
            break
          
    while True:
        print("Valor de P ",p)
        print("Valor de Q ",q)
        print("Modulo ", n)
        print("Public key ",public_key)
        print("Secret key ",secret_key)
        word = input("Para seguir haciendo pruebas Ingresa los dos valores =>")
