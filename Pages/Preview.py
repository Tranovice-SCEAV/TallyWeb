from Config import *
import time

current_time = time.strftime("%H : %M")

web = f'''
<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    <meta http-equiv="refresh" content="0.75">
</head>
<body style="background-color:#79e83e;">
    <div class="row">
        <div class="col">
            <p class="text-start fs-1">Source: {SOURCE}</p>
        </div>
        <div class="col">
            <p class="text-center fs-1 border border-dark border-3 rounded-pill bg-success bg-success">PREVIEW</p>
        </div>
        <div class="col">
            <p class="text-end fs-1">{current_time}</p>
            <p class="text-end fs-1">{PROGRAM}</p>
        </div>
    </div>
</body>
</html>
'''