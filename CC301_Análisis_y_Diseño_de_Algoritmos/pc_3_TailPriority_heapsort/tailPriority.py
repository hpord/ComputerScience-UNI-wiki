import time 
import heapq as hq 
from colorama import Fore
from colorama import Style


  
# jobs to be executed 
jobs = [(3, 'geolocation'), (5, 'music'), (1, 'check security system'), (4, 'fans'), (1, 'start driving')] 
  
# interrupts 
interrupts = [(4, 'battery'), (1, 'pedestrian (stop)'), (2, 'playing horn'), (13, 'check tires')] 
  
j = 0
  
# Arranging jobs in heap 
hq.heapify(jobs) 
  

print("\n------------------------------------------------------------", end="")
print("------------------------------------------------------------")
print("------------------------------------------------------------", end="")
print("------------------------------------------------------------", end="")
print("\n\t\t\t\t\t\t    SELF-DRIVING SYSTEM\n")
print(f"\t\t\t\t\t  {Fore.MAGENTA}Subject: Priority tail using heaps{Style.RESET_ALL}\n")
print(f"\t\t\t\t\t  {Fore.MAGENTA}Author: Sanchez Sauñe, Cristhian Wiki{Style.RESET_ALL}\n")
print("------------------------------------------------------------", end="")
print("------------------------------------------------------------")
print("------------------------------------------------------------", end="")
print("------------------------------------------------------------", end="")
input("\n\nPress an key to initialize..")
print("\n\nShowing initial priority queue..")
print("\n", jobs, "\n") 
print("------------------------------------------------------------", end="")
print("------------------------------------------------------------")
input("\n\nPress an key to show task flow..")
print()
# scheduling the tasks 
while len(jobs) != 0: 
  
    # printing execution log 
    processCurrent = "'{}' with priority {} in progress".format(jobs[0][1], jobs[0][0])
    processCurrent = "\t{}{}".format(Fore.GREEN, processCurrent)
    print(processCurrent, end="") 
  
    # servicing the tasks
    for _ in range(0, 5):
        print(".", end="") 
        time.sleep(0.5) 
    print(f'{Style.RESET_ALL}')   
  
    # pop the job that completed 
    hq.heappop(jobs) 
  
    # adding interrupts 
    if j < len(interrupts): 
  
        hq.heappush(jobs, interrupts[j]) 
        print(f'{Fore.RED}')
        print("\tNew interrupt arrived!!", interrupts[j], f'{Style.RESET_ALL}')
        j = j+1
  
    # job queue after arrival of interrupt 
    print(f'{Fore.YELLOW}')
    time.sleep(0.2) 
    print("\tJob queue currently :", jobs) 
    print(f'{Style.RESET_ALL}')
    print("------------------------------------------------------------", end="")
    print("------------------------------------------------------------", end="")
    print("\n") 
  
print(f"\t{Fore.BLUE}All interrupts and jobs completed!{Style.RESET_ALL}\n\n")
