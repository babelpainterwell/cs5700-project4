
IPv4_HEADER_SIZE = 20  # 20 bytes
IPv4_MAX_SIZE = 65_515 # 65515 bytes

class IPv4Packet:

    def __init__(self, checksum=0, sourceAddress, destinationAddress, mode, data) -> None:
        """
        Purpose: Initializes an IPv4Packet object which encapsulates an IPv4 packet using the information specified
                 in the arguments. 
        ***SPECIFY THE DATA TYPES OF THE PARAMETERS/ARGMENTS ABOVE***
        :param checksum:
        :param sourceAddress:
        :param destinationAddress:
        :param mode:
        :param data: 
        :return: void
        """
        self.version = 4 #IPv4
        self.IHL = ??? # "Internet Header Length"; min value is 5?
        self.TOS = ??? # "Type of Service"; 0?
        self.totalLength = len(data) + IPV4_HEADER_SIZE
        self.ID = ??? # just a random value?
        self.flags = ??? #0?
        self.fragmentOffset = ???
        self.TTL = ??? # 255?
        self.protocol = ??? # socket.IPPROTO_TCP ?
        self.checksum = checksum
        self.sourceAddress = sourceAddress
        #self.destinationAddress = destinationAddress
        self.destinationAddress = destinationAddress if mode == "receive" else socket.gethostbyname(destinationAddress)
        
        self.options = ???
        
        self.data = data

    # need methods for:
        # formatting/encoding/packing IP packets (header fields)
        # decoding/parsing/unpacking incoming IP packets (getting the data and creating a new IPHeader object)

    def encodePacket(self) -> ?:
        """
        Purpose: Allows an IPv4Packet object to encode itself, thus preparing it to be sent out to a server.
        :return: Encoded IPv4Packet object. 
        """
        pass


    @staticmethod
    def decodePacket(self, received: bin) -> IPv4Packet:
        """
        Purpose: Takes in the encoded data which was received from the server, decodes this data, and
                 uses this data to create a new IPPacket object. 
        :param: ????? The encoded data received from the server.
        :return: IPv4Packet object which contains the decoded data 
        """
        pass
