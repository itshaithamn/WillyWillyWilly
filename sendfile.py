import freewili
from freewili.serial_util import find_all
from freewili.types import FreeWiliProcessorType

# Find the first Main Processor.
first_device = freewili.find_all(FreeWiliProcessorType.Main)[0]
# Send the file to the Main Processor.
first_device.send_file("my_script.wasm", "/scripts/my_script.wasm").unwrap()