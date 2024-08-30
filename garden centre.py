#g.courtney
#5/9/2023
#Garden Center

print("2 - Garden Center Program")
print()

tulips_spend = int(input('How much did you spend on tulips?'))
crocuses_spend = int(input("How much did you spend on crocuses?"))
snowdrops_spend = int(input("How much did you spend on snowdrops?"))
daffodils_spend = int(input("How much did you spend on daffodils?"))

total_spend = tulips_spend + crocuses_spend + snowdrops_spend + daffodils_spend

print()
print("You spent £", total_spend, "that is far to much to spend on flowers")

if total_spend > 30 :
    print("have a free bulb loser")


