class CANDriver:

    def send_message(self, message_id, data):

        print(
            f"CAN ID={hex(message_id)} DATA={data}"
        )


if __name__ == "__main__":

    driver = CANDriver()

    driver.send_message(
        0x100,
        {"rpm": 1500}
    )