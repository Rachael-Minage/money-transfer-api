import math

def calculate_loan_repayment(loan_amount, loan_term, annual_interest_rate, repayment_frequency):
    frequencies = {
        'monthly': 12,
        'bi-monthly': 6,
        'weekly': 52
    }
    payments_per_year = frequencies.get(repayment_frequency, 12)
    period_interest_rate = annual_interest_rate / 100 / payments_per_year
    num_payments = loan_term * payments_per_year // 12
    
    if period_interest_rate > 0:
        period_payment = loan_amount * period_interest_rate / (1 - (1 + period_interest_rate) ** -num_payments)
    else:
        period_payment = loan_amount / num_payments
    
    remaining_balance = loan_amount
    total_interest = 0
    repayment_schedule = []
    
    for i in range(num_payments):
        interest_payment = remaining_balance * period_interest_rate
        principal_payment = period_payment - interest_payment
        remaining_balance -= principal_payment
        total_interest += interest_payment
        
        repayment_schedule.append({
            'Payment Number': i + 1,
            'Interest Payment': round(interest_payment, 2),
            'Principal Payment': round(principal_payment, 2),
            'Remaining Balance': round(remaining_balance, 2)
        })
    
    total_repayment = period_payment * num_payments
    
    result = {
        'Total Interest': round(total_interest, 2),
        'Total Repayment': round(total_repayment, 2),
        'Repayment Schedule': repayment_schedule
    }
    
    return result
