#!/usr/bin/env python

# from pyxl320 import ServoSerial
from pyxl320 import Packet
# from pyxl320 import DummySerial
from pyxl320 import ServoSerial
import argparse


def handleArgs():
	parser = argparse.ArgumentParser(description='ping servos')
	parser.add_argument('-i', '--id', help='servo id', type=int, default=1)
	parser.add_argument('angle', help='servo angle', type=float)
	parser.add_argument('-p', '--port', help='serial port', type=str, default='/dev/tty.usbserial-A5004Flb')

	args = vars(parser.parse_args())
	return args


def main():
	args = handleArgs()

	ID = args['id']
	port = args['port']  # '/dev/tty.usbserial-A5004Flb'
	angle = args['angle']

	serial = ServoSerial(port)  # use this if you want to talk to real servos
	# serial = DummySerial(port)  # use this for simulation
	serial.open()

	pkt = Packet.makeServoPacket(ID, angle)  # move servo 1 to 158.6 degrees
	err_no, err_str = serial.sendPkt(pkt)  # send packet to servo
	if err_no:
		print('Oops ... something went wrong!: {}'.format(err_str))

if __name__ == '__main__':
	main()