class CANFrame:

    def __init__(self, can_id, data):

        self.can_id = can_id

        self.data = data

    def display(self):

        print("------------")

        print("CAN FRAME")

        print("ID :", hex(self.can_id))

        print("DATA :", self.data)

        print("------------")


if __name__ == "__main__":

    frame = CANFrame(

        0x100,

        {
            "rpm": 1500
        }

    )

    frame.display()