from xmlrpc.client import ServerProxy
import json
import time
import numpy as np
from multiprocessing import Process
import pickle
import pandas as pd
import asyncio
import pyswarms as ps

chaosRabbitInstance = ServerProxy("http://localhost:3000")
consumerInstance = ServerProxy('http://localhost:3001')



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

    def collect_probe_data(self,timeStep,totatTime,fileName):
        while totatTime>0:
            self.q1.collect()
            totatTime=totatTime-timeStep
            time.sleep(timeStep)
        print("probe over")
        data = pd.DataFrame.from_dict(self.q1.__dict__)
        data.to_csv(fileName, sep='\t')


    def experiment(self):
        self.collect_probe_data(timeStep=5,totatTime=1800,fileName="NoPertubationData2")
        print("done")

        
class Experiment2():
    
    def __init__(self) -> None:
        self.q1 = QueueEntity("test")
        self.maxMemory = 40000
        self.consumerList = []
        self.Steady_State = pd.read_csv("NoPertubationData",sep="\t")
       

    def rollback(self):
        for p in self.consumerList:
            consumerInstance.resumeProcess(p)
        


    def collect_probe_data(self,timeStep,totatTime,fileName):
        while totatTime>0:
            self.q1.collect()
            if(max(self.q1.q_messages_count)>self.maxMemory):
                self.rollback()
                print("memory limit reached...")
                return "BAD"
            totatTime=totatTime-timeStep
            time.sleep(timeStep)
        print("probing done")
      
        
        return self.q1.q_messages_count
    
    def refreshAndWaitForSteadyState(self):
        chaosRabbitInstance.purgeQueue("rabbit-server")
        while(self.Steady_State["q_messages_count"].quantile(0.15)<int(chaosRabbitInstance.get_messages())):
             time.sleep(5)
             print("waiting...")
    
    def sub_experiment(self,kill_count,time_param):
         self.q1 = QueueEntity("test")
         self.consumerList = consumerInstance.getPids()
         for p in range(kill_count):
             consumerInstance.killProcess(self.consumerList[p])
         print("killed")
         result = self.collect_probe_data(5,time_param,f"Killed_{kill_count} time_{time_param}")
         self.rollback()
         print("rollback done")
         return result


    def experiment(self,t,kill):
         self.consumerList = consumerInstance.getPids()
         confidenceRepetitions = 1
         composite_vector = np.array([])

         print(f"kill: {kill}  time: {t}")
         for i in range(confidenceRepetitions): 
             self.rollback()
             self.refreshAndWaitForSteadyState()
             result = self.sub_experiment(kill_count=kill,time_param=t)
             if(result == "BAD"):
                 print("BAD")
             else:
                 composite_vector = np.concatenate((composite_vector, np.array(result)))
                 pd.DataFrame(composite_vector).to_csv(f"kill:{kill} time:{t}.csv", sep='\t')




if __name__=="__main__":
        Experiment2().experiment(t=50,kill=10)
        Experiment2().experiment(t=50,kill=20)
        Experiment2().experiment(t=50,kill=30)
        Experiment2().experiment(t=50,kill=40)

        
