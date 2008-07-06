#!/usr/bin/python

import repidr_common
import errors
import util

import id800_ll

class ID800v2Radio(repidr_common.IcomRadio):
    BAUD_RATE = 9600

    _mmap = None
    _memories = []

    def _fetch_mmap(self):
        self._mmap = id800_ll.get_memory_map(self.pipe)
        self._memories = id800_ll.parse_map_for_memory(self._mmap)

    def get_memory(self, number, vfo=None):
        if not self._mmap:
            self._fetch_mmap()
        
        return self._memories[number]

    def get_memories(self, vfo=None):
        if not self._mmap:
            self._fetch_mmap()

        return self._memories

if __name__ == "__main__":
    import serial

    s = serial.Serial(port="/dev/ttyUSB0",
                      baudrate=9600,
                      timeout=1)

    r = ID800v2Radio(s)
    print r.get_memories()
