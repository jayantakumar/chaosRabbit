import pika
from pika.exchange_type import ExchangeType
import time,random,math,numpy as np
from multiprocessing import Process
from xmlrpc.client import ServerProxy
import os

consumerInstance = ServerProxy('http://localhost:3001')

def Consumer(i):
    np.random.seed(i)

    def message_recived(ch,method,properties,body):
        timeout = np.random.exponential(1/130)
        time.sleep(timeout)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return 0

    connectionParams = pika.ConnectionParameters("localhost")
    connection = pika.BlockingConnection(connectionParams)

    channel = connection.channel()
    channel.exchange_declare(exchange="pubsub",exchange_type=ExchangeType.fanout)
    queue = channel.queue_declare(queue="test")
    channel.queue_bind(exchange="pubsub",queue=queue.method.queue)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue.method.queue,on_message_callback=message_recived)

    #print("Starting consumer!")

    channel.start_consuming()

if __name__ =="__main__":
    plist = []
    process_id_list = []
    c = Process(target=Consumer)
    for i in range(100):
        c = Process(target=Consumer,args=[i])
        plist.append(c)
        c.start()
        process_id_list.append(c.pid)
    consumerInstance.putPids(process_id_list)             
    for p in plist:
        p.join()
    
