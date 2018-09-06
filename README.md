
DEMO:API
http://192.168.134.200:5000/apidocs/

http --json GET http://192.168.134.200:5000/api/v1.0/java
http --json --auth : GET http://192.168.134.200:5000/api/v1.0/java
http --json --auth admin:123 GET http://192.168.134.200:5000/api/v1.1/java
http --json --auth admin:123 GET http://192.168.134.200:5000/api/v1.0/java

tree -L 4 -C -I __pycache__
