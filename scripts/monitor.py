import requests 

def monitor():
  print("Monitoring the application...")
  response = requests.get("http://localhost:5000/health")
  if response.status_code == 200:
    print("Application is healthy")
  else:
    print("Application is not healthy")
  
if __name__ == "__main__":
  monitor()
  