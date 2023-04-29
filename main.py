import pygame
import pygame._sdl2.audio as sdl2_audio
import pygame.mixer as mixer

def get_devices(capture_devices: bool = False) -> tuple[str, ...]:
    init_by_me = not pygame.mixer.get_init()
    if init_by_me:
        pygame.mixer.init()
    devices = tuple(sdl2_audio.get_audio_device_names(capture_devices))
    if init_by_me:
        pygame.mixer.quit()
    return devices

print(get_devices())

# set output to 'CABLE Input (VB-Audio Virtual Cable)'
mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')

# on drag and drop
def drop_file(path):
    mixer.music.load(path)
    mixer.music.play()

# init pygame window
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Drag and drop a file on me to play the audio through your mic!')

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.DROPFILE:
            drop_file(event.file)
    pygame.display.update()