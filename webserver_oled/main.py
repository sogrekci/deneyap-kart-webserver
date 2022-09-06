from urldecode import urldecode

try:
  import usocket as socket
except:
  import socket

if not exit_btn.value():
    print("System exit!\n")
    oprint("SYSTEM EXIT!",20,startfill=True)
    time.sleep(1)
    oprint("",0,endfill=True)
    sys.exit(1)


web_page_html = """
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
</head>
<body>
<h1>Deneyap Kart Web Sunucu</h1>
<form action="/" method="post" accept-charset="UTF-8">
<textarea id="code" name="code" rows="20" cols="50"></textarea>
<br><br>
<input type="submit" value="Gönder">
</form>
</body>
</html>
"""


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 80))
s.listen(5)
print("\nListening..\n")
oprint("LISTENING..",40)

while True:
  conn, addr = s.accept()
  print('\nGot a connection from %s' % str(addr))
  oprint("GOT A CONNECTION!",40, startfill=True)
  oprint("CONNECTED",20)
  oprint("IP:%s" % station.ifconfig()[0],0)
  request = conn.recv(1024)
  request = request.decode()
  print('\n\nContent = %s\n\n' % request)
  oprint("DATA RECEIVED..",40, startfill=True)
  time.sleep(0.5)
  oprint("IP:%s" % station.ifconfig()[0],0)
  oprint("CONNECTED",20)
  try:
      raw_data = request.splitlines()[-1][5:]
      data = urldecode(raw_data)
      if data:
          print("\nRECEIVED DATA:\n" + "-"*20)
          print(data)
          print("-"*20)
  except:
      data = ""
      print("NO DATA RECEIVED!")
  
  response = web_page_html
  try:
      conn.send('HTTP/1.1 200 OK\n')
      conn.send('Content-Type: text/html\n')
      conn.send('Connection: close\n\n')
      conn.sendall(response)
      conn.close()
  except OSError:
      oprint("OSError!", 30, startfill=True)
      time.sleep(0.5)
      oprint(" ",0,endfill=True)
  
  if data:
      try:
          print("\nEXECUTING..\n")
          exec(data)
          print("\nCOMMANDS EXECUTED!\n\n") 
          oprint("EXECUTED..",40, startfill=True)
          time.sleep(3)
          oprint("CONNECTED",20)
          oprint("IP:%s" % station.ifconfig()[0],0)
      except Exception as e:
          print("FAILED:\n" + str(e))
          oprint("",0,endfill=True)
          oprint("IP:%s" % station.ifconfig()[0],0)
          oprint("CONNECTED",20)
          oprint("FAILED!",40, startfill=True)
          time.sleep(3)
  
  oprint("LISTENING..",40, startfill=True)
  oprint("IP:%s" % station.ifconfig()[0],0)
  oprint("CONNECTED",20)

