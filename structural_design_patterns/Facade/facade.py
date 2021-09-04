# These are some of the classes of a complex 3rd-party video
# conversion framework. We don't control that code, therefore
# can't simplify it.

class VideoFile:
	def __init__(self, name) -> None:
		self.name = name


class GreyScaleVideo:
	def grey_scale(self, video_file: VideoFile):
		print(f"Adding GreyScale to the video {video_file.name}")


class MPEG4Compression:
	def compress(self, video_file: VideoFile):
		print(f"Compressing video file {video_file.name}")


class FPSAjust:
	def adjust_fps(self, video_file: VideoFile, fps: int):
		print(f"Adjusting FPS of video file {video_file.name} to {fps} Hz")


class AudioMixer:
	def add_audio(self, video_file: VideoFile):
		print(f"Adding audio to video file {video_file.name}")


# We create a facade class to hide the framework's complexity
# behind a simple interface. It's a trade-off between
# functionality and simplicity.
class VideoConverter:
	@staticmethod
	def convert(filename, format):
		file = VideoFile(filename)

		mpeg4convertor = MPEG4Compression()

		if (format == "mp4"):
			mpeg4convertor.compress(file)

		fpsadjustor = FPSAjust()
		fpsadjustor.adjust_fps(file, 120)

		audio = AudioMixer()
		audio.add_audio(file)

# Application classes don't depend on a billion classes
# provided by the complex framework. Also, if you decide to
# switch frameworks, you only need to rewrite the facade class.

if __name__ == "__main__":
	convertor = VideoConverter()
	convertor.convert("facade-pattern-intro.mp4", "mp4")