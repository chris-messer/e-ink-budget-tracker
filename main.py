from services.print_budget import refresh_budget

monthly_budget = 5000

while True:
    refresh_budget(monthly_budget, _debug=True)
    time.sleep(10000)
    print('pause')