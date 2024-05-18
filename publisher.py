import pika,time,random
from pika.exchange_type import ExchangeType
import numpy as np
from multiprocessing import Process

def publish(i):
    np.random.seed(i)
    connectionParams = pika.ConnectionParameters("localhost")
    connection = pika.BlockingConnection(connectionParams)

    channel = connection.channel()
    channel.exchange_declare(exchange="pubsub",exchange_type=ExchangeType.fanout)

    channel.queue_declare(queue="test")
    import numpy
    d = 30
    n = 1000000
    data = numpy.random.uniform(0, 1000,size=(n,d))
    message = str(data)

    try: 
        while True:
            inter_arrival_time = np.random.exponential(1/90)

            channel.basic_publish(exchange="pubsub",routing_key="",body=message)
            #print(inter_arrival_time)
            time.sleep(inter_arrival_time)
    except KeyboardInterrupt:
        print(f"Closing Publisher:{message}")
        connection.close()

if __name__ =="__main__":
    plist = []
    c = Process(target=publish)
    for i in range(100):
        c = Process(target=publish,args=[1000-i])
        plist.append(c)
        c.start()
    
    for p in plist:
        p.join()
    