def add_time(start, duration, day_of_week=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    start_hours = int(start.split(":")[0])
    start_minutes = int(start.split(":")[1].split(" ")[0])
    start_period = start.split(" ")[1]
    duration_hours = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])

    if start_period == "PM":
        start_hours += 12

    end_hours = start_hours + duration_hours
    end_minutes = start_minutes + duration_minutes

    if end_minutes >= 60:
        end_hours += end_minutes // 60
        end_minutes = end_minutes % 60

    days_passed = end_hours // 24
    end_hours = end_hours % 24

    if end_hours > 12:
        end_hours -= 12
        end_period = "PM"
    elif end_hours == 12:
        end_period = "PM"
    elif end_hours == 0:
        end_hours = 12
        end_period = "AM"
    else:
        end_period = "AM"

    new_time = f"{end_hours}:{end_minutes:02d} {end_period}"

    if day_of_week:
        day_index = days_of_week.index(day_of_week.capitalize()) + days_passed
        new_day = days_of_week[day_index % 7]
        new_time += f", {new_day}"

    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time

# Example usage:
print(add_time('11:30 AM', '2:32', 'Monday')) 
print(add_time('3:00 PM', '3:10'))