from os import path
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

submissions = open('./data/cleaned_data.txt').read()

cloud = WordCloud(relative_scaling=.5, height=1024, width=760)
cloud.generate(submissions)

# write to file
cloud.to_file(path.join(path.dirname(__file__), "cloud.png"))

# show word cloud using matplotlib
plt.imshow(cloud)
plt.axis("off")
plt.show()
