import multiprocessing
import time

from hvl_ccb.dev.fluke884x import Fluke8845a, Fluke8845aTelnetCommunication, Fluke8845aTelnetCommunicationConfig, \
    Fluke8845aConfig, MeasurementFunction

def connection(ip: str):
    fluke_com_conf = Fluke8845aTelnetCommunicationConfig(host=ip)
    fluke_com = Fluke8845aTelnetCommunication(fluke_com_conf)
    dev_conf = Fluke8845aConfig('Fluke1')
    dev = Fluke8845a(com=fluke_com, dev_config=dev_conf)
    dev.start()
    return dev


# dev.measurement_function = MeasurementFunction.VOLTAGE_DC
# print(dev.measure())
# dev.stop()