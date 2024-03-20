def min_meeting_rooms(schedule):
  # Sort meetings based on end time
  schedule.sort(key=lambda x: x[1])

  rooms = [schedule[0]]

  # behaves like a min heap O(n log n)
  def current_room(rooms):
    rooms.sort(key=lambda x: x[1])
    return rooms[0]

  for i in range(1, len(schedule)):
    room = current_room(rooms) # current room that can be alloted now
    time = schedule[i]
    if room[1] <= time[0]:  # If the room is available for the current meeting, update its end time.
      room[1] = time[1]
    else: # If the current meeting overlaps with existing meetings, allocate a new room
      rooms.append(time)

  return len(rooms)

def convert(time_str):
  hour, minute = map(int, time_str.split(':'))
  return hour * 60 + minute

# Test cases
s = ['10:00', '10:30', '11:00', '11:30']
e = ['10:30', '11:00', '11:30', '12:00']
print(min_meeting_rooms([[convert(i), convert(j)] for i, j in zip(s,e)]))  # Output: 2
s = ['9:00', '9:30', '11:00', '12:00']
e = ['10:15', '11:00', '12:15', '13:00']
print(min_meeting_rooms([[convert(i), convert(j)] for i, j in zip(s,e)]))  # Output: 2

s = ['9:00', '9:15', '9:30', '9:00', '10:15']
e = ['10:00', '10:30', '10:45', '9:30', '11:30']
print(min_meeting_rooms([[convert(i), convert(j)] for i, j in zip(s,e)]))  # Output: 3