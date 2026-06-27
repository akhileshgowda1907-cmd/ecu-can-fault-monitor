class CANReceiver:

    def receive_message(self, message_id, data):

        print("\nMessage Received")

        print(f"CAN ID : {hex(message_id)}")

        print(f"DATA   : {data}")


if __name__ == "__main__":

    receiver = CANReceiver()

    receiver.receive_message(
        0x100,
        {
            "rpm": 2000,
            "temperature": 30,
            "fuel_level": 90
        }
    )