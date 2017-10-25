"""
This module uses zeroMQ publish-subscribe pattern
in order to create a failure detector and leader
election for Bully Algorithm.
"""
import time
import zmq


def peer(id, tokens, url, send_port, hosts):
    ctx = zmq.Context.instance()
    server = ctx.socket(zmq.PUB)
    server.bind('%s:%s' % (url, send_port))

    client = zmq.Context()
    sock = client.socket(zmq.SUB)
    sock.setsockopt(zmq.SUBSCRIBE, b"")
    tau = 0.1
    hosts_timeout = {peer_id: 0 for peer_id, host in hosts.items()}
    while True:
        time.sleep(1)
        curr_status = {}

        for name, ip in hosts.items():
            # if not current peer
            if id != name:
                # check out type of token
                # send my current token to all subscribers
                if type(tokens[id]) == bytes:
                    server.send(tokens[id])
                else:
                    server.send_string(tokens[id])
                # sleep tau of seconds 0.1s
                time.sleep(tau)
                # subscribe to one of the hosts list
                sock.connect(ip)
                message = sock.recv()

                # detect failure
                # 1. collect successful received tokens from other publishers
                for k, v in tokens.items():
                    # if my token 'message' equals the peer token
                    if message == v:
                            # set this that your token is received!
                            curr_status[k] = message
                # 2. detect failure
                for k in tokens.keys():
                    # if not my server
                    if id != k:
                        # if my subscriber received a token from this peer publisher
                        if k in curr_status.keys():
                            print('{host} Working!'.format(host=k))
                            hosts_timeout[k] = 0
                        # else give it timeout ~ 10x tau.
                        else:
                            if hosts_timeout[k] >= 10:
                                print('{host} down!'.format(host=k))
                                #TODO: start leader election in the future :)
                            hosts_timeout[k] += 1
