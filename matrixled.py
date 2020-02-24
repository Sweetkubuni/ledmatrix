import serial

class Block:

  def __init__(self, blocknum, x_offset):
    self._block_num = blocknum
    self._x_offset = x_offset
    self._blocks = [0 for i in range (64)]

  def flush(self, serial_port):
    for row in range(8):
      msg = []
      msg.append('B')
      msg.append(str(self._block_num))
      msg.append('R')
      msg.append(str(row))
      msg.append('C')
      value = 0
      for col in range (8):
        if self._blocks[col + row*8]:
          value = value | (1 <<  col)
      msg.append(chr(value))
      msg.append(';')
      msg = ''.join(msg)
      serial_port.write(msg)

  def set_column(self, row_blocks, column = 7):
    if blocks == None:
      return
    else:
      for row in range(8):
        self._blocks[7] = row_blocks[row]

  def shift_columns(self):




