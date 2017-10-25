# Consensus and Leader Election

This module uses zeroMQ publish-subscribe pattern in order to create a failure detector and leader election for Bully Algorithm. 

### pre-requests

* Ubuntu 16.04
* Docker 13.0+

### Start peers
 
in order to run this algorithm use the following command:

```
	$ sudo docker run -it -v <MYSRCFILES>:/home/user/github/ aabdulwahed/ubuntu:python3.5 bash
	$ cd /home/user/github/
	$ screen 1
	$ python3 peer1.py
	
	# run the other peers in another screens
	# scrren 2
	$ python3 peer2.py
	# screen 3
	$ python3 peer3.py
```

