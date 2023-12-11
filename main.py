import subprocess

packageName = "org.videolan.vlc"
activityName = "org.videolan.vlc.gui.video.VideoPlayerActivity"

command = f"am start -n {packageName}/{activityName}"


subprocess.run(command, shell=True)


