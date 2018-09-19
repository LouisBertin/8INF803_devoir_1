def string_between_two_others(start, end, string):
    s = str(string)
    return s[s.find(start)+len(start):s.rfind(end)].strip()
