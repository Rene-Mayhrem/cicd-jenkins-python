import subprocess

def deploy():
  print("Deploying the application")
  subprocess.run(["echo", "Deployment script executed"])
  
if __name__ == "__main__":
  deploy()