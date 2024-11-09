import requests
import threading

def fire_get_and_forget(url, params=None, **kwargs):
    """
    Fire off a GET request and forget about it.

    This function sends a GET request to the specified URL and then forgets about it.
    It does not return anything or wait for a response.

    :param url: The URL to send the GET request to.
    :param params: The parameters to send with the GET request.
    :param **kwargs: Any additional keyword arguments to pass to the request.
    """
    def send_request(url, params=None, **kwargs): 
        _ = requests.get(url, params, **kwargs)
    thread = threading.Thread(target=send_request(url))
    thread.start()