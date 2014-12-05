__author__ = 'davide'

from nltk.metrics.agreement import AnnotationTask

#
# In defining the AnnotationTask class, we use naming conventions similar to the
# paper's terminology.  There are three types of objects in an annotation task:
#
# the coders (variables "c" and "C")
#     the items to be annotated (variables "i" and "I")
#     the potential categories to be assigned (variables "k" and "K")
#
# The simplest way to initialize an AnnotationTask is with a list of triples,
# each containing a coder's assignment for one object in the task:
#
#     task = AnnotationTask(data=[('c1', '1', 'v1'),('c2', '1', 'v1'),...])
data = []


def appender(annotator, line):
    word = line[:-3]

    '''
    if ('0' in line):
        print((annotator,word,'0'))
        data.append((annotator,word,'0'))
    if ('1' in line):
        data.append((annotator,word,'1'))
    if ('2' in line):
        data.append((annotator,word,'2'))
    '''

    if ('0' in line):
        print((annotator, word, '0'))
        data.append((annotator, '0', word))
    if ('1' in line):
        data.append((annotator, '1', word))
    if ('2' in line):
        data.append((annotator, '2', word))


with open("annotd") as d:
    content = d.readlines()
    for line in content:
        appender('d', line)

with open("annots") as d:
    content = d.readlines()
    for line in content:
        appender('s', line)

with open("annots") as d:
    content = d.readlines()
    for line in content:
        appender('k', line)

task = AnnotationTask(data)
#print(task.avg_Ao())

print(task.kappa())
