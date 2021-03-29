#!C:\Python39\python.exe
import cgitb
import os
import cgi
import glob
from conf import INPUTSDIR, OUTPUTSDIR
from moviepy.editor import *
print("Content-Type: text/html\n\n")
cgitb.enable()

# METHODS
# combining the vid clips


def combineVid(vidClips, outputDir, fileName="combinedVid.mp4"):
    if fileName[-3:] != "mp4":
        fileName = fileName + ".mp4"
    idx = 1
    tempClip = vidClips[0]
    while idx < len(vidClips):
        tempClip = concatenate_videoclips([tempClip, vidClips[idx]])
        idx += 1
    outputPath = os.path.join(outputDir, fileName)
    tempClip.write_videofile(outputPath)


#print("<h1>COMBINING @ VIDEO ????</h1>")
print("""<html><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="A minimalistic way to cut your long videos into 15 seconds segments for whatsapp and instagram in windows, instead of cutting it manually.">
<meta name="keywords" content="Whatsapp, instagram, cutter, video, status, stories, trim">
<meta name="author" content="Kishor. A">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"></link>
<link rel="stylesheet" href="darkmode/dark-mode.css">
<title>Status Cutter</title>
</head><body><div class="container-fluid">
        <div class="topbar row bg-dark p-4">
            <div class="col-6 col-sm-6 col-lg-7 text-left font-weight-bold text-white align-self-center">
                <h1 style="font-size: 2.5rem;"> <a href="index.php" style="text-decoration: none; color: white"> STATUS CUTTER</a></h1>
            </div>
            <div class="nav-link align-self-center">
                <div class="dm custom-control custom-switch">
                  <input type="checkbox" class="custom-control-input" id="darkSwitch">
                  <label class="custom-control-label text-white " for="darkSwitch">Dark Mode</label>
                </div>
                <script src="darkmode/dark-mode-switch.min.js"></script>
            </div>
            <div class="col-3 col-sm-3 col-lg-1 text-center font-weight-bold text-white align-self-center">
                <button type="button" class="btn btn-light text-center btn-outline-light"><a href="https://github.com/k1sh0r/StatusCutter"><img src="git1.png" alt="GitHub" style="width:2rem;" ></a></button>
            </div>
        </div>
    </div>
    </div><br><br><br><div class='container'>
    <div style="display: none;">""")
# PATH
# test 1 #
# print(INPUTSDIR)
# print(OUTPUTSDIR)

# TAKING VIDCLIPS
form = cgi.FieldStorage()
vid1 = form["vidClip1"]
vid2 = form["vidClip2"]
filename = "combinedVid.mp4"

if vid1.filename[-3:] != "mp4" or vid2.filename[-3:] != "mp4":
    #print("""<h1>INVALID FILE, ENTER mp4 file</h1>""")
    print("""</div><div class='row'><div class="col-lg-12 text-center"><h3>Please upload a .mp4 video file</h3></div><div class='mt-3 col-lg-12 col-sm-12'>                    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js">
                </script>
                <lottie-player src="retry.json"  background="transparent"  speed="1"  style="width: 300px; height: 300px; margin-left: auto;margin-right: auto"  loop  autoplay>
                </lottie-player><div class='row'><div class='col-lg-12 col-sm-12'><div class="text-center"><button onclick="window.history.go(-1); return false;" class="btn btn-dark">Go back</button></div></div>
            </div></div></div>
            <div>
            <nav class="navbar topbar fixed-bottom row bg-dark p-1">
                <div class="btn-group dropup col-3 col-sm-3 col-lg-1 mr-sm-2 my-2 my-lg-0 text-center font-weight-bold text-white align-self-right">
                    <button type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <?php echo $lang['lang_option'] ?>
                    </button>
                    <div class="dropdown-menu">
                        <a class="dropdown-item" href="index.php?lang=en" class="en">English</a>
                        <a class="dropdown-item" href="index.php?lang=id" class="id"><?php echo $lang['lang_id'] ?></a>
                    </div>
                </div>
            </nav>
            </div><body></html>""")
else:
    fnVid1 = "1.mp4"
    fnVid2 = "2.mp4"

    open('inputs/' + fnVid1, 'wb').write(vid1.file.read())
    open('inputs/' + fnVid2, 'wb').write(vid2.file.read())

    # INPUT PATH
    sourceDir = INPUTSDIR

    # Output Path
    outputPath = os.path.join(OUTPUTSDIR, "combinedVid.mp4")

    # taking vids from inputs DIR
    filesPath = []
    for folder, subfolders, files in os.walk(sourceDir):
        for fname in files:
            tempPath = os.path.join(sourceDir, fname)
            filesPath.append(tempPath)
    # test 2 #
    # print("<script>console.log('{}')</script>".format(len(filesPath)))

    # opening the vid clips
    vidClips = []
    for path in filesPath:
        tempClip = VideoFileClip(path)
        vidClips.append(tempClip)

    # test 3 #
    # print("<script>console.log('vidclips:{}')</script>".format(len(vidClips)))

    '''
    COMBINING THE CLIPS
    '''
    combineVid(vidClips, OUTPUTSDIR)

    # test 4 #
    # print("<script>console.log('{}')</script>".format(os.path.basename(vid1.filename)))
    # print("<script>console.log('{}')</script>".format(os.path.basename(vid2.filename)))
    # vidClips = [vid1, vid2]

    '''
    EPILOG
    '''
    # print("<h1>{}</h1>".format(vid1.filename))
    # print("<h1>{}</h1>".format(vid2.filename))
    print("""</div><div class='row'>""")
    print("""<div class="col-lg-12 text-center" style="padding-bottom: 10px;padding-top: 10px;"><a href='http://localhost/statusCutter/outputs/{}' class="btn btn-dark" download>DOWNLOAD</a></div></div>""".format(filename))
    print("""<div class="text-center mt-5"><button onclick="window.history.go(-1); return false;" class="btn btn-dark">Go back</button>
                    </div>""")
    # closing the vid clips
    for clip in vidClips:
        clip.close()
    # deleting the vid clips
    for folder, suubfolders, files in os.walk(INPUTSDIR):
        for fname in files:
            os.remove(os.path.join(INPUTSDIR, fname))

    print("""<nav class="navbar topbar fixed-bottom row bg-dark p-1">
                <div class="btn-group dropup col-3 col-sm-3 col-lg-1 mr-sm-2 my-2 my-lg-0 text-center font-weight-bold text-white align-self-right">
                    <button type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <?php echo $lang['lang_option'] ?>
                    </button>
                    <div class="dropdown-menu">
                        <a class="dropdown-item" href="index.php?lang=en" class="en"><?php echo $lang['lang_en'] ?></a>
                        <a class="dropdown-item" href="index.php?lang=id" class="id"><?php echo $lang['lang_id'] ?></a>
                    </div>
                </div>
            </nav>
            </div>
            <body></html>""")
