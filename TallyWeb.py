# ─── IMPORTS ────────────────────────────────────────────────────────────────────
import PyATEMMax, web, time
from Config import *
from Pages import Nothing, OnAir, Preview

# ─── ATEM CONFIG AND SETUP ──────────────────────────────────────────────────────
switcher = PyATEMMax.ATEMMax()

switcher.connect(SWITCHERIP)
switcher.waitForConnection()

last_tally_str = str(switcher.tally.bySource.flags[SOURCE])

# ─── WEB CONFIG AND SETUP ───────────────────────────────────────────────────────
urls = ('/(.*)', 'TallyWeb', 'Select')

app = web.application(urls, globals())

# ─── WEB CODE AND STATUS DETECTION ──────────────────────────────────────────────
class TallyWeb:
    def GET(self, name):
        #Status Detection
        tally_str = str(switcher.tally.bySource.flags[SOURCE])

        #Clock
        current_time = time.strftime("%H : %M")

        #Web sorter
        if tally_str == "[PGM]":
            return f'''{OnAir.web}'''
        elif tally_str == "[PVW]":
            return f'''{Preview.web}'''
        elif tally_str == "[]":
            return f'''{Nothing.web}'''

# ─── RUN THE WEBSITE ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run()