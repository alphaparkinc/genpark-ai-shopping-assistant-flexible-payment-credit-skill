class AiShoppingAssistantFlexiblePaymentCreditClient:
    def plan_flexible_pay_in_four(self, purchase_total_usd=320.0, user_account_tier='gold'):
        installment = round(purchase_total_usd / 4.0, 2)
        return {
            'klarna_session_id': 'kln_sess_5519',
            'pay_in_4_installments': [
                {'installment_num': 1, 'amount_usd': installment, 'due_date': 'TODAY_AT_PURCHASE'},
                {'installment_num': 2, 'amount_usd': installment, 'due_date': 'DAY_14'},
                {'installment_num': 3, 'amount_usd': installment, 'due_date': 'DAY_28'},
                {'installment_num': 4, 'amount_usd': installment, 'due_date': 'DAY_42'}
            ],
            'interest_apr_pct': 0.0,
            'ai_price_drop_protection_active': True,
            'single_click_merchant_checkout_token': 'tok_kln_991823'
        }
