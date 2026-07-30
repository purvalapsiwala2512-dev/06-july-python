correct_pin = '1234'

attempts = 0
max_attempts = 3 

while attempts < max_attempts:
    pin = input('Enter your PIN: ')
    if pin == correct_pin:
       print('Access granted. Welcome!')
       break

    else:
        attempts += 1

        remaining = max_attempts - attempts
print(f'Wrong PIN. {remaining} attempt(s) left.')

if attempts == max_attempts:
 print('Card blocked. Contact your bank')