import random

print("=== Treasure Hunt: Deeper Secrets ===")
player = input("Your name, brave hunter: ").strip()
if not player:
    player = "Hunter"

hp = 100
gold = 0
luck = random.randint(1, 6)  
has_rope = False
has_torch = False
map_piece = False

print(f"Welcome, {player}. Your luck is {luck} (1-6). Find the treasure!")

# initial random discovery 
if random.random() < 0.45:
    found = random.choice(["rope", "torch", "small coin"])
    if found == "rope":
        has_rope = True
        print("On the path you find a sturdy rope coiled beside a stump.")
    elif found == "torch":
        has_torch = True
        print("A discarded torch lies half-buried; it could be useful in darkness.")
    else:
        c = random.randint(3, 12)
        gold += c
        print(f"You spot a glint and pick up {c} gold coins.")
else:
    print("The path is quiet. Nothing to take with you... yet.")

print("\nYou reach the fork in the road.")
choice1 = input("Do you go 'left' (cave) or 'right' (river)? ").strip().lower()

if choice1 == "left":
    print("You head into a shadowed cave. Stalactites drip above.")
    # nested choice with torch/stealth
    if has_torch:
        c2 = input("You have a torch. Do you 'light' it or 'sneak' without lighting? (light/sneak): ").strip().lower()
    else:
        c2 = input("Do you 'light' (you don't have torch) or 'sneak'? (light/sneak): ").strip().lower()

    if c2 == "light":
        if has_torch:
            print("The torch flares, revealing glittering veins in the rock and a locked chest.")
        else:
            # attempting to light without torch: risk
            print("You attempt to create a spark with flint and stick. It takes effort.")
            if luck >= 4:
                print("You manage to produce a flame and see a locked chest ahead.")
                has_torch = True
            else:
                print("Your attempt fails and you startle a cave-dweller. It bites you before fleeing.")
                hp -= 18

        # encounter chest with lock puzzle
        print("The chest is secured with a strange mechanism: a three-peg code (1-3 each).")
        print("You may try to guess the code (three numbers 1-3) or attempt to pick the lock.")
        attempt = input("Try 'guess' or 'pick': ").strip().lower()
        if attempt == "guess":
            code = [random.randint(1, 3) for _ in range(3)]
            guess = input("Enter three digits without spaces (e.g. 123): ").strip()
            if guess == ''.join(str(x) for x in code):
                reward = random.randint(40, 90)
                gold += reward
                print(f"Correct! The chest yields {reward} gold and a shimmering gem. You win! (ending: chest master)")
            else:
                print("Wrong code! A dart shoots from the lid and grazes you.")
                hp -= random.randint(8, 16)
                # secondary chance to brute force with map
                if map_piece:
                    print("Using a map piece, you deduce the code's pattern and recover the chest partially.")
                    gold += 20
                else:
                    print("You leave the chest, wounded but alive.")

        elif attempt == "pick":
            # pick success depends on luck
            if luck + random.randint(0, 3) >= 6:
                loot = random.randint(30, 70)
                gold += loot
                print(f"You expertly pick the lock and claim {loot} gold (ending: thief's pride).")
            else:
                print("Your tools slip; a trap triggers and you are hit by a falling rock.")
                hp -= random.randint(10, 22)
        else:
            print("Hesitation costs you; you back out of the chest area.")

    elif c2 == "sneak":
        # chance to bypass traps; depends on luck
        if luck >= 3:
            print("You move quietly and find a hidden crevice with an old map piece inside.")
            map_piece = True
            gold += random.randint(5, 15)
        else:
            print("You stumble on loose gravel and trigger a noise; a guardian bat swarm arrives.")
            hp -= random.randint(6, 14)
            if hp < 1:
                print("You are overwhelmed by injuries in the cave.")

    else:
        print("Indecision in the cave costs time; a cave-in blocks your path. You return to the fork. Game ends here.")

elif choice1 == "right":
    print("You approach a wide, swift river. The current looks strong.")
    c2 = input("Do you 'swim' across, 'build' a raft, or 'search' the bank? (swim/build/search): ").strip().lower()
    if c2 == "search":
        print("You search the bank. You find footprints and a partly-buried chest nailed shut.")
        if random.random() < 0.45:
            print("Inside the chest is a rope and a small stash of coins.")
            gold += random.randint(10, 25)
            has_rope = True
        else:
            print("The chest is empty but you notice a faint trail leading downstream.")

    elif c2 == "build":
        if has_rope:
            print("Using rope and driftwood you fashion a sturdy raft and cross safely.")
            gold += random.randint(10, 30)
            print("Across the river you find an abandoned campsite and a useful map fragment.")
            map_piece = True
        else:
            print("Without rope building a reliable raft is risky.")
            if luck >= 4:
                print("You improvise a raft and it holds. You cross safely but lose some gear.")
                gold += random.randint(5, 20)
            else:
                print("The makeshift raft fails; you are thrown into the water and struggle to shore.")
                hp -= random.randint(10, 20)

    elif c2 == "swim":
        # swimming risk
        if luck >= 5:
            print("You swim skillfully and avoid hidden currents, reaching the far bank.")
            gold += random.randint(5, 15)
        else:
            print("A current drags you; you fight but lose valuables and take damage.")
            gold = max(0, gold - random.randint(5, 15))
            hp -= random.randint(6, 18)

    else:
        print("Unable to decide, the sun sets and you make camp by the river.")

else:
    print("You dawdle at the fork and a traveling merchant passes by offering clues for a price.")
    trade = input("Do you 'buy' a clue for 10 gold or 'ignore'? (buy/ignore): ").strip().lower()
    if trade == "buy" and gold >= 10:
        gold -= 10
        print("The merchant points you to a hidden hollow beneath the old oak (a third path opens).")
        hidden = input("Do you investigate the hidden hollow? (yes/no): ").strip().lower()
        if hidden == "yes":
            print("Inside you find the map piece that will help with chests.")
            map_piece = True
    else:
        print("You continue with your modest gear.")

# After primary choices, offer a final crossroad for finishing the hunt
print('\nAs dusk falls, you approach the riverbank where an old bridge and a narrow trail converge.')
final = input("Do you take the 'bridge' or the 'trail'? ").strip().lower()

if final == "bridge":
    if has_rope and luck >= 3:
        print("On the bridge you rappel down to a hidden grotto using your rope and claim the ultimate treasure.")
        gold += 120
        print("Ending: Master Explorer — you found the grotto treasure!")
    else:
        print("The bridge creaks; midway it collapses but you manage to grab a ledge.")
        if luck >= 4:
            print("You pull yourself up and discover a pouch of rare coins tucked under a rock.")
            gold += 45
        else:
            print("You fall and injure yourself, losing the chance to find the main treasure.")
            hp -= 25

elif final == "trail":
    if map_piece:
        print("Using the map piece you follow glyphs to a buried chest. It opens to reveal ancient coins and relics.")
        gold += 90
        print("Ending: Cartographer's Fortune — maps win the day.")
    else:
        print("The trail leads to a rickety hilltop with nothing but an old coin. Still, it's a find.")
        gold += 10

else:
    print("You sit and reflect; the journey itself was the treasure. You record your tale for others.")

# Conclude with status and grading
print("\n--- Adventure Summary ---")
print(f"Name: {player}")
print(f"HP: {hp}    Gold: {gold}")
print(f"Inventory: rope={has_rope} torch={has_torch} map_piece={map_piece}")

score = gold + (hp // 2) + (10 if map_piece else 0) + (15 if has_rope else 0)
if score >= 180:
    rank = "Legendary Hunter"
elif score >= 120:
    rank = "Seasoned Explorer"
elif score >= 60:
    rank = "Adept Adventurer"
else:
    rank = "Novice Seeker"

print(f"Score: {score}  Rank: {rank}")
print("Thanks for playing the upgraded Treasure Hunt.")