import serial.tools.list_ports
import serial
import sys
import time

keycodes = [
    18, 19, 20, 21, 23, 22, 26, 28, 25
]

def list_serialports():
    ports = {}

    for index, p in enumerate(list(serial.tools.list_ports.comports())):
        print(f"{index + 1}: {p.device}")
        ports[index] = p.device

    print("シリアルポートを選択してください(番号を選んてEnterキーを押す)")
    target = int(input()) - 1
    return ports[target]

def write(path, serialport):
    with open(path, 'r') as f:                                                                                      
        data = f.read()
        print(data)
        f.close()

        ser = serial.Serial(serialport, 115200)
        ser.write(b'\x02')
        time.sleep(0.5)
        ser.write(data.encode())
        time.sleep(0.5)
        ser.write(b'\x03')

        ser.close()

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print("設定ファイルを指定してください")
        exit(0)

    serialport = list_serialports()

    write(args[1], serialport)






