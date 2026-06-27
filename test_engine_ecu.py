from ecu_simulator.engine_ecu import EngineECU

def test_engine_ecu():

    ecu = EngineECU()

    signals = ecu.read_signals()

    assert "rpm" in signals

    assert "temperature" in signals

    assert "fuel_level" in signals
    