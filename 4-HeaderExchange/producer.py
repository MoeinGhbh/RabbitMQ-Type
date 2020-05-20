#!/home/ubd/anaconda3/envs/test_env/bin/python
 
import json
import pika
import sys
 
if len(sys.argv) < 4:
	print("Call syntax: python SCRIPT_NAME PRODUCER_NAME MESSAGE_STRING HEADERS_VALUES")
	exit()
	
producerName = sys.argv[1]
messageText = sys.argv[2]	
headersValues = sys.argv[3:]
 
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
 
channel.exchange_declare(exchange='exchange_headers', exchange_type='headers')
 
headers = {}
number = 1
for headerValue in headersValues:
	headers["K" + str(number)] = headerValue
	number = number + 1
	
data = {
        "producerName": producerName,
        "headersValues": headersValues,
        "headers": headers,
        "messageText": messageText
    }
message = json.dumps(data)
 
channel.basic_publish(
    exchange='exchange_headers',
    routing_key='',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,
        headers=headers
    ))
    
print("Producer name: %s, headers: %s, message text:%s" % (producerName, headers, message))
connection.close()





# python producer.py P1 'Message 1 from producer P1' A Producer name: P1, headers: {'K1': 'A'}, message text:{"producerName": "P1", "headersValues": ["A"], "headers": {"K1": "A"}, "messageText": "Message 1 from producer P1"}