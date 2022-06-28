def is_leap(year) :
    if (year%400==0) or ((year %4 ==0) and (year % 100 !=0)) :
        m_days[2] = 29
    else :
        m_days[2] = 28

year = int(input("what year did you met? "))
mon  = int(input("what month did you met? "))
day = int(input("what day did you met? "))
cnt = int(input("how many day: "))

days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
m_days= days.copy()
 
t_year = year
t_mon = mon
tmp = cnt

is_leap(year)
m_days[mon] -= (day-1)

while (tmp > m_days[t_mon]):
    tmp -= m_days[t_mon]
    t_mon = t_mon + 1
    if (t_mon==13) :
        t_year = t_year + 1
        t_mon = 1
        is_leap(year)
    
print("the day would be ", t_year,t_mon, tmp)