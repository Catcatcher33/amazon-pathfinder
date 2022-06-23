from cmath import phase
from tasks import phase_1, phase_2, bonus




if __name__ == '__main__':
    import sys
    # need to create a more interfaceable thing
    actions: dict = {
        phase_1 : "phase 1", 
        phase_2 : "phase 2", 
        bonus : "bonus"
    }# forgot the other way to display dictionaries

    for action, title in actions.items():
        print(f"Executing {title}. Proceed? (y/n)")
        if input() == 'y':
            action()
        else:
            break


    for action in actions:
        print('Starting with phase 1. Proceed? (y/n)')
        action()
    
   # while input() != 'n':
      #  print('Starting with phase 1. Proceed? (y/n)')
     #   if input() == 'y':
    #        phase_1()
   #     print('Starting phase 2. Proceed? (y/n)')
  #      if input() == 'y':
 #           phase_2()
#        print('Starting bonus. Proceed? (y/n)')
    #    if input() == 'y':
     #       bonus()
    #    sys.exit()

