lfc = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_counter = 0
sword_counter = 0
shield_counter = 0
armor_counter = 0
output = ""

for fight in range(1, lfc + 1):
    if fight % 2 == 0:
        helmet_counter += 1
    if fight % 3 == 0:
        sword_counter += 1
    if fight % 6 == 0:
        shield_counter += 1
    if fight % 12 == 0:
        armor_counter += 1

    helmet_loss = helmet_price * helmet_counter
    sword_loss = sword_price * sword_counter
    shield_loss = shield_price * shield_counter
    armor_loss = armor_price * armor_counter
    expenses = helmet_loss + armor_loss + shield_loss + sword_loss
    output = f"Gladiator expenses: {expenses:.2f} aureus"
print(output)
