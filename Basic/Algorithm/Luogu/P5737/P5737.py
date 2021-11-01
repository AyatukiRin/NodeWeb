import calendar
startYear, endYear = map(int, input().split())
lt = list(filter((lambda year: calendar.isleap(year)), range(startYear, endYear + 1)))
print(len(lt))
for year in lt:
    print(year, end=' ')