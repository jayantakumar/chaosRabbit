from xmlrpc.client import ServerProxy
import json
import time
import numpy as np
from multiprocessing import Process
import pickle

chaosRabbitInstance = ServerProxy("http://localhost:3000")
def save_object(obj, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

# sample usage


class QueueEntity:
    def __init__(self,queueName) -> None:
        self.q_name = queueName
        self.q_published:np.array() = []
        self.q_publish_rate:np.array() = []
        self.q_delivered:np.array() = []
        self.q_delivered_rate:np.array() = []
        self.q_messages_count:np.array() = [] 

    def collect(self):
        chaosRabbitInstance.set_queue(self.q_name)
        message_stats = json.loads(chaosRabbitInstance.get_message_stats_string())
        message_in_queue = chaosRabbitInstance.get_messages()
        self.q_delivered.append(message_stats.get("deliver"))
        self.q_published.append(message_stats.get("publish"))
        self.q_publish_rate.append(message_stats.get("publish_details").get("rate"))
        self.q_delivered_rate.append(message_stats.get("deliver_details").get("rate"))
        self.q_messages_count.append(message_in_queue)


    def get_stat(self):
        return self.q_published

class ZeroExperiment:

    def __init__(self) -> None:
        self.q1 = QueueEntity("test")

    def collect_probe_data(self,timeStep,totatTime):
        while totatTime>0:
            self.q1.collect()
            totatTime=totatTime-timeStep
            time.sleep(timeStep)
        print("probe over")
        save_object(self.q1, 'queue1_probe.pkl')




    def experiment(self):
        self.collect_probe_data(5,900)
        self.q1.q_publish_rate
        


if __name__=="__main__":
    ZeroExperiment().experiment()

        
