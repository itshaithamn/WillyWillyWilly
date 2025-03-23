import freewili
from freewili.serial_util import find_all
from freewili.types import FreeWiliProcessorType

# Find the first Main Processor.
first_device = freewili.find_all(FreeWiliProcessorType.Main)[1]
# Send the file to the Main Processor.
first_device.send_file("willy.wav", "/sounds/willy.wav").unwrap()

# #    from freewili.serial_util import find_all
#     from freewili.types import FreeWiliProcessorType
#
#     # Find the first Main Processor.
#     first_device = freewili.find_all(FreeWiliProcessorType.Main)[0]
#     # Send the file to the Main Processor.
#     input(f"WARNING: This will force the processor for {first_device} into UF2 bootloader, press any key to continue...")
#     first_device.reset_to_uf2_bootloader().unwrap()