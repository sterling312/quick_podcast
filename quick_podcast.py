import logging
import sys
import tempfile
import wave
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from pydub import AudioSegment

logger = logging.getLogger(__name__)

def main(textfile: str, audiofile: str, speaker1: str = 'v2/en_speaker_9', speaker2: str = 'v2/en_speaker_2'):
    with open(textfile) as fh:
        lines = fh.readlines()[1:-1:3]
        sound = None
        for txt1, txt2 in zip(lines[::2], lines[1::2]):
            host1 = generate_audio(txt1, history_prompt=speaker1)
            host2 = generate_audio(txt2, history_prompt=speaker2)
            with tempfile.TemporaryDirectory() as tmp:
                logger.debug(f'tempdir {tmp}')
                logger.info(f'{txt1}')
                write_wav(f'{tmp}/host1.wav', SAMPLE_RATE, host1)
                sound1 = AudioSegment.from_wav(f'{tmp}/host1.wav')
                logger.info(f'{txt2}')
                write_wav(f'{tmp}/host2.wav', SAMPLE_RATE, host2)
                sound2 = AudioSegment.from_wav(f'{tmp}/host2.wav')
                combined_sounds = sound1 + AudioSegment.silent(duration=1000) + sound2
                if sound is None:
                    sound = combined_sounds
                else:
                    sound += combined_sounds
            sound.export(audiofile, format='wav')

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    main(*sys.argv[1:])
