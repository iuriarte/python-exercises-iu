students = {
  'best': 'Mittens',
  'worst': 'Jason'
}

print(students['best'])
students['best'] = 'Lassie'
print(students['best'])
students['favorite_foods'] = ['pizza', 'chicken']
print(students['favorite_foods'][1])
## del students['favorite_foods']
print(students['favorite_foods'])
print(students)
for key, value in students.items():
    print('{}: {}'.format(key,value))
    
print(students.get('best'))