from pyModbusTCP.client import ModbusClient
import struct

c = ModbusClient(host="10.50.174.51", port=502, unit_id=20, auto_open=True)
regs = c.read_holding_registers(3111, 2)

print(struct.unpack('!f', bytes.fromhex('{0:02x}'.format(regs[0]) + '{0:02x}'.format(regs[1]))))

if regs:
    print(regs)

    #print(locals())
else:
    print("read error")