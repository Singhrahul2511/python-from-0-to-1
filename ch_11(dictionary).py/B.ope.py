courses = {'cs101':'c progm','cs102':'java','cs103':'sql'}
#add new key_val pair
courses['cs104'] ='web dev'
#modify
courses['cs102'] = 'opps in java'
print(courses)

#delete
del(courses['cs101'])
print(courses)

#del whole dict
del(courses)