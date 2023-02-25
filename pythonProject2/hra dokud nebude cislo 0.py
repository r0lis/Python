tokens = 15

while tokens > 0:
    print(f"Matches remaining: {tokens}")

    # Player's turn
    while True:
        tokens_to_take = int(input("How many matches do you want to remove? "))
        if 1 <= tokens_to_take <= 3 and tokens_to_take <= tokens:
            break
        else:
            print("Invalid number of matches.")
    tokens = tokens - tokens_to_take
    if tokens == 0:
        print("Computer wins.")
        break

    # Computer's turn
    tokens_to_take = (tokens - 1) % 4
    if tokens_to_take == 0:
        tokens_to_take = 1
    tokens = tokens - tokens_to_take
    print(f"Computer removed {tokens_to_take} match(es).")
    if tokens == 0:
        print("Player wins.")
        break