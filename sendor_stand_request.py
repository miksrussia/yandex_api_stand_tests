import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                         json=body,
                         headers=data.headers)



def get_order_by_number(order_track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER + order_track)


