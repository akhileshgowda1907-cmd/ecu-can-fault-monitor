import time

from ecu_simulator.engine_ecu import EngineECU
from can_stack.can_driver import CANDriver

ecu = EngineECU()
driver = CANDriver()

print("Starting ECU Simulation...\n")

for i in range(10):
    ecu.update()
    signals = ecu.read_signals()
    driver.send_message(0x100, signals)
    time.sleep(1)