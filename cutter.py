#!C:\Python39\python.exe
from moviepy.editor import *
from datetime import datetime
import cgi
import os
import cgitb
print("Content-Type: text/html\n\n")
print("""<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="A minimalistic way to cut your long videos into 15 seconds segments for whatsapp and instagram in windows, instead of cutting it manually.">
        <meta name="keywords" content="Whatsapp, instagram, cutter, video, status, stories, trim">
        <meta name="author" content="Kishor. A">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"></link>
        <link rel="stylesheet" href="darkmode/dark-mode.css">
        <title>Status Cutter</title>
    </head>
    <body>
        <div class="container-fluid">
            <div class="topbar row bg-dark p-4">
                <div class="col-6 col-sm-6 col-lg-7 text-left font-weight-bold text-white align-self-center">
                    <h1 style="font-size: 2.5rem;"><a href="index.php" style="text-decoration: none; color: white"> STATUS CUTTER</a></h1>
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
        <br>
        <br>
        <br>
        <div class='container'>
        <div style="display: none;">""")
cgitb.enable()


def cutvid(duration, videoClip):
    cuts = videoClip.duration/duration
    cuts = int(cuts)
    # print(cuts)
    subclips = []

    def st(value):
        x = value*duration
        return x

    def et(value):
        x = value+1
        x = x*duration
        return x
    for i in range(0, cuts):
        subclips.append(videoClip.subclip(st(i), et(i)))
        subclips[i].write_videofile(
            "downloads/" + clipname + str(i+1) + '.mp4')
        print(subclips[i].duration)

    subclips.append(videoClip.subclip(st(cuts), videoClip.duration))
    print(subclips[cuts].duration)
    subclips[cuts].write_videofile(
        "downloads/" + clipname + str(cuts+1) + '.mp4')
    print("""</div><div class='row'>""")
    for i in range(0, cuts+1):
        print("""<div class="col-lg-12 text-center" style="padding-bottom: 10px;padding-top: 10px;"><button type="button" class="btn btn-dark"><a class="text-white" href='downloads/%s%s.mp4' download> Download - %s</a></button></div>""" % (clipname, i+1, i+1))

    print("""
                    <div class='col-lg-12 col-sm-12'>
                    <div class="text-center mt-5"><button onclick="window.history.go(-1); return false;" class="btn btn-dark">Go back</button>
                    </div>
                    </div>
                    </div>
                    <div>
                        <nav class="navbar topbar fixed-bottom row bg-dark p-1">
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
                <body>
            </html>""")


form = cgi.FieldStorage()
# Get filename here.
fileitem = form['filename']
allowed_extensions = ['mp4']
dur = int(form.getvalue("duration"))

# Test if the file was uploaded

if fileitem.filename and fileitem.filename[-3:] in allowed_extensions:
    if dur > 1:
        # strip leading path from file name to avoid
        fn = os.path.basename(fileitem.filename)
        open('uploads/' + fn, 'wb').write(fileitem.file.read())
        message = 'The file "' + fn + '" was uploaded successfully'
        datentime = datetime.now()
        clipname = datentime.strftime("%d%m%H%M%S%f")

        print(fn)
        fn = str("uploads/"+fn)
        clip = VideoFileClip(fn)
        cutvid(dur, clip)
    else:
        print("""
                        </div>
                        <div class='row'><div class="col-lg-12 text-center">
                            <h3>Please input segments duration</h3></div><div class='mt-3 col-lg-12 col-sm-12'>                    
                                <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
                                <lottie-player src="retry.json"  background="transparent"  speed="1"  style="width: 300px; height: 300px; margin-left: auto;margin-right: auto"  loop  autoplay>
                                </lottie-player><div class='row'><div class='col-lg-12 col-sm-12'><div class="text-center"><button onclick="window.history.go(-1); return false;" class="btn btn-dark">Go back</button>
                        </div>
                        </div>
                        </div>
                        </div>
                        </div>
                        <div>
                            <nav class="navbar topbar fixed-bottom row bg-dark p-1">
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
                    <body>
                </html>""")


else:
    print("""
                        </div>
                        <div class='row'><div class="col-lg-12 text-center">
                            <h3>Please upload a .mp4 video file</h3></div><div class='mt-3 col-lg-12 col-sm-12'>                    
                                <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
                                <lottie-player src="retry.json"  background="transparent"  speed="1"  style="width: 300px; height: 300px; margin-left: auto;margin-right: auto"  loop  autoplay>
                                </lottie-player><div class='row'><div class='col-lg-12 col-sm-12'><div class="text-center"><button onclick="window.history.go(-1); return false;" class="btn btn-dark">Go back</button>
                        </div>
                        </div>
                        </div>
                        </div>
                        </div>
                        <div>
                            <nav class="navbar topbar fixed-bottom row bg-dark p-1">
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
                    <body>
                </html>""")
