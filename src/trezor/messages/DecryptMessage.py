# Automatically generated by pb2py
from protobuf import protobuf as p
t = p.MessageType()
t.add_field(1, 'address_n', p.UVarintType, flags=p.FLAG_REPEATED)
t.add_field(2, 'nonce', p.BytesType)
t.add_field(3, 'message', p.BytesType)
t.add_field(4, 'hmac', p.BytesType)
DecryptMessage = t