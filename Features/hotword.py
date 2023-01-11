# Clap detection script
# Used OOPS
# Modules
import pyaudio
import struct
import math

# Variables
INITIAL_TAP_THRESHOLD = 0.1
FORMAT = pyaudio.paInt16
SHORT_NORMALIZE = 1.0/32768.0
CHANNELS = 2
RATE = 44100
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE * INPUT_BLOCK_TIME)
OVERSENSITIVITY = 15.0/INPUT_BLOCK_TIME
UNDERSENSITIVITY = 120.0/INPUT_BLOCK_TIME
MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME

# Get RMS function
def get_rms(block):

    count = len(block)/2
    format = "%dh" % (count)
    shorts = struct.unpack(format, block)
    sum_squares = 0.0

    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt(sum_squares / count)

# Clapper class
class clapper(object):

    # Initializing
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        self.noisycount = MAX_TAP_BLOCKS+1
        self.quietcount = 0
        self.errorcount = 0

    # Closing the stream
    def stop(self):
        self.stream.close()

    # Opening mic stream
    def open_mic_stream(self):
        device_index = 2
        stream = self.pa.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, input_device_index=device_index, frames_per_buffer=INPUT_FRAMES_PER_BLOCK)
        return stream

    # Listen function
    def listen(self):

        # Try catch
        try:
            block = self.stream.read(INPUT_FRAMES_PER_BLOCK)

        except IOError as e:
            self.errorcount += 1
            print("(%d) Error recording: %s" % (self.errorcount, e))
            self.noisycount = 1
            return

        amplitude = get_rms(block)

        if amplitude > self.tap_threshold:
            self.quietcount = 0
            self.noisycount += 1
            if self.noisycount > OVERSENSITIVITY:

                self.tap_threshold *= 1.1
        else:

            if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
                return "True-Mic"
            self.noisycount = 0
            self.quietcount += 1
            if self.quietcount > UNDERSENSITIVITY:
                self.tap_threshold *= 2

# Tester function
def clap():
    tt = clapper()
    while True:
        kk = tt.listen()
        if "True-Mic" == kk:
            # >>> Clap detected! <<<
            print(">>> Clap Detected <<<")
            break
