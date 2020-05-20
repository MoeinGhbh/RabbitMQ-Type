# Exchange Type

## RabbitMQ has four type to send message

---

    * Direct Exchange
    * Fanout Exchange
    * Topic Exchange
    
    * Header Exchange
        
        1:
            * python queue.py Q1 'any' A C
            * python queue.py Q1 'any' A C
        2:
            * python consumer.py C1 Q1
            * python consumer.py C1 Q2
            * python consumer.py C1 Q3
        3:
            * python producer.py P1 'Message 1 from producer P1' A
              Producer name: P1, headers: {'K1': 'A'}, message text:{"producerName": "P1", headersValues": ["A"], "headers": {"K1": "A"}, "messageText": "Message 1 from producer P1"}

