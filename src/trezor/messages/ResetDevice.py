# Automatically generated by pb2py
from protobuf import protobuf as p
t = p.MessageType()
t.add_field(1, 'display_random', p.BoolType)
t.add_field(2, 'strength', p.UVarintType, default=256)
t.add_field(3, 'passphrase_protection', p.BoolType)
t.add_field(4, 'pin_protection', p.BoolType)
t.add_field(5, 'language', p.UnicodeType, default=u'english')
t.add_field(6, 'label', p.UnicodeType)
ResetDevice = t