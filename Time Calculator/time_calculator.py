def add_time(start, duration, day=False):

    start_lst = start.split()
    start_time = start_lst[0].split(":")
    am_or_pm = start_lst[1]
    start_hr = int(start_time[0])
    start_min = int(start_time[1])

    duration_lst = duration.split(":")
    dur_hr = int(duration_lst[0])
    dur_min = int(duration_lst[1])

    days = ['monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']

    if day:
        day = day.lower()

    new_hr = start_hr + dur_hr
    new_min = start_min + dur_min

    if new_min > 60:
        extra_min = new_min % 60
        extra_hr = new_min//60
        new_hr += extra_hr
        new_min = extra_min

    if dur_hr % 24 == 0:
        if (new_hr//12) % 2 == 0:
            if new_hr > 12:
                new_hr = new_hr % 12
                if new_hr == 0:
                    new_hr = 12
            if am_or_pm == "AM":
                new = "AM"
            else:
                new = "PM"
        else:
            if new_hr > 12:
                new_hr = new_hr % 12
                if new_hr == 0:
                    new_hr = 12
            if am_or_pm == "AM":
                new = "PM"
            else:
                new = "AM"
    else:
        if new_hr >= 12:
            if new_hr > 12:
                new_hr = new_hr % 12
                if new_hr == 0:
                    new_hr = 12
            if am_or_pm == "AM":
                new = "PM"
            else:
                new = "AM"
        else:
            if am_or_pm == "AM":
                new = "AM"
            else:
                new = "PM"

    str_new_hr = str(new_hr)
    str_new_min = str(new_min)

    if len(str_new_min) < 2:
        str_new_min = "0" + str_new_min

    new_time = str_new_hr + ":" + str_new_min + " " + new

    # calculating days

    no_days = None
    hr_diff = abs(start_hr - new_hr)
    no_days_dur = dur_hr // 24

    if no_days_dur == 0:
        if am_or_pm == "PM" and new == "AM":
            no_days = 1
        else:
            no_days = 0
    else:
        if am_or_pm == "PM" and new == "AM":
            no_days = no_days_dur + 1
        else:
            no_days = no_days_dur

    # calculations which day of the week
    if day:
        current_day_index = None
        count = 0
        for x in days:
            if day == x:
                current_day_index = count
                break
            else:
                count += 1
        new_day_index = current_day_index + no_days
        if new_day_index > 7:
            new_day_index %= 7
        new_day = days[new_day_index]
        new_day = new_day.capitalize()
        day = day.capitalize()

    if day:
        if no_days > 0:
            if no_days == 1:
                new_time += ", " + new_day + " (next day)"
            else:
                new_time += ", " + new_day + \
                    " (" + str(no_days) + " days later)"
        else:
            new_time += ", " + day
    else:
        if no_days > 0:
            if no_days == 1:
                new_time += " (next day)"
            else:
                new_time += " (" + str(no_days) + " days later)"

    return new_time
