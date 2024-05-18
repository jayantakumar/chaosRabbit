import requests
import json
from requests.auth import HTTPBasicAuth
from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(('localhost',3000),logRequests=True)
userName = "guest"
password = "guest"
vhost_name = "%2f"
url = "http://localhost:15672/api/queues/"+vhost_name


class QueueGetter:
    def __init__(self, queue, username, password):
        self.url = url+"/"+queue
        self.username = username
        self.password = password
        self.queue = queue

    def get_data(self):
        response = requests.get(self.url, auth=HTTPBasicAuth(self.username, self.password))
        return response.json()
    
    def set_queue(self,queue):
        self.url = url+"/"+queue
        return "Success"

    # Getters for top-level fields
    def get_consumer_details(self):
        response = self.get_data()
        return response.get("consumer_details")

    def get_arguments(self):
        response = self.get_data()
        return response.get("arguments")

    def get_auto_delete(self):
        response = self.get_data()
        return response.get("auto_delete")

    def get_consumer_capacity(self):
        response = self.get_data()
        return response.get("consumer_capacity")

    def get_consumer_utilisation(self):
        response = self.get_data()
        return response.get("consumer_utilisation")

    def get_consumers(self):
        response = self.get_data()
        return response.get("consumers")

    def get_deliveries(self):
        response = self.get_data()
        return response.get("deliveries")

    def get_durable(self):
        response = self.get_data()
        return response.get("durable")

    def get_effective_policy_definition(self):
        response = self.get_data()
        return response.get("effective_policy_definition")

    def get_exclusive(self):
        response = self.get_data()
        return response.get("exclusive")

    def get_exclusive_consumer_tag(self):
        response = self.get_data()
        return response.get("exclusive_consumer_tag")

    def get_garbage_collection(self):
        response = self.get_data()
        return response.get("garbage_collection")

    def get_head_message_timestamp(self):
        response = self.get_data()
        return response.get("head_message_timestamp")

    def get_incoming(self):
        response = self.get_data()
        return response.get("incoming")

    def get_memory(self):
        response = self.get_data()
        return response.get("memory")

    def get_message_bytes(self):
        response = self.get_data()
        return response.get("message_bytes")

    def get_message_stats(self):
        response = self.get_data()
        return response.get("message_stats")
    
    def get_message_stats_string(self):
        response = self.get_data()
        return json.dumps(response.get("message_stats"))

    def get_messages(self):
        response = self.get_data()
        return response.get("messages")

    def get_name(self):
        response = self.get_data()
        return response.get("name")

    def get_node(self):
        response = self.get_data()
        return response.get("node")

    def get_operator_policy(self):
        response = self.get_data()
        return response.get("operator_policy")

    def get_owner_pid_details(self):
        response = self.get_data()
        return response.get("owner_pid_details")

    def get_policy(self):
        response = self.get_data()
        return response.get("policy")

    def get_recoverable_slaves(self):
        response = self.get_data()
        return response.get("recoverable_slaves")

    def get_reductions(self):
        response = self.get_data()
        return response.get("reductions")

    def get_single_active_consumer_tag(self):
        response = self.get_data()
        return response.get("single_active_consumer_tag")

    def get_state(self):
        response = self.get_data()
        return response.get("state")

    def get_storage_version(self):
        response = self.get_data()
        return response.get("storage_version")

    def get_type(self):
        response = self.get_data()
        return response.get("type")

    def get_vhost(self):
        response = self.get_data()
        return response.get("vhost")
    
    def get_message_stats_ack(self):
        message_stats = self.get_message_stats()
        return message_stats.get("ack")

    def get_message_stats_ack_rate(self):
        ack_details = self.get_message_stats().get("ack_details")
        return ack_details.get("rate")

    def get_message_stats_deliver(self):
        message_stats = self.get_message_stats()
        return message_stats.get("deliver")

    def get_message_stats_deliver_rate(self):
        deliver_details = self.get_message_stats().get("deliver_details")
        return deliver_details.get("rate")

    def get_message_stats_deliver_get(self):
        message_stats = self.get_message_stats()
        return message_stats.get("deliver_get")

    def get_message_stats_deliver_get_rate(self):
        deliver_get_details = self.get_message_stats().get("deliver_get_details")
        return deliver_get_details.get("rate")

    def get_message_stats_deliver_no_ack(self):
        message_stats = self.get_message_stats()
        return message_stats.get("deliver_no_ack")

    def get_message_stats_deliver_no_ack_rate(self):
        deliver_no_ack_details = self.get_message_stats().get("no_ack_details")
        return deliver_no_ack_details.get("rate")

    def get_message_stats_get(self):
        message_stats = self.get_message_stats()
        return message_stats.get("get")

    def get_message_stats_get_rate(self):
        get_details = self.get_message_stats().get("get_details")
        return get_details.get("rate")

    def get_message_stats_get_empty(self):
        message_stats = self.get_message_stats()
        return message_stats.get("get_empty")

    def get_message_stats_get_empty_rate(self):
        get_empty_details = self.get_message_stats().get("empty_details")
        return get_empty_details.get("rate")

    def get_message_stats_get_no_ack(self):
        message_stats = self.get_message_stats()
        return message_stats.get("get_no_ack")

    def get_message_stats_get_no_ack_rate(self):
        get_no_ack_details = self.get_message_stats().get("no_ack_details")
        return get_no_ack_details.get("rate")

    def get_message_stats_publish(self):
        message_stats = self.get_message_stats()
        return message_stats.get("publish")

    def get_message_stats_publish_rate(self):
        publish_details = self.get_message_stats().get("publish_details")
        return publish_details.get("rate")

    def get_message_stats_redeliver(self):
        message_stats = self.get_message_stats()
        return message_stats.get("redeliver")

    def get_message_stats_redeliver_rate(self):
        redeliver_details = self.get_message_stats().get("redeliver_details")
        return redeliver_details.get("rate")
    
    def injector_SetQueueMaxBytes(self,limit=100000,container_name="rabbit-mq",policy_name="my_policy",queue_name=""):
        command = f"rabbitmqctl set_policy {policy_name}"+f" \"^{queue_name}$\""+" \'{\"max-length-bytes\":"+f"{limit}"+"}\' --apply-to queues"
        command = f"docker exec {container_name} "+command
        print(command)
        # change your execution to appropriate system , here its the local terminal
        import os
        try:
            output = os.system(command)
            print(output)
            return "Success"
        except:
            print("Exception occured")
            return Exception("Exception Occured")
        
    def injector_SetQueueMax(self,limit=100,container_name="rabbit-mq",policy_name="my_policy",queue_name=""):
        command = f"rabbitmqctl set_policy {policy_name}"+f" \"^{queue_name}$\""+" \'{\"max-length\":"+f"{limit}"+"}\' --apply-to queues"
        command = f"docker exec {container_name} "+command
        print(command)
        # change your execution to appropriate system , here its the local terminal
        import os
        try:
            output = os.system(command)
            print(output)
            return "Success"
        except:
            print("Exception occured")
            return Exception("Exception Occured")
        
    def rollbackPolicy(self,container_name,policy_name="my_policy",vhost_name="/"):
        command = f"rabbitmqctl clear_policy -p {vhost_name} {policy_name}"
        command = f"docker exec {container_name} "+command
        import os
        try:
            output = os.system(command)
            print(output)
            return "Success"
        except:
            print("Exception occured")
            return Exception("Exception Occured")
        
    def purgeQueue(self,container_name):
        command = f"docker exec {container_name} rabbitmqctl purge_queue {self.queue}"
        import os
        try:
            output = os.system(command)
            print(output)
            return "success"
        except:
            print("Exception occured")
            return Exception("Exception Occured")


    

    

        

        





server.register_instance(QueueGetter("test","guest","guest"))
if __name__=="__main__":
    try:
        print("Serving..")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting..")
