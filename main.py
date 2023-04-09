import requests
import datetime
import os

requests.post("https://pixe.la/v1/users/townsend/graphs/townsend",json = {"date": datetime.date.today().strftime("%Y%m%d"), "quantity": input("how many rounds did u do today: ")}, headers = {"X-USER-TOKEN": os.environ.get("TOKEN")})