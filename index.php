<?php
include "config.php";
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A minimalistic way to cut your long videos into 15 seconds segments for whatsapp and instagram in windows, instead of cutting it manually.">
    <meta name="keywords" content="Whatsapp, instagram, cutter, video, status, stories, trim">
    <meta name="author" content="Kishor. A">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
    </link>
    <link rel="stylesheet" href="darkmode/dark-mode.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <title>Status Cutter</title>

    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
            ;
        }

        .accordion {
            background-color: #eee;
            color: #444;
            cursor: pointer;
            padding: 18px;
            width: 100%;
            border: 0.1px solid black;
            text-align: left;
            outline: none;
            font-size: 15px;
            transition: 1s;
            border-radius: 0.3rem 0.3rem 0 0;
        }

        .active,
        .accordion:hover {
            background-color: #ccc;
        }

        .panel {
            padding: 0 18px;
            display: none;
            color: black;
            background-color: #f2f2f2;
            overflow: hidden;
            border: 0.1px solid black;
            border-top-style: none;
            border-radius: 0 0 0.3rem 0.3rem;
            /* box-shadow: 4px 4px 20px #b3b3b3;        */
        }

        #button {
            display: flex;
            justify-content: center;
        }

        .inputFile {
            width: 0.1px;
            height: 0.1px;
            opacity: 0;
            overflow: hidden;
            position: absolute;
            z-index: -1;
        }

        #fileInput {
            margin: 2rem;
            display: flex;
            justify-content: space-evenly;
        }

        .inputFile+label {
            font-size: 1.25em;
            font-weight: 700;
            color: #404040;
            background-color: white;
            display: inline-block;
            padding: 0.5rem;
            border: 1px solid #404040;
            border-radius: 0.5rem;
        }

        .inputFile:focus+label,
        .inputFile+label:hover {
            background-color: #404040;
            color: white;
        }

        .inputFile:focus+label {
            outline: 1px dotted #000;
            outline: -webkit-focus-ring-color auto 5px;
        }

        #combineBtn {
            border: 1px solid #404040;
            padding: 0.5rem;
            border-radius: 0.4rem;
            font-weight: bold;
            background-color: white;
            font-size: 1.25rem;
            color: #404040;
        }

        #combineBtn:hover {
            background-color: #404040;
            color: white;
        }

        #combinep {
            display: flex;
            justify-content: center;
        }

        section {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            background: #000;
            pointer-events: none;
            animation: fadeout .5s linear forwards;
            animation-delay: 0.5s;
        }

        .loader {
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            background: white;
        }

        .count {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 15vw;
            color: #fff;
            font-weight: bold;
            mix-blend-mode: difference;
            text-align: center;
        }

        @keyframes fadeout {
            0% {
                opacity: 1;
            }

            100% {
                opacity: 0%;
            }
        }
    </style>

</head>

<body>
    <section>
        <div class="loader"></div>
        <div class="count"></div>
    </section>
    <script type="text/javascript" src="loading/jquery-3.6.0.js"></script>
    <script type="text/javascript">
        $(document).ready(function() {
            var count = 0;
            var counter = setInterval(function() {
                if (count <= 100) {
                    $('.count').text(count + '%');
                    $('.loader').css('width', count + '%');
                    count++;
                } else {
                    clearInterval(counter);
                }
            }, 50);
        });
    </script>
    <div class="container-fluid">
        <div class="topbar row bg-dark p-4">
            <div class="col-6 col-sm-6 col-lg-7 text-left font-weight-bold text-white align-self-center">
                <h1 style="font-size: 2.5rem;"><a href="index.php" style="text-decoration: none; color: white"> STATUS CUTTER</a></h1>
            </div>
            <div class="nav-link align-self-center">
                <div class="dm custom-control custom-switch">
                    <input type="checkbox" class="custom-control-input" id="darkSwitch">
                    <label class="custom-control-label text-white " for="darkSwitch"><?php echo $lang['theme'] ?></label>
                </div>
                <script src="darkmode/dark-mode-switch.min.js"></script>
            </div>
            <div class="col-3 col-sm-3 col-lg-1 text-center font-weight-bold text-white align-self-center">
                <button type="button" class="btn btn-light text-center btn-outline-light"><a href="https://github.com/k1sh0r/StatusCutter"><img src="git1.png" alt="GitHub" style="width:2rem;"></a></button>
            </div>
        </div>
    </div>
    <br><br><br>
    <div class="container">
        <h2><?php echo $lang['title'] ?></h2>
        <button class="accordion"><?php echo $lang['cut_title'] ?></button>
        <div class="panel p-5">
            <div class="col-lg-12 text-center">
                <h6 class="pl-3 pr-3"><?php echo $lang['cut_description'] ?></h6>
            </div>
            <div class="col-lg-12 text-center">

                <form action="cutter.py" enctype="multipart/form-data" method="post" class="form-inline row" name="cutForm">
                    <div class="input-group col-lg-12">

                        <div class="custom-file m-2">
                            <input type="file" name="filename" class="btn btn-dark custom-file-input " id="inputGroupFile01" aria-describedby="inputGroupFileAddon01">
                            <label class="custom-file-label border border-dark " for="inputGroupFile01"><?php echo $lang['cut_button1'] ?></label>
                        </div>
                        <div>
                            <select class="custom-select m-2" name="duration">
                                <option selected value="1"><?php echo $lang['cut_option1'] ?></option>
                                <option value="15"><?php echo $lang['cut_option2'] ?></option>
                                <option value="30"><?php echo $lang['cut_option3'] ?></option>
                                <option value="60"><?php echo $lang['cut_option4'] ?></option>
                            </select>
                        </div>
                        <div class="input-group-append m-2">
                            <button onclick="loader()" type="submit" class="btn btn-dark" id="inputGroupFileAddon01"><?php echo $lang['cut_button3'] ?></button>
                        </div>

                    </div>
                </form>

            </div>
        </div>
        <!-- ADDED NEW LINE OF CODES -->
        <!-- FOR COMBINING 2 Vids Feature-->
        <button class="accordion mt-2"><?php echo $lang['combine_title'] ?></button>
        <div class="panel p-5">
            <div id="combinep">
                <p><?php echo $lang['combine_description'] ?></p>
            </div>
            <div>
                <form action="combineVid.py" method="POST" enctype="multipart/form-data">
                    <div id="fileInput">
                        <input type="file" name="vidClip1" id="vidClip1" class="inputFile">
                        <label id="label1" for="vidClip1"><?php echo $lang['combine_button1'] ?></label>
                        <input type="file" name="vidClip2" id="vidClip2" class="inputFile">
                        <label id="label2" for="vidClip2"><?php echo $lang['combine_button2'] ?></label>
                    </div>
                    <div id="button">
                        <button type="submit" id="combineBtn"><?php echo $lang['combine_button3'] ?></button>
                    </div>
                </form>
            </div>
        </div>
        <!-- END -->

        <div class="row">

            <div class="col-lg-12 text-center" style="display: none; margin-top: -30px; margin-bottom: -30px" id="loading">
                <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js">
                </script>
                <lottie-player src="https://assets9.lottiefiles.com/packages/lf20_78Ybeg.json" background="transparent" speed="1" style="width: 300px; height: 300px; margin-left: auto;margin-right: auto" loop autoplay>
                </lottie-player>
            </div>

            <div class="col-lg-12 col-sm-12 text-center" style="display: none;" id="uploading">
                <h5 style="margin-left: auto;margin-right: auto">Uploading... please wait!</h5>
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

    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>

</body>
<script>
    function loader() {
        $("#loading").fadeIn();
        setTimeout(function() {
            $("#uploading").fadeIn();
        }, 1000);
    }

    window.addEventListener("pageshow", function(event) {
        var historyTraversal = event.persisted ||
            (typeof window.performance != "undefined" &&
                window.performance.navigation.type === 2);
        if (historyTraversal) {
            // Handle page restore.
            window.location.reload();
        }
    });

    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var panel = this.nextElementSibling;
            if (panel.style.display === "block") {
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }
        });
    }
    const inputs = document.querySelectorAll('.inputFile');
    console.log(inputs);
    const label1 = document.querySelector("#label1")
    console.log(label1)
    const label2 = document.querySelector("#label2")
    console.log(label2)
    let fileNames = [];
    for (let input of inputs) {
        input.addEventListener("change", function(event) {
            let uploadedFileName = event.target.files[0].name;
            fileNames.push(uploadedFileName);
            console.log(uploadedFileName);
            if (fileNames[0] != undefined) {
                label1.textContent = fileNames[0];
            }
            if (fileNames[1] != undefined) {
                label2.textContent = fileNames[1];
            }
        });
    }
</script>

</html>