# Scientific Computing with Python Project 2
# Made by Oriana Fawkes '24

# a start time in the 12-hour clock format (ending in AM or PM)
# a duration time that indicates the number of hours and minutes
# (optional) a starting day of the week, case insensitive
def add_time(start, duration, given_day = ""):
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # The function should add the duration time to the start time and return the result.
    augend = start.split(' ')[0]
    suffix = start.split(' ')[-1]
    augend_hour = augend.split(':')[0]
    augend_minute = augend.split(':')[-1]
    addend_hour = duration.split(':')[0]
    addend_minute = duration.split(':')[-1]
    
    # Prepare adjustments for Hour value
    carry_twelve = 12 if suffix == 'PM' else 0
    carry_one = (int(augend_minute) + int(addend_minute))//60
    
    # Update Minute value
    augend_minute = (int(augend_minute) + int(addend_minute))%60
    augend_minute = str(augend_minute) if augend_minute > 9 else '0' + str(augend_minute)
    
    # Count Days passed
    days_passed = (int(augend_hour) + carry_one + carry_twelve + int(addend_hour))//24
    for n, day in enumerate(days_of_the_week):
        if given_day.lower() == day.lower():
            new_day = (n + days_passed)%len(days_of_the_week)
            break
        new_day = -1
    
    # Update Hour value
    augend_hour = (int(augend_hour) + carry_one + carry_twelve + int(addend_hour))%24
    suffix = 'AM' if augend_hour < 12 else 'PM'
    augend_hour = str(augend_hour) if augend_hour <= 12 else str(augend_hour - 12)
    augend_hour = '12' if int(augend_hour) == 0 else augend_hour
    
    # Format Output Message
    message = 'next day' if days_passed == 1 else f'{days_passed} days later'
    new_time = f'{augend_hour}:{augend_minute} {suffix}' if new_day == -1 else f'{augend_hour}:{augend_minute} {suffix}, {days_of_the_week[new_day]}'
    new_time += f' ({message})' if days_passed > 0 else ''
    return new_time

print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))