from can_stack.can_frame import CANFrame
from can_stack.can_bus import CANBus
from can_stack.can_logger import CANLogger


class CANDriver:

    def __init__(self):
        self.bus = CANBus()
        self.logger = CANLogger()

    def send_message(self, can_id, data):

        frame = CANFrame(can_id, data)

        self.logger.log(frame)

        self.bus.transmit(frame)


if __name__ == "__main__":

    driver = CANDriver()

    driver.send_message(
        0x100,
        {
            "rpm": 3000,
            "temperature": 32
        }
    )
    