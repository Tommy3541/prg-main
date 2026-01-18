import datetime as dt

cas = dt.datetime.now()

print(cas)

print(cas.month)
print(cas.day)
print(cas.year)
print(cas.second)

print(f"ted je {cas}")

minus10 = cas - dt.timedelta(minutes=10)
print(f"momentalni cas minus 10 minut je {minus10}")

# vlastni cas

vlastni_cas = dt.datetime(2025, 11, 18, 15, 5) - cas

print(f"cas do prestavky: {vlastni_cas}")

