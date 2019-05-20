import emoji
from twilio.rest import Client 
from datetime import date

today = date.today()
month = int(str(today.month))

account_sid = ""
auth_token = ""
client = Client(account_sid,auth_token)

def main(): 

    while True
    month = int(str(date.today().month))

    if current_month != month 
        current_month = month 
        sendText(current_month) 


def sendText(month): 

    if month  == 1: 
        message = client.messages.create(
            body= emoji.emojize("happy new year :boom:", use_aliases = True),
            from_='',
            to=''
        )

    elif month  == 2: 
        message = client.messages.create(
            body= emoji.emojize("happy february! ", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month  == 3: 
        message = client.messages.create(
            body= emoji.emojize("happy march :clover:", use_aliases = True),
            from_='',
            to=''
        )

    elif month  == 4: 
        message = client.messages.create(
            body= emoji.emojize("happy april fools day! ::stuck_out_tongue_closed_eyes:", use_aliases = True),
            from_='',
            to=''
        )

    elif month  == 5: 
        message = client.messages.create(
            body= emoji.emojize("Happy May Day! :heart:", use_aliases = True),
            from_='+Twilio Number',
            to='+Your Phone Number'
        )

    elif month  == 6: 
        message = client.messages.create(
            body= emoji.emojize("Happy June! :sun:", use_aliases = True),
            from_='',
            to=''
        )

    elif month  == 7:
        message = client.messages.create(
            body= emoji.emojize("Happy July! It's almost my birthday :blush:", use_aliases = True),
            from_='',
            to=''
        )

    elif month  == 8: 
        message = client.messages.create(
            body= emoji.emojize("Happy August! Almost school time :sad: ", use_aliases = True),
            from_='',
            to=''
        )

    elif month  == 9: 
        message = client.messages.create(
            body= emoji.emojize("Happy September! Time to hit the books :book: ", use_aliases = True),
            from_='',
            to=''
        )

    elif month  == 10: 
        message = client.messages.create(
            body= emoji.emojize("Happy October! Have a spooky time :pumpkin: ", use_aliases = True),
            from_='',
            to=''
        )

    elif month  == 11: 
        message = client.messages.create(
            body= emoji.emojize("Happy November! Have a great thanksgiving, I'm thankful for you :turkey: ", use_aliases = True),
            from_='',
            to=''
        )

    elif month  == 12: 
        message = client.messages.create(
            body= emoji.emojize("Happy December! Merry Christmas :Santa: ", use_aliases = True),
            from_='',
            to=''
        )

if __name__ == "__main__": 
    main()


