#!/usr/bin/env python3

import timeit
import copy
import time
from datetime import datetime
from time import perf_counter
import random
from collections import deque #import queue
from pref import male_participants, female_participants


male_pref = dict()
female_pref = dict()
#single_list = queue.Queue()
#regular queue deosnt have some functions like append...dequeue does
single_list = deque()



def set_preferences():#sets pref of male and female participants..
    
    for male in male_participants:
        temp = female_participants.copy()
        random.shuffle(temp) #randomizing pref_lists
        male_pref[male] = [temp, 0, None] # sets male pref by importing temp(copy)
                                              # of female_participants
        single_list.append(male)

    for female in female_participants:
        temp = male_participants.copy()
        random.shuffle(temp) #randomizing pref_lists
        female_pref[female] = [temp, False, None] #False if engaged or not, will check later


def print_preferences(preferences):
    for key in preferences:
        if(len(key) > 3): #examples include Abby:
                                           #Ed:
                                           # Will format to Abby:  
                                           #                Edd :
            print(key, end=": ")
            print((preferences[key][0]))
        elif(len(key) == 2):
            print(key, end="  : ")
            print((preferences[key][0]))
        else:

            print(key, end=" : ") #matching moodle format, aligning ':'
            print((preferences[key][0]))
 
start_time = datetime.now() # starts the timer
t1_start = perf_counter() # starts the timer
t0 = time.time()

def gale_shapley():
    while(len(single_list) != 0): # while single men exists...
        man = single_list.popleft() #gets first most single man
        cur_state = male_pref.get(man)[1] #gets "man" preference at index 1(rank 1) (current state)
        woman = male_pref.get(man)[0][cur_state]# gets woman preference similarly to cur_state but holds a val
        if female_pref[woman][1] is False:               #
            male_pref[man][2] = woman                    #
            female_pref[woman][2] = man                  # Checks if preferences match up, does
            female_pref[woman][1] = True                 # some swapping then engages

            print('{0} engaged to {1}'.format(man, woman))      

            cur_state+=1
            male_pref.get(man)[1] = cur_state
        else: #if not matched 
            partner_temp = female_pref[woman][2] #sets temp pref. partner to woman
            if female_pref[woman][0].index(man) < female_pref[woman][0].index(partner_temp): #if cur man ranks lower than other man....

                print('{0} dumped {1}'.format(woman, partner_temp)) #dumps! 

                male_pref[partner_temp][2] = None
                single_list.appendleft(partner_temp)
                male_pref[man][2] = woman    #repeats functionality in lines 57-61
                female_pref[woman][2] = man

                print('{0} engaged to {1}'.format(man, woman))

                cur_state+=1
                male_pref.get(man)[1] = cur_state #sets
            else:
                print('{0} rejected {1}'.format(woman, man))

                cur_state+=1
                male_pref.get(man)[1] = cur_state
                single_list.appendleft(man)


t1_stop = perf_counter()

def main():

    print("Participants:")
    print(*male_participants) #matching moodle format
    print(*female_participants, "\n")
    set_preferences()
    print("Preferences:")
    print_preferences(male_pref)
    print_preferences(female_pref)
    gale_shapley()


if __name__ == "__main__":
    main()
