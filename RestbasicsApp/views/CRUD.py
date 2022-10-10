from email import message
from itertools import count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import DataSerializer,CarModelSerializer
from urllib.request import urlopen
import queue, time, urllib.request
from threading import Thread
import json
from ..models import Data

@api_view(['POST'])
def postAllInValidData(request):
  
    def perform_web_requests(addresses, no_workers):
        class Worker(Thread):
            def __init__(self, request_queue):
                Thread.__init__(self)
                self.queue = request_queue
                self.results = []

            def run(self):
                while True:
                    content = self.queue.get()
                    if content == "":
                        break
                    response = urlopen(content)
                    data_json = json.loads(response.read())
                    for each in data_json["Results"]:
                        # data = CarModelSerializer(data = each)
                        self.results.append(each)
                    self.queue.task_done()

        # Create queue and add addresses
        q = queue.Queue()
        for url in addresses:
            q.put(url)

        # Workers keep working till they receive an empty string
        for _ in range(no_workers):
            q.put("")

        # Create workers and add tot the queue
        workers = []
        for _ in range(no_workers):
            worker = Worker(q)
            worker.start()
            workers.append(worker)
        # Join workers to wait till they finished
        for worker in workers:
            worker.join()

        # Combine results from all workers
        r = []
        for worker in workers:
            r.extend(worker.results)
        return r

    wantedUrls = []
    for year in range(2010,2019,1):
        url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/honda/modelyear/" + str(year) + "?format=json"
        wantedUrls.append(url)

    unWantedUrls = []
    for year in range(2019,2021,1):
        url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/honda/modelyear/" + str(year) + "?format=json"
        unWantedUrls.append(url)

    wantedResults = perform_web_requests(wantedUrls, 10)
    unwantedResults = perform_web_requests(unWantedUrls, 2)

    ans = []
    real_ans = Data()
    real_ans.Count = 100
    real_ans.save()
    for i in wantedResults:
        flag = False
        for j in unwantedResults:
            if(i.is_valid() and j.is_valid()):
                if(i["Model_ID"] == j["Model_ID"]):
                    flag = True
                    break
        if(not flag):
            # i.save()
            print(i)
            real_ans.Results.add(i)
            ans.append(i)

    # se = DataSerializer(data = real_ans)
    # print(se)
    # print("HI")
    # if(se.is_valid()):
        # se.save()
        # print(se.data)
    print(real_ans)
    return Response("SAVED DATA",status=status.HTTP_201_CREATED)
    return Response(se.errors, status=status.HTTP_400_BAD_REQUEST)

