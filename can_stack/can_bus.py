from can_stack.can_frame import CANFrame

class CANBus:

    def transmit(self, frame):

        print("===== CAN BUS =====")
        print("Message Transmitted Successfully")
        print("CAN ID :", hex(frame.can_id))
        print("DATA   :", frame.data)
        print("===================")

if __name__ == "__main__":

    bus = CANBus()

    frame = CANFrame(
        0x100,
        {
            "rpm": 2200
        }
    )

    bus.transmit(frame)
    