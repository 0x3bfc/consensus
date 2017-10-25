import peer

tokens = {'peer3': b'4d46eb472348b8b22e1ac9d58d85615328cda5927d6431a2ac5131eca105',
          'peer1': b'58661271ffbde96af93d368231eb49793aae9c53a3c32dbeba05cdb04f52',
          'peer2': b'eaee42eab023549b2285115b93e0b714b34f1888ff28b449071e042b1144'}
peer.peer('peer3',
          tokens,
          'tcp://127.0.0.1',
          '3335',
          {'peer1': 'tcp://127.0.0.1:4445',
           'peer2': 'tcp://127.0.0.1:5555',
           'peer3': 'tcp://127.0.0.1:3335'})
