#Hola Griff
#Drunk Walker version 1.1
print "Drunk Walker has an equal chance of taking a step forward as he does a step backward"
print "Predict Drunk Walker's position."
print "After the 500th step, you will have the opportunity to change your guess."
print "You have five rounds. May the odds be ever in your favor."
print "This is a fun game."
roundz = 1
points = 0
nada = True
while nada == True: 
    nothing = True
    while (nothing):
        print ""
        print "Round " + str(roundz)
        guess = raw_input("What is your guess after 1000 steps? ")
        try:
            int(guess)
            guess = int(guess)
            nothing = False
        except:
            print "That doesn't work"

    import random
    this = True


    i = 0
    count = 0
    while count < 1001:
        a = random.randint(-1,1)
        i = i + a
        print i
        count += 1
        if count == 500:
            while this == True:
                print "Your old guess was " + str(guess)
                c = raw_input("Do you want to change your guess?(Y/N) ").lower()
                try:
                    if c == "y":
                        hi = True
                        while hi == True:
                            b = raw_input("What is your guess? ")
                            try:
                                guess = int(b)
                                while count < 1001:
                                    a = random.randint(-1,1)
                                    i = i + a
                                    print i
                                    count += 1
                                this = False
                                hi = False
                                                           
                            except:
                                print "That doesn't work"

                    elif c == "n":
                        
                        print "OKAY THEN"
                        print " "
                        print " "
                        print " "
                        print " "
                        print " "
                        count = count + 1
                        this = False
                    else:
                        print "That doesn't work"
                except:
                    print "That doesn't work"

    print " "
    print "Value:"
    print i
    print " "
    print "Your Guess:"
    print guess
    print " "

    if i == guess:
        print "You win!"
        points += 5
    elif (i < 0) and (guess < 0):
        if abs(abs(i) - abs(guess)) == 1:
            print "Close!"
            points += 4
        elif abs(abs(i) - abs(guess)) == 2:
            print "Less close." 
            points += 3
        elif abs(abs(i) - abs(guess)) == 3:
            print "Lesser close." 
            points += 2
        elif abs(abs(i) - abs(guess)) == 4:
            print "Eh." 
            points += 1
        else:
            print "YOU LOST"
    elif (i > 0) and (guess > 0):
        if abs(abs(i) - abs(guess)) == 1:
            print "Close!"
            points += 4
        elif abs(abs(i) - abs(guess)) == 2:
            print "Less close." 
            points += 3
        elif abs(abs(i) - abs(guess)) == 3:
            print "Lesser close." 
            points += 2
        elif abs(abs(i) - abs(guess)) == 4:
            print "Eh." 
            points += 1
        else:
            print "YOU LOST"
    elif (i > 0) and (guess < 0):
        if (i < 5) and (abs(guess) < 5):
            if abs(i + guess) == 1:
                print "Close!"
                points += 4
            elif abs(i + guess) == 2:
                print "Less close." 
                points += 3
            elif abs(i + guess)== 3:
                print "Lesser close." 
                points += 2
            elif abs(i + guess) == 4:
                print "Eh." 
                points += 1
            else:
                print "YOU LOST"
        else:
            print "YOU LOST"
    elif (i < 0) and (guess > 0):
        if (abs(i) < 5) and (guess < 5):
            if abs(i + guess) == 1:
                print "Close!"
                points += 4
            elif abs(i + guess) == 2:
                print "Less close." 
                points += 3
            elif abs(i + guess)== 3:
                print "Lesser close." 
                points += 2
            elif abs(i + guess) == 4:
                print "Eh." 
                points += 1
            else:
                print "YOU LOST"
        else:
            print "YOU LOST"
    print "You have " + str(points) + " points"
    roundz += 1
    if roundz > 5:
        nada = False
    


    
    
