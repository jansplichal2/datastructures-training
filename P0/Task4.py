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

def textingNumbers(texts):
  """Gets phone numbers that are texting"""
  texting = set()
  for text in texts:
    incoming, receiving, _ = text
    texting.add(incoming)
    texting.add(receiving)
  return texting

def calledNumbers(calls):
  """Gets phone numbers that have been called"""
  called = set()
  for call in calls:
    called.add(call[1])
  return called

def callingNumbers(calls):
  """Gets phone numbers that have been calling somebody"""
  calling = set()
  for call in calls:
    calling.add(call[0])
  return calling

def possibleMarketers(calls, texts):
  """Gets calling numbers minus called numbers and texting numbers"""
  callers = callingNumbers(calls)
  called = calledNumbers(calls)
  texting = textingNumbers(texts)  
  return callers.difference(called).difference(texting)


def main(calls, texts):
  telemarketers = possibleMarketers(calls, texts)
  print("These numbers could be telemarketers: ")
  print('\n'.join(sorted(telemarketers)))  

main(calls, texts)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

