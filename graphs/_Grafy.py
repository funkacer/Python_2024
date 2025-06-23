import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def rd(x,y=0):
    ''' A classical mathematical rounding by Voznica '''
    try:
        m = int('1'+'0'*y) # multiplier - how many positions to the right
        q = x*m # shift to the right by multiplier
        c = int(q) # new number
        i = int( (q-c)*10 ) # indicator number on the right
        if i >= 5:
            c += 1
        result = '{num:.{prec}f}'.format(num=c/m,prec=y)
    except:
        result = ''
    return result

def getBarChart(df, columns = [], kind='v', precision=0, normalize=False, reverse=False, total=False,
                title='', label='', width=0.8, rotation=0, figsize=(5, 5), file='', html=False):
    '''Tato funkce vytváří grafy s popisky hodnot'''
    if kind =='v' or kind =='vs' or kind =='h' or kind =='hs':
        # šaráda s cols je kvůli False, True v názvech sloupců (viz Titanic)
        cols = []
        if columns != []:
            for i, column in enumerate(columns):
                cols.append(df.columns.get_loc(column))
        else:
            for i, column in enumerate(df.columns):
                cols.append(df.columns.get_loc(column))
        
        df = df.iloc[:, cols]
        columns = df.columns
        if total:
            df.loc['Total'] = df.sum()
        if normalize:
            df = df.div(df.sum(axis=1), axis=0)*100
        if reverse:
            df = df[::-1]
        fig, ax = plt.subplots(figsize = figsize)
        rectss = []
        bottom = np.zeros(len(df))
        ticks = np.arange(len(df))  # the x/y ticks locations
        width1 = 0    # pro popisky
        if  kind =='v' or  kind =='h':
            width = width / len(columns) #0.25  # the width of the bars
            width1 = width/2*(len(columns)-1)
        multiplier = 0
        if kind =='v' or kind =='vs':
            for column in columns:
                offset = width * multiplier
                if kind =='vs':
                    rectss.append(ax.bar(x=ticks, height=df[column], bottom=bottom, width=width, label=column))
                elif kind =='v':
                    rectss.append(ax.bar(x=ticks + offset, height=df[column], width=width, label=column))
                multiplier += 1
                bottom += np.array(df[column])
            bottom = np.zeros(len(df))
            for rects in rectss:
                bott = []
                for i, rect in enumerate(rects):
                    if len(columns) == 1 or kind =='v':
                        ax.annotate(text=rd(rect.get_height(), precision), xy=(rect.get_x() + rect.get_width()/2, rect.get_height()), ha='center', va='bottom')
                    else:
                        ax.annotate(text=rd(rect.get_height(), precision), xy=(rect.get_x() + rect.get_width()/2, rect.get_height()/2 + bottom[i]), ha='center', va='center')
                    bott.append(rect.get_height())
                bottom += np.array(bott)
            if rotation > 0 and rotation < 90:
                ax.set_xticks(ticks + width1, df.index, rotation = rotation, rotation_mode='anchor', ha='right')
            else:
                ax.set_xticks(ticks + width1, df.index, rotation = rotation)
            ax.set_xlabel(df.index.name)
            ax.set_ylabel(label)
            #ax.set_xticks(x + width, species)
        if kind =='h' or kind =='hs':
            for column in columns:
                offset = width * multiplier
                if kind =='hs':
                    rectss.append(ax.barh(y=ticks, width=df[column], left=bottom, height=width, label=column))
                elif kind =='h':
                    rectss.append(ax.barh(y=ticks + offset, width=df[column], height=width, label=column))
                multiplier += 1
                bottom += np.array(df[column])
            bottom = np.zeros(len(df))
            for rects in rectss:
                bott = []
                for i, rect in enumerate(rects):
                    if len(columns) == 1 or kind =='h':
                        ax.annotate(text=rd(rect.get_width(),precision), xy=(rect.get_width(), rect.get_y()+rect.get_height()/2), ha='left', va='center')
                    else:
                        ax.annotate(text=rd(rect.get_width(),precision), xy=(rect.get_width()/2+bottom[i], rect.get_y()+rect.get_height()/2), ha='center', va='center')
                    bott.append(rect.get_width())
                bottom += np.array(bott)
            if rotation > 0 and rotation < 90:
                ax.set_yticks(ticks + width1, df.index, rotation = rotation, rotation_mode='anchor', ha='right')
            else:
                ax.set_yticks(ticks + width1, df.index, rotation = rotation, va='center')
            ax.set_xlabel(label)
            ax.set_ylabel(df.index.name)
        ax.legend(title=df.columns.name, loc='upper center', bbox_to_anchor=(1.1, 1), ncol=1, fancybox=True, shadow=True)
        ax.set_title(title)
        if file != '':
            fig.savefig(file, dpi=fig.dpi, bbox_inches='tight')
        if html:
            buf = BytesIO()
            fig.savefig(buf, format="png", bbox_inches='tight')
            # Embed the result in the html output.
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            return f"<img src='data:image/png;base64,{data}'/>"
    else:
        raise Exception("Sorry, wrong type(only accept 'h', 'hs', 'v', 'vs')")