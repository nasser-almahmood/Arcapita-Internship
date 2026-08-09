import random
lives = 3

life_death = ['life', 'null', 'negative']
l_e_d = ['extra life', 'empty', 'damage']
locations = ['moon river', 'whisper woods', 'stone circle', 'old cabin', 'shadow bridge', 'big tree', 'fog path', 'dark cave', 'bright hill', 'frozen lake', 'quiet meadow', 'old tower', 'deep forest', 'lost path', 'red cliff', 'silver stream', 'hidden hollow', 'mystery chest', 'risky road']



while lives > 0:
    random_life = random.choice(life_death)
    
    random_chest = random.choice(l_e_d)

    random_location = random.choice(locations)

    locations_1 = [x for x in locations if x != random_location]
    random_location_1 = random.choice(locations_1)

    locations_2 = [x for x in locations_1 if x != random_location_1]
    random_location_2 = random.choice(locations_2)

    locations_3 = [x for x in locations_2 if x != random_location_2]
    random_location_3 = random.choice(locations_3)

    

    print('-You now have', lives, 'lives')
    


    # choice
    print('-Choose a route:', random_location, 'OR', random_location_1, 'OR', random_location_2, 'OR', random_location_3)
    random_all = [random_location, random_location_1, random_location_2, random_location_3]
    print('Pick a route: ')
    choice = input('')
    if choice not in random_all:
         continue
    


    
    # mystery chest
    if choice == 'mystery chest':
        if random_chest == 'extra life':
            lives += 5
            print('-CONGRATS, you now have 5 EXTRA lives :)')
        elif random_chest == 'empty':
            print("-WHAT A SHAME, it's EMPTY :|")
        elif random_chest == 'damage':
            lives -= 5
            print('-The chest was a TRAP!!!, you LOST 5 lives :(' )
    


        # risky road
    elif choice == 'risky road':
            if random_life == 'life':
                lives += 10
                print('-OOOLLLAYYYY RISK IT FOR THE BISCUIT, YOU GOT 10 MORE LIVES YAY :)')
            else:
                lives = 0
                print('-OHHHH NOooOOOOooO, you lost all your lives :(')
        


        # the rest of the routes
    elif choice == 'moon river' or 'whisper woods' or 'stone circle' or 'old cabin' or 'shadow bridge' or 'big tree' or 'fog path'or 'dark cave' or 'bright hill' or 'frozen lake' or 'quiet meadow' or 'old tower' or 'deep forest' or 'lost path' or 'red cliff' or 'silver stream' or 'hidden hollow':
            if random_life == 'life':
                lives += 1
                print('-CONGRATS, you now have an EXTRA  1 life :)')
            elif random_life == 'null':
                print("-Nothing happened :|")
            elif random_life == 'negative':
                lives -= 1
                print('-The killer was waiting for you there and ambushed you , you LOST 1 life :(' )
        





    # play again?
    if lives <= 0:
            print('-Would you like to play again? YES or NO:')
            play_again = input('').lower()
            if play_again == 'yes':
                lives = 3
                continue
            elif play_again == 'no':
                break            