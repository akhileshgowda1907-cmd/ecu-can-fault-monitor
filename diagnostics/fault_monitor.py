class FaultMonitor:

    def check_rpm(self, rpm):

        if rpm > 4000:
            print("FAULT: RPM TOO HIGH")
        else:
            print("RPM NORMAL")


if __name__ == "__main__":

    monitor = FaultMonitor()

    print("Testing Fault Monitor...\n")

    monitor.check_rpm(3500)

    monitor.check_rpm(4500)