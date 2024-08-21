import threading
import os
import time


# Backend function
def run_backend():
    os.system("python backend.py")


# Frontend function
def run_frontend():
    os.system("streamlit run frontend.py")


if __name__ == "__main__":
    # Create threads for backend and frontend
    backend_thread = threading.Thread(target=run_backend)
    frontend_thread = threading.Thread(target=run_frontend)

    # Start both threads
    backend_thread.start()
    time.sleep(2)  # Give backend some time to start
    frontend_thread.start()

    # Join threads to keep them running
    backend_thread.join()
    frontend_thread.join()
