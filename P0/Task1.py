"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def uniquePhoneNumbers(texts, calls):
  uniques = set()
  
  for text in texts:
    sending, receiving, _ = text
    uniques.add(sending)
    uniques.add(receiving)

  for call in calls:
    sending, receiving, *rest = call
    uniques.add(sending)
    uniques.add(receiving)
    
  return len(uniques)
    
def main():
  uniqueNumbers = uniquePhoneNumbers(texts, calls)
  print('There are {} different telephone numbers in the records.'.format(uniqueNumbers))

main()

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
