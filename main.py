import re
import long_responses as long

def get_response(unser_input):
    split_message = re.split(r'\s+|[,;?!.-]')

# Testing response system
while True:
    print('Bot: ' + get_response(input('You: ')))