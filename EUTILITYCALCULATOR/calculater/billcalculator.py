
def calculate_bill(total_kwh):
    if total_kwh <= 50:
        service_charge=10
        bill_amount=total_kwh * 0.2730
    elif total_kwh <= 100:
         service_charge=42.00
         bill_amount=total_kwh * 0.7670
    elif total_kwh <= 200:
         service_charge=42.00
         bill_amount=total_kwh * 1.6200
    elif total_kwh <= 300:
         service_charge=42.00
         bill_amount=total_kwh * 2.0000
    elif total_kwh <= 400:
         service_charge=42.00
         bill_amount=total_kwh * 2.2000
    elif total_kwh <= 500:
         service_charge=42.00
         bill_amount=total_kwh * 2.4050
    elif total_kwh > 500:
         service_charge=42.00
         bill_amount=total_kwh * 2.4813
    else:
        bill_amount=0   
    total_bill = bill_amount + service_charge

    print(f"Energy Charge: {bill_amount} ETB")
    print(f"Service Charge: {service_charge:} ETB")
    print(f"TOTAL BILL: {total_bill:} ETB")

    return total_bill