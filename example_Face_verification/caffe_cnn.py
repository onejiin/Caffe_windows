import subprocess
import numpy as np

from function import *

__author__ = 'wjung'

# caffe usage : caffe.exe total_5layer.prototxt total_iter_21464.caffemodel image.jpg


def main(argv):

    INPUT_IMAGE = sys.argv[1]
    if os.path.exists(INPUT_IMAGE) == False:
        print 'check the correct input file'
        return -1
    cmd = 'caffe.exe ./car_siamese_test-leveldb_10layer.prototxt ./model/total_iter_222000.caffemodel ' + INPUT_IMAGE

    cmd_arg = cmd.split()
    result = subprocess.check_output(cmd_arg)
    result_list = result.split()
    for i in range(len(result_list)):
        result_list[i] = float(result_list[i])
    result_array = np.array(result_list)
    scale = np.ones(len(result_array)) * 256

    result = result_array / scale
    result = result.tolist()

    name = []
    score = []

    verification_face_all(result, name, score)

    print '=================================='
    for i in range(len(name)):
        print 'score :', round(score[i], 3), '-->', name[i]
    print '=================================='


if __name__ == '__main__':
    sys.path.append('config')
    sys.exit(main(sys.argv))
