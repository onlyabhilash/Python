import re

emails = '''
AbhilashNAchalkar@gmail.com
abhilash.achalkar@university.edu
abhilash-321-achalkar@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)
