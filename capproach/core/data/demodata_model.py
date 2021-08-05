# python3 manage.py shell < core/data/demodata_model.py 
from django.contrib.auth.models import User
from core.models import Contact
import pandas
userid = User.objects.filter(username='testuser').values_list('id', flat=True).first()
instance = Contact.objects.filter(created_by_id=userid)
instance.delete()
print('*** deleted records from database matching to user ' + str(userid) + ' ***')
Contact.objects.filter(created_by_id=userid)
df = pandas.read_csv('core/data/demodata.csv')
for index, row in df.iterrows():
	p = Contact(date_approach = df.loc[index, 'date_approach'],
		time_approach = df.loc[index, 'time_approach'],
		name = df.loc[index, 'name'],
		age = df.loc[index, 'age'],
		nationality = df.loc[index, 'nationality'],
		duration = df.loc[index, 'duration'],
		interaction = df.loc[index, 'interaction'],
		looks = df.loc[index, 'looks'],
		close = df.loc[index, 'close'],
		reply = df.loc[index, 'reply'],
		date = df.loc[index, 'date'],
		lay = df.loc[index, 'lay'],
		comments = df.loc[index, 'comments'],
		created_by_id = userid)
	p.save()
	print('*** saved record #'+ str(index) + ' into database ***')