from xml.etree import ElementTree
import requests
import multiprocessing as mp

def say_hello(_):
    pid = mp.current_process().pid
    print('Hello world from process: ', pid)
    return pid


def download(id):
    pid = mp.current_process().pid
    url = f"https://name-service-phi.vercel.app/api/v1/names/{id}.json"
    response = requests.get(url)
    #events = ElementTree.iterparse(response.raw)
    print(f"Id: {id} -> {response.json()}")
    return pid

if __name__ == '__main__':
    #print(list(range(25)))

    with mp.Pool(5) as p:
        #result = p.map(say_hello, range(25))
        result = p.map(download, range(25))

    print(result)

    
