def min_rooms(schedule):
  schedule.sort()
  # print(*schedule)

  rooms = [schedule[0]]

  # behaves like a min heap O(n log n)
  def current_room(rooms):
    # Sort timings based on end time
    rooms.sort(key=lambda x: x[1])
    return rooms[0]

  for i in range(1, len(schedule)):
    # print(*rooms)
    room = current_room(rooms) # current room that can be alloted now
    time = schedule[i]
    if room[1] <= time[0]:  # If the room is available for the current meeting, update its end time.
      room[1] = time[1]
    else: # If the current meeting overlaps with existing meetings, allocate a new room
      rooms.append(time)
  # print(*rooms)
  return len(rooms)

def convert(time_str):
  hour, minute = map(int, time_str.split(':'))
  return hour * 60 + minute

def testcases():
  tc = {
    "1": {
      "start": ['10:00', '10:30', '11:00', '11:30'],
      "end": ['10:30', '11:00', '11:30', '12:00']
    },
    "2": {
      "start": ['9:00', '9:30', '11:00', '12:00'],
      "end": ['10:15', '11:00', '12:15', '13:00']
    },
    "3": {
      "start": ['9:00', '9:15', '9:30', '9:00', '10:15'],
      "end": ['10:00', '10:30', '10:45', '9:30', '11:30']
    }
  }
  inp = input("Choose Testcase[1/2/3]: ")
  print(f"Testcase #{inp}:\Start: {tc[inp]['start']}\End: {tc[inp]['end']}")
  schedule = [[convert(i), convert(j)] for i,j in zip(tc[inp]["start"], tc[inp]["end"])]
  print(min_rooms(schedule))

if __name__ == "__main__":
  testcases()
  # start = list(map(int, input().strip().split()))
  # end = list(map(int, input().strip().split()))
  # schedule = [[convert(i), convert(j)] for i,j in zip(start, end)]
  # print(min_rooms(schedule))
  # print()