from mq7 import MQ7

MQ7(0,3.3)

print("Value of carbon monoxide value: ",MQ7.getPPM())
print("The resistance ratio: ",MQ7.getRatio())
print("The sensor resistance: ",MQ7.getSensorResistance())