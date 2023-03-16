def find_day(day, n):
  days = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
    'Sunday'
  ]
  day = day.capitalize()
  for i, yawm in enumerate(days):
    if yawm == day:
      x = i + n
      while x >= 7:
        x = x - 7 * 2
      return days[x]


def add_time(time, duration, day=False):
  parts = time.split()
  start = parts[0]
  am_or_pm = parts[1]
  n = 0

  start_hour = str(start).split(':')[0]
  start_min = str(start).split(':')[1]

  duration_hour = str(duration).split(':')[0]
  duration_min = str(duration).split(':')[1]

  new_time_hours = int(start_hour) + int(duration_hour)
  new_time_min = int(start_min) + int(duration_min)

  while new_time_min > 60:
    new_time_min -= 60
    new_time_hours += 1
  if len(str(new_time_min)) == 1:
    new_time_min = f'0{new_time_min}'
  else:
    pass

  while new_time_hours > 24:
    new_time_hours -= 24
    n += 1

  if new_time_hours >= 12:
    if am_or_pm == 'AM':
      am_or_pm = 'PM'
      if new_time_hours != 12:
        new_time_hours -= 12
    else:
      am_or_pm = 'AM'
      if new_time_hours != 12:
        new_time_hours -= 12
      n += 1
  else:
    pass

  #if len(str(new_time_hours)) == 1:
  #   new_time_hours = f'0{new_time_hours}'
  #else: pass

  if day != False:
    new_day = find_day(day, n)
    if n > 1:
      x = f'({n} days later)'
    elif n == 1:
      x = '(next day)'
    else:
      x = ''
    result = f'{new_time_hours}:{new_time_min} {am_or_pm}, {new_day} {x}'

  else:
    if n > 1:
      x = f'({n} days later)'
    elif n == 1:
      x = '(next day)'
    else:
      x = ''
    result = f'{new_time_hours}:{new_time_min} {am_or_pm} {x}'

  while result[-1] == ' ' or result[-1] == ',':
    result = result[:-1]
  return result
