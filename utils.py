import pyaudio

pa = pyaudio.PyAudio()
device_count = pa.get_device_count()

print("\n\nAvailable audio devices:")
for i in range(device_count):
    device_info = pa.get_device_info_by_index(i)
    device_name = device_info['name']
    device_index = device_info['index']
    print(f"Device {device_index}: {device_name}")

pa.terminate()