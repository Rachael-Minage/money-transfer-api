from loans.loan_calculator import calculate_loan_repayment
from django.test import TestCase

class LoanRepaymentCalculatorTest(TestCase):
    
    def test_monthly_repayment(self):
        result = calculate_loan_repayment(1000, 12, 5, 'monthly')
        
        self.assertTrue(result['Total Interest'] > 0)
        self.assertTrue(result['Total Repayment'] > 1000)
        self.assertEqual(len(result['Repayment Schedule']), 12)

    def test_bi_monthly_repayment(self):
        result = calculate_loan_repayment(1000, 12, 5, 'bi-monthly')
        
        self.assertTrue(result['Total Interest'] > 0)
        self.assertTrue(result['Total Repayment'] > 1000)
        self.assertEqual(len(result['Repayment Schedule']), 6)

    def test_weekly_repayment(self):
        result = calculate_loan_repayment(1000, 12, 5, 'weekly')
        
        self.assertTrue(result['Total Interest'] > 0)
        self.assertTrue(result['Total Repayment'] > 1000)
        self.assertEqual(len(result['Repayment Schedule']), 52)

    def test_zero_interest(self):
        result = calculate_loan_repayment(1000, 12, 0, 'monthly')
        
        self.assertEqual(result['Total Interest'], 0)
        self.assertEqual(result['Total Repayment'], 1000)
        self.assertEqual(len(result['Repayment Schedule']), 12)
        for payment in result['Repayment Schedule']:
            self.assertEqual(payment['Interest Payment'], 0)
            self.assertEqual(round(payment['Principal Payment'], 2), round(1000 / 12, 2))

    def test_single_payment(self):
        result = calculate_loan_repayment(1000, 1, 5, 'monthly')
        
        self.assertTrue(result['Total Interest'] > 0)
        self.assertTrue(result['Total Repayment'] > 1000)
        self.assertEqual(len(result['Repayment Schedule']), 1)


