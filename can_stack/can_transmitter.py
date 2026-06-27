import time

from ecu_simulator.engine_ecu import EngineECU
from can_stack.can_driver import CANDriver
from can_stack.can_receiver import CANReceiver
from diagnostics.fault_monitor import FaultMonitor

monitor = FaultMonitor()

ecu = EngineECU()

driver = CANDriver()

receiver = CANReceiver()

while True:

    ecu.update()

    signals = ecu.read_signals()

    driver.send_message(
        0x100,
        signals
    )
     
    monitor.check_rpm(
    signals["rpm"]
)

    receiver.receive_message(
        0x100,
        signals
    )

    time.sleep(1)