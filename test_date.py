from dateutil.parser import parse

start_date = parse('2017-04-30')
end_date = parse('2018-12-10')
a=20170825
b=str(a)
c=parse(b)

print(c.date())

if start_date < c < end_date:
    print('在')
else:
    print('不在')
