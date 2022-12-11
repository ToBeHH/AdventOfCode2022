# -*- coding: utf-8 -*-
# Nice looking progress bar
# inspired by https://stackoverflow.com/questions/6169217/replace-console-output-in-python
# and https://stackoverflow.com/questions/3160699/python-progress-bar

import sys


def progressbar(howmany, bar_len=50, title='Please wait', out=sys.stdout):
    for index in range(howmany):
        yield index
        percent_done = (index + 1) / howmany * 100
        percent_done = round(percent_done, 1)

        done = round(percent_done / (100 / bar_len))
        togo = bar_len - done

        done_str = '█' * int(done)
        togo_str = '░' * int(togo)

        print(f'⏳ {title}: [{done_str}{togo_str}] {percent_done}% done', end='\r', file=out, flush=True)

    print('✅ ', file=out, flush=True)
