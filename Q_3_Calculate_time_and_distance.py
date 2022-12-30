'''

3. Provide a program to calculate the time and distance based on 
below problem.
• We have a 100-meter rod.
• At both ends, 1-1 cockroach is place.
• The left cockroach moves at 1 meter per second forward, and every 10 seconds moves 2 
meters backward.
• The right cockroach moves at 2 meters per second forward, and every 5 seconds moves 1 
meter backward.
• When both cockroaches meet, we have to calculate the time and distance. Calculate the total
time to complete the 100 meter rod.

'''







def calculate_time_and_distance(distance):
  time = 0
  left_position = 0
  right_position = 0

  while left_position < distance and right_position < distance:
    time += 1
    left_position += 1
    right_position += 2

    if time % 10 == 0:
      left_position -= 2

    if time % 5 == 0:
      right_position -= 1

  return time, left_position

distance = 100
time, position = calculate_time_and_distance(distance)
print(f"Time: {time} seconds")
print(f"Distance: {position} meters")
