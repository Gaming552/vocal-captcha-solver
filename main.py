import speech_recognition as sr, os

class VocalCaptchaModule:
    def __init__(self
        self.recognizer = sr.Recognizer()

    def recognize_audio_captcha(self, audio_file_path):
        """
        Recognize text from an audio captcha file.

        :param audio_file_path: Path to the audio captcha file.
        :return: The recognized text from the audio captcha.
        """
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio_data = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")
            return None


if __name__ == "__main__":
    captcha_module = VocalCaptchaModule()
    audio_file_path = sys.argv[1]
    captcha_text = captcha_module.recognize_audio_captcha(audio_file_path)

    if captcha_text:
        print(f"Recognized text: {captcha_text}")
    else:
        print("Failed to recognize the captcha text.")
