"""
Running: +3 HP (health points) per min for 180 min ; +1 HP per min for >180 min
    -2 H (hedons) per min if tired & using no stars
    +2 H per min for first 10 min if not tired & -2 H after 10 min if not tired

Carrying Textbooks: +2 HP per min
    +1 H per min for first 20 min if not tired & -1 H after 20 min if not tired

Resting: +0 H & +0 HP per min

Tired: Finished running or carrying textbooks <2 hours before current activity

Star: +3 H per min for <=10 min (if used immediately lasting one activity)
    >3 stars offered in 2 hour span, stars become ineffective

"""

def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    
    # global cur_star (don't need)
    
    global cur_star_activity
    
    # global last_finished (don't need)
    
    global bored_with_stars

    
    # vvv personally added vvv
    
    # Resets to 120 every time a "running" or "textbooks" action is performed
    # Keeps track of how long the person is tired
    global time_left_tired

    # Keeps track of the times a star is offered (using cur_time)
    global star_times
    
    # Keeps track of the difference in time between star times.
    # The sum of two adjacent star times is the time span between the first and
    # third star. (Can check if sum is <120 min. and adjust bored_with_stars)
    global star_times_differences
    

    cur_hedons = 0
    cur_health = 0
    
    # cur_star = None (don't need)
    cur_star_activity = None
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    
    # last_finished = -1000 (don't need)
    
    # personally added
    time_left_tired = 0

    star_times = []
    star_times_differences = []

            
def star_can_be_taken(activity):
    global cur_star_activity

    return activity == cur_star_activity

def apply_possible_star(activity):
    # Checks if star can apply to activity and person isn't bored with stars
    if star_can_be_taken(activity) and bored_with_stars != True:
        return 3
    else:
        return 0
    
def perform_activity(activity, duration):
    global cur_hedons
    global cur_health
    global cur_time
    global last_activity
    global last_activity_duration
    global cur_star_activity
    
    # personally added
    global time_left_tired


    if activity == "running":
        # Health
        
        # Determines how much remaining time running will give 
        # +3 health points per minute
        effective_minutes_health = get_effective_minutes_left_health(activity)
        # Any duration above effective_minutes_health only gives
        # +1 health points per minute
        if effective_minutes_health >= duration:
            cur_health += 3 * duration
        
        else:
            cur_health += 3 * effective_minutes_health
            cur_health += 1 * (duration - effective_minutes_health)
        
        # Hedons
        # Checks if person is tired (time_left_tired > 0)
        if time_left_tired <= 0:
            if duration <= 10:
                cur_hedons += (2 + apply_possible_star(activity)) * duration
            
            # Applies star offer and non-tired, running hedons condition
            # only for first 10 min. 
            else:
                cur_hedons += (2 + apply_possible_star(activity)) * 10
                cur_hedons += (-2) * (duration - 10)
        
        else:
            if duration <= 10:
                cur_hedons += (-2 + apply_possible_star(activity)) * duration
            
            # Applies star offer and tired, running hedons condition
            # only for first 10 min. 
            else:
                cur_hedons += (-2 + apply_possible_star(activity)) * 10
                cur_hedons += (-2) * (duration - 10)
        
        # Resets tired timer to 2 hours (120 min.)
        time_left_tired = 120
        update_last_activity(activity, duration)


    elif activity == "textbooks":
        # Health
        cur_health += 2 * duration
        
        # Hedons
        if time_left_tired <= 0:
            if duration <= 10:
                cur_hedons += (1 + apply_possible_star(activity)) * duration
            
            # Applies star offer and non-tired, textbooks hedons condition
            # only for first 10 min.
            elif duration <= 20:
                cur_hedons += (1 + apply_possible_star(activity)) * 10
                cur_hedons += (1) * (duration-10)
        
            else:
                cur_hedons += (1 + apply_possible_star(activity)) * 10
                cur_hedons += (1) * 10 
                cur_hedons += (-1) * (duration - 20)
        
        else:
            if duration <= 10:
                cur_hedons += (-2 + apply_possible_star(activity)) * duration
            
            # Applies star offer and tired, textbooks hedons condition
            # only for first 10 min.
            else:
                cur_hedons += (-2 + apply_possible_star(activity)) * 10
                cur_hedons += (-2) * (duration - 10)

        # Resets tired timer to 2 hours (120 min.)
        time_left_tired = 120
        last_activity = "textbooks"
        last_activity_duration = duration


    elif activity == "resting":
        time_left_tired -= duration
        last_activity = "resting"
        last_activity_duration = duration

    cur_time += duration
    cur_star_activity = None
        

def get_cur_hedons():
    return cur_hedons
    

def get_cur_health():
    return cur_health
    

def offer_star(activity):
    global cur_star_activity
    global star_times, star_times_differences
    global bored_with_stars
    
    if bored_with_stars != True:
        star_times.append(cur_time)
        if len(star_times) > 1:
            star_times_differences.append(star_times[len(star_times)-1] - \
                                            star_times[len(star_times)-2])
        
            # Checks the time between every two consecutive 
            # star_time_differences
            # (time between every three star)
            for time in range(len(star_times_differences)-1):
                time_between_three_stars = star_times_differences[time] + \
                    star_times_differences[time+1]
            
                if (time_between_three_stars<120):
                    bored_with_stars = True

    if bored_with_stars != True:
        cur_star_activity = activity
        

def most_fun_activity_minute():
    # Determined from hedons conditions and possible star offers
    if time_left_tired <= 0:
        if cur_star_activity == "textbooks":
            return "textbooks"
        else:
            return "running"
    
    else:
        if cur_star_activity == "running":
            return "running"
        
        elif cur_star_activity == "textbooks":
            return "textbooks"
        
        else:
            return "resting"


# personally added
# Specifically made for the running activity
# Keeps track of consecutive running durations in last_activity_duration
def update_last_activity(activity, duration):
    global last_activity, last_activity_duration

    if last_activity == activity:
        last_activity_duration += duration
    else:
        last_activity = activity
        last_activity_duration = duration

################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

# Didn't use
def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass
    

def get_effective_minutes_left_health(activity):

    if activity == "running" and last_activity == "running":
        # Gets cummulative consecutive time running previously
        # and subtracts that from 180 minutes.
        return 180 - last_activity_duration
    else:
        return 180

# Didn't use
def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass
            
# Didn't use
def estimate_health_delta(activity, duration):
    pass
        
################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)    
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
    print("-----------")
    initialize()
    offer_star("running")
    perform_activity("running", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 130)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    print(most_fun_activity_minute())
    perform_activity("resting", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    print(most_fun_activity_minute())
    perform_activity("running", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("running", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("textbooks", 50)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("resting", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("running")
    perform_activity("resting", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    offer_star("running")
    perform_activity("textbooks", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 140)
    print(get_cur_health())
    print(get_cur_hedons())
    
