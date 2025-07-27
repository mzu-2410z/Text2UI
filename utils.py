# # %%writefile ngrok_utils.py
# import sys
# import os
# from pyngrok import ngrok
# import subprocess
# import time

# def setup_ngrok():
#     # Set ngrok authtoken (replace "YOUR_AUTHTOKEN" with your actual authtoken)
#     # You can get your authtoken from the ngrok dashboard after signing up: https://dashboard.ngrok.com/get-started/your-authtoken
#     ngrok.set_auth_token("30NTtOILT6cV7qjwaPWyrSb09ca_7ptSe44xTE6PSte8dq9vq")

#     # Start the Streamlit app
#     # Check if streamlit process is already running on port 8501
#     try:
#         # Use lsof to check for processes listening on port 8501
#         lsof_output = subprocess.check_output(['lsof', '-i', ':8501', '-t'])
#         if lsof_output:
#             print("Streamlit app is already running.")
#             return
#     except subprocess.CalledProcessError:
#         # lsof will return a non-zero exit code if no process is found
#         pass
#     except FileNotFoundError:
#         print("lsof command not found. Cannot check for running processes.")
#         print("Proceeding with starting Streamlit assuming it's not running.")


#     print("Starting Streamlit app in the background...")
#     # Use sys.executable to ensure the correct python environment is used
#     # Use os.path.abspath to get the absolute path of app.py
#     streamlit_path = os.path.join(os.path.dirname(__file__), 'app.py')
#     subprocess.Popen([sys.executable, "-m", "streamlit", "run", streamlit_path, "--server.port", "8501", "--server.headless", "true"],
#                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
#     print("Streamlit app started. Waiting a few seconds for it to initialize...")
#     time.sleep(5) # Give Streamlit a few seconds to start

# def create_ngrok_tunnel():
#     print("Creating ngrok tunnel...")
#     try:
#         # Disconnect existing tunnels to avoid conflicts
#         ngrok.kill()
#         time.sleep(1) # Give a moment for processes to terminate

#         public_url = ngrok.connect(8501).public_url
#         print(f"🔗 Public URL: {public_url}")
#         return public_url
#     except Exception as e:
#         print(f"Error creating ngrok tunnel: {e}")
#         return None

# def kill_ngrok_tunnels():
#     print("Disconnecting all active ngrok tunnels...")
#     try:
#         ngrok.kill()
#         print("All ngrok tunnels disconnected.")
#     except Exception as e:
#         print(f"Error killing ngrok tunnels: {e}")

# if __name__ == '__main__':
#     # Example usage (optional, for testing the script directly)
#     kill_ngrok_tunnels() # Ensure no tunnels are running before starting
#     setup_ngrok()
#     time.sleep(5) # Wait for streamlit to potentially start
#     public_url = create_ngrok_tunnel()
#     if public_url:
#         print(f"Access your Streamlit app at: {public_url}")
#     else:
#         print("Failed to create ngrok tunnel.")
#     # Note: The Streamlit app and ngrok tunnel will remain open until manually stopped or the script exits.
#     # In a notebook environment, you would typically call setup_ngrok() and create_ngrok_tunnel() from a notebook cell.