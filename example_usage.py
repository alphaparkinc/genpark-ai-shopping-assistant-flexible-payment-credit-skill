from client import AiShoppingAssistantFlexiblePaymentCreditClient

def main():
    client = AiShoppingAssistantFlexiblePaymentCreditClient()
    res = client.plan_flexible_pay_in_four(480.0)
    print('Session: ' + res['klarna_session_id'] + ' (APR: ' + str(res['interest_apr_pct']) + '%)')
    print('Plan: 4 installments of $' + str(res['pay_in_4_installments'][0]['amount_usd']))
    print('Price Drop Shield: ' + str(res['ai_price_drop_protection_active']) + ' | Token: ' + res['single_click_merchant_checkout_token'])

if __name__ == '__main__':
    main()
