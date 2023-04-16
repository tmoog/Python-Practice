def print_rates_chart() -> None:
    file_name = "pricing_sheet.csv"
    #product_name=input('Enter Product Name:')
    product_name='10003.20.001'
    #lock_period=input('Enter Lock Period:')
    lock_period='45'
    #loan_amount=input('Enter Loan Amount:')
    loan_amount='250000'
    pricing_sheet_csv = open(file_name)
    
    list_of_matching_products_and_locks = []

    for line in pricing_sheet_csv:
        line=line.strip()
        temp_list=line.split(',')

        if temp_list[0] == product_name and temp_list[1] == lock_period:
            try:
                cost = -(int(loan_amount) * (float(temp_list[2]) - 100) / 100)
                if cost == -0.00: cost = 0.00

                rate = temp_list[3]
            except:
                pass

            list_of_matching_products_and_locks.append((product_name, lock_period, cost, rate))

    border = '|--------------|--------|----------------|--------|'
    print(border)
    print('|              |  Lock  |                |        |')
    print('| Product Name | Period |      Cost      |  Rate  |')
    print(border)

    for product_name, lock_period, cost, rate, in list_of_matching_products_and_locks:
        cost = '${:,.2f}'.format(cost)
        rate='{:.3f}'.format(float(rate))
        print('| {} | {:>6} | {:>14} | {:>5}% |'.format(product_name,lock_period,cost,rate))
    

if __name__ == "__main__":
    print_rates_chart()
