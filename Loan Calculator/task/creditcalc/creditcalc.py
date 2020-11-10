import math
import sys, getopt


# write your code here
def getArgs():
    args = {}
    for param in sys.argv[1:]:
        opt, arg = param.split("=")
        key = "".join(opt.split('-'))
        args[key] = arg

    return args


inputs = getArgs()

payment = int(inputs['payment']) if 'payment' in inputs else 0
principal = int(inputs['principal']) if 'principal' in inputs else 0
periods = int(inputs['periods']) if 'periods' in inputs else 0
interest = float(inputs['interest']) if 'interest' in inputs else 0

nominal = interest / (12 * 100)
int_inputs = [payment, principal, periods, interest]

if len(inputs) != 4 or any(v < 0 for v in int_inputs) or (inputs['type'] != 'diff' and inputs['type'] != 'annuity'):
    print('''python creditcalc.py --type=diff --principal=30000 
    --periods=-14 --interest=10 
    Incorrect parameters''')


elif inputs['type'] == 'diff':
    if 'payment' in inputs:
        print('''python creditcalc.py --type=diff --principal=30000 
            --periods=-14 --interest=10 
            Incorrect parameters''')

    else:
        total = 0
        for i in range(1, periods + 1):
            diff_payment = math.ceil((principal / periods) + nominal * (principal - (principal * (i - 1))/periods))
            total = diff_payment + total
            print(f'Month {i}: payment is {diff_payment}')

        print(f'Overpayment = {total - principal}')

else:
    if 'principal' not in inputs:
        lower_cal = (nominal * (1 + nominal) ** periods) / ((1 + nominal) ** periods - 1)
        principal_loan = math.ceil(payment / lower_cal)

        print(f'Your loan principal = {principal_loan}')
        overpay = (payment * periods) - principal_loan
        print(f'Overpayment = {overpay}')

    elif 'periods' not in inputs:
        num_months = math.ceil(math.log(payment / (payment - nominal * principal), 1 + nominal))
        if num_months < 12:
            print(f'It will take {num_months} months to repay the loan')
        else:
            years = num_months // 12
            months = num_months % 12
            if months == 0:
                print(f'It will take {years}  years to repay this loan!')
            else:
                print(f'It will take {years} years and {months} months to repay this loan!')

        overpayment = (num_months * payment) - principal
        print(f'Overpayment = {overpayment}')

    elif 'payment' not in inputs:
        top_cal = nominal * math.pow(1 + nominal, periods)
        bottom_cal = math.pow(1 + nominal, periods) - 1
        annuity_payment = math.ceil(principal * top_cal / bottom_cal)
        print(f'Your monthly payment = {annuity_payment}')
        over_pay = (annuity_payment * periods) - principal
        print(f'Overpayment = {over_pay}')