import google.protobuf.message

def print_fields(msg: google.protobuf.message.Message):
    print(msg.DESCRIPTOR.fields)
