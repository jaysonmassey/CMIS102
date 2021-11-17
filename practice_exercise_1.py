#  Practice Exercise 1
#  compute and display the average speed of a race car given the statistics for a particular race.

#  constant variables
track_length = 1  # in miles

# declare user variables
start_time = 0
finish_time = 0
elapsed_time = 0

# - start time
# - finish time
# - laps

# results
# - elapsed time = finish time - start time (in minutes)
# - average speed =  (laps x track length) / (elapsed time * 60)
# - speed is in miles per hour.  get length in miles and turn time in minutes into hours

and = 0
start_time = input('Enter the start time: ')
finish_time = input('Enter the finish time: ')
num_laps = input('Enter the number of laps: ')

# TODO: add logic to prevent the finish time to be less than the start time
elapsed_time = int(finish_time) - int(start_time)
total_miles = int(num_laps) * track_length
car_speed = total_miles / (elapsed_time / 60)
print("Elapsed time: ", elapsed_time)
print("Miles traveled: ", total_miles)
print("Average speed: ", car_speed, " miles per hour")