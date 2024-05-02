import pika
from pika.exchange_type import ExchangeType
import time,random,math,numpy as np
from multiprocessing import Process
def Consumer():
    def message_recived(ch,method,properties,body):
        timeout = np.random.exponential(1/10)
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

    print("Starting consumer!")

    channel.start_consuming()

if __name__ =="__main__":
    plist = []
    c = Process(target=Consumer)
    for i in range(30):
        c = Process(target=Consumer)
        plist.append(c)
        c.start()
    for p in plist:
        p.join()
    