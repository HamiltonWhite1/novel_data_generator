from hashlib import new
import random
import pandas as pd
from book import i_robot

#instantiate a dictionary with all of the chapters in the novel
i_robot_chapters = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
}

#generating a while loop to append random lines to random chapters
lines_per_book = 0
while lines_per_book <= 7431:
    for line in i_robot:
        chapter = random.choice(i_robot_chapters)
        line_for_chapter = random.choice(i_robot)
        if line_for_chapter in chapter:
            pass
        else:
            chapter.append(line_for_chapter)
        lines_per_book += 1

#setting up the new Pandas DF. orient parameter needs to be set to index and the DF needs to be transposed to avoid the ValueError of arrays not being the same length
new_dataframe = pd.DataFrame.from_dict(i_robot_chapters, orient='index')
new_dataframe = new_dataframe.transpose()

#writing the new csv file to start your ETL process
new_dataframe.to_csv("practice_csv.csv", index=False)