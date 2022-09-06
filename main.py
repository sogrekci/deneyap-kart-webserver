from urldecode import urldecode

try:
  import usocket as socket
except:
  import socket

if not exit_btn.value():
    print("System exit!\n")
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

while True:
  conn, addr = s.accept()
  print('\nGot a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = request.decode()
  print('\n\nContent = %s\n\n' % request)
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
      print("OSError!")
  
  if data:
      try:
          print("\nEXECUTING..\n")
          exec(data)
          print("\nCOMMANDS EXECUTED!\n\n") 
      except Exception as e:
          print("FAILED:\n" + str(e))
