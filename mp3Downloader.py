import youtube_dl
import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from mainUI import Ui_MainWindow
from PyQt5.QtWidgets import QDialog, QApplication

ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}

ydlmp4_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp4',
		'preferredquality': '192',
	}],
}

class Youtube_mp3(QDialog, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

	def eventDownload(self):
		self.download(ydl_opts)

	def eventDownloadmp4(self):
		self.download(ydlmp4_opts)

	def download(self,opts):
		URL = self.ui.urlEdit.text()
		
		try:
			with youtube_dl.YoutubeDL(opts) as ydl:
				ydl.download([URL])
			self.ui.urlEdit.clear()
		
		except Exception as e:
			self.ui.urlEdit.clear()
			pass

if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = Youtube_mp3()
	win.show()
	sys.exit(app.exec_())
	
