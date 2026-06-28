from can_stack.can_frame import CANFrame

class CANLogger:

    def log(self, frame):

        print("===== CAN LOGGER =====")
        print("CAN ID :", hex(frame.can_id))
        print("DATA   :", frame.data)
        print("======================")

if __name__ == "__main__":

    logger = CANLogger()

    frame = CANFrame(
        0x200,
        {
            "temperature": 40
        }
    )

    logger.log(frame)