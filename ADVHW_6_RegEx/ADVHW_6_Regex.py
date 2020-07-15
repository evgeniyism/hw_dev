import csv
import re
import itertools
from pprint import pprint


with open('phonebook_raw.csv', 'r', encoding='utf-8') as f:
  data = csv.reader(f, delimiter=",", )
  contacts = list(data)

pattern_name = re.compile(r'([А-Я]{1}[а-я]*)((\s)|(\'\,\s\'))([А-Я]{1}[а-я]*)((\s)|(\'\,\s\'))?([А-Я]{1}[а-я]*)?')
pattern_phone = re.compile(r'(\+7|8)\s?\(?(\d{3})\)?.?(\d{3}).?(\d{2}).?(\d{2})')
pattern_additional = re.compile(r'доб.\s(\d{4})')

result_raw = []
for i in contacts[1:]:
    name = re.findall(pattern_name, ''.join(i[0:3]))
    newname = list(re.sub(pattern_name, r'\1 \5 \9', ' '.join(i[0:3])).split())
    if len(newname) < 3:
        newname.append('')
    place = i[3]
    position = i[4]
    phone = re.findall(pattern_phone, i[5])
    additional = re.findall(pattern_additional, i[5])
    if len(phone) > 0:
        format_phone = f'+7 ({phone[0][1]}) {phone[0][2]}-{phone[0][3]}-{phone[0][4]}'
        if additional:
            format_phone = f'{format_phone} доб.{str(additional[0])}'
    else:
        format_phone = ''
    email = i[6]
    new_contact = [newname[0], newname[1], newname[2], place, position, format_phone, email]
    if len(result_raw) > 0:
        for record in result_raw:
            if new_contact[0] in record:
                for value in new_contact:
                    if value not in record:
                        record.append(value)
            else:
                result_raw.append(new_contact)
    else:
        result_raw.append(new_contact)
result_raw.sort()
phonebook = [['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']]
result_clear = list(result_raw for result_raw,_ in itertools.groupby(result_raw))
garb = result_clear[0]
result_clear.remove(garb)
phonebook.extend(result_clear)

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(phonebook)
