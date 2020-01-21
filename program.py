import datetime

def sanskrit_style(year, month, day, clr=0.25):
    arr = [23, 3, 20, 0, 24, 4, 0, 8, 16, 12, 20, 16]
    out = year
    if (year < 0 or day < 0 or month < 0):
        return -4
    if (month > 12):
        return -3
    else:
        out += arr[month - 1]
    days = [1, -1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
    if (days[month - 1] == 1):
        if (day > 31):
            return -2
    elif (days[month - 1] == 0):
        if (day > 30):
            return -2
    else:
        if (year % 100 == 0):
            if (year % 400 == 0 and day > 29):
                return -2
            elif(day > 28):
                return -2
        elif (year % 4 == 0):
            if (day > 29):
                return -2
        else:
            if (day > 28):
                return -2
    # out += (out / 4) 
    # out = int(out *  1.242199)
    # out += int(out * 0.242199)
    out += int(out * clr)
    out -= 3
    return (out + day - 1) % 7

def test(days, from_date):
    error = []
    for i in range(days):
        if (sanskrit_style(from_date.year, from_date.month, from_date.day) != from_date.weekday()):
            error.append([from_date, sanskrit_style(from_date.year, from_date.month, from_date.day), from_date.weekday()])
            return error
        from_date = datetime.date.fromordinal(from_date.toordinal() + 1)
    return error

if __name__ == "__main__":
    print(test(90000, datetime.date(2019, 12, 1))[0])
