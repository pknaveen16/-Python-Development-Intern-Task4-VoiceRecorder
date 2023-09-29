import sounddevice as sd
import wave

def record_audio(filename, duration):
  """Records audio from the microphone and saves it to a file.

  Args:
    filename: The name of the file to save the audio to.
    duration: The duration of the recording in seconds.
  """

  # Create a wave file object.
  wf = wave.open(filename, "wb")

  # Set the wave file parameters.
  wf.setnchannels(1)
  wf.setsampwidth(2)
  wf.setframerate(44100)

  # Start recording.
  recording = sd.rec(int(duration * 44100), samplerate=44100, channels=1)

  # Write the recording to the wave file.
  wf.writeframes(recording)

  # Stop recording.
  sd.stop()

if __name__ == "__main__":
  # Get the filename to save the recording to.
  filename = input("Enter the filename to save the recording to: ")

  # Get the duration of the recording in seconds.
  duration = int(input("Enter the duration of the recording in seconds: "))

  # Record the audio.
  record_audio(filename, duration)

  # Print a message to the user.
  print("Recording saved to {}".format(filename))
