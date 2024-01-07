import psutil
import time

def pause_process_by_name(process_name, pause_duration):
    # Finde den Prozess nach dem Namen
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            # Pause für die angegebene Dauer
            proc.suspend()

            # Warte für die angegebene Dauer
            time.sleep(pause_duration)

            # Fortsetzen des Prozesses
            proc.resume()
            return


#Here you can set the Exe file, and the Timeout that the program will be stopped.
if __name__ == "__main__":
    exe_name = "eurotrucks2.exe"
    pause_duration = 3.5  # In Sekunden

    pause_process_by_name(exe_name, pause_duration)
