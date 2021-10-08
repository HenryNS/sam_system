from __future__ import print_function
from array import array
import time
import os
import sys
import libtiepie
sys.executable 
libtiepie.network.auto_detect_enabled = True
libtiepie.device_list.update()


scp = None
for item in libtiepie.device_list:
    if item.can_open(libtiepie.DEVICETYPE_OSCILLOSCOPE):
        scp = item.open_oscilloscope()
        if (scp.measure_modes & libtiepie.MM_BLOCK) and (scp.segment_count_max > 1):
            break
        else:
            scp = None
if scp:
    try:

        scp.measure_mode = libtiepie.MM_BLOCK
        scp.sample_frequency = 200e6  # 1 MHz
        scp.record_length = 3000  # 1000 samples
        scp.pre_sample_ratio = 0  # 0 %
        scp.segment_count = 5  # 5 segments
        for ch in scp.channels:
            ch.enabled = False

     
        ch = scp.channels[0]  # Ch 1
        ch.enabled = True
        ch.range = 8  # 8 V
        ch.coupling = libtiepie.CK_DCV  # DC Volt
        scp.trigger_time_out = 0  # 100 ms:
        for ch in scp.channels:
            ch.trigger.enabled = False

        ch = scp.channels[0]  # Ch 1
        ch.trigger.enabled = True
        ch.trigger.kind = libtiepie.TK_RISINGEDGE  # Rising edge

        ch.trigger.levels[0] = 0.5  # 50 %
        ch.trigger.hystereses[0] = 0.05  # 5 %

        for i in range(125):
        
            scp.start()

            # Wait for measurement to complete:
            while not scp.is_data_ready:
                time.sleep(0.01)  # 10 ms delay, to save CPU time

            # Create data arrays,
            data = []

            # Get all data from the scope:
            while scp.is_data_ready:
                data.append(scp.get_data()[0])  # only collect data from Ch 1

            # Output CSV data:
            csv_file = open(f'filename_{i}.csv', 'w')
            try:
                csv_file.write('Sample')
                for i in range(len(data)):
                    csv_file.write(';Segment ' + str(i + 1))
                csv_file.write(os.linesep)
                for i in range(len(data[0])):
                    csv_file.write(str(i))
                    for j in range(len(data)):
                        csv_file.write(';' + str(data[j][i]))
                    csv_file.write(os.linesep)

                print()
                print('Data written to: ' + csv_file.name)

            finally:
                csv_file.close()

    except Exception as e:
        print('Exception: ' + e.message)
        sys.exit(1)

    # Close oscilloscope:
    del scp

else:
    print('No oscilloscope available with block measurement and segmented trigger support!')
    sys.exit(1)

sys.exit(0)
