from pydub import AudioSegment

def compress_mp3(input_file, output_file, bitrate='64k'):
    try:
      audio = AudioSegment.from_mp3(input_file)
      audio.export(output_file, format="mp3", bitrate=bitrate)
    except:
      print("Error: Failed to compress MP3 file.")

if __name__ == '__main__':
  input_file = 'input.mp3'
  output_file = './your_output.mp3'
  compress_mp3(input_file, output_file)