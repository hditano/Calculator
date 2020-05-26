# Fields

names = ['john ClEEse', 'Eric IDLE', 'michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
names.extend(names1)
count = 0
countMorePeople = 0

# MainLoop()

print("Welcome to the Party, let me check who's invited")
while count < len(names):
    for i in names:
        print(f"{i.lower().capitalize()}! You are invited to the party on saturday")
        count += 1
        print(f"We have already invited {count} person at the party!!")
    print("Want to invite someone else? (yes) or (no): ")
    moreInvites = input().lower()
    if moreInvites == 'yes':
        morePeople = int(input("How many people you want to add to the Party: "))
        while morePeople > countMorePeople:
            countMorePeople += 1
            names.append(input("Please introduce the names: "))
        else:
            break
    else:
        continue
print(f"Your final list is a total of {count} people")
print(' ,'.join(names).title())
