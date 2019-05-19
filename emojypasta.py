import emoji
from twilio.rest import Client 
from datetime import date


today = date.today()
month = int(str(today.month))

account_sid = "AC9f70aceb6df3479af5b7c9c8bd4058cf"
auth_token = "a22c7649bbb08d0779a6c71887bdaff5"
client = Client(account_sid,auth_token)

if month == 1: 
	message = client.messages.create(
		body = emoji.emojize("get :weary: ready for  JIZZ :sweat_drops: JAR :yum: JANUARY :cloud: ", use_aliases = True),
		from_= '+17322904210' ,
		to = '+17324237064'
	)

elif month == 5: 
	message = client.messages.create(
		body = emoji.emojize(" it's MAY DAY you CUMMODITY fetishist :construction_worker::construction_worker: Most people :family: :couple:  are forced to work :computer: :phone: :hammer: for PROFIT :heavy_dollar_sign: :moneybag: :chart_with_upwards_trend: :chart_with_downwards_trend: :sweat: but I would work :computer: :phone: :hammer: for YOU :man_with_turban:  because YOU'RE MY CUM-RADE :droplet: :droplet: ", use_aliases = True),
		from_ = '+17322904210' ,
		to = '+17323221591'
	)