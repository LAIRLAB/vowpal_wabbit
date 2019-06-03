import os
import time
import numpy as np
#from IPython import embed


#for shot in available_shots.iterkeys():
print("## perform experiments on aloi ##")
num_of_classes = 1000
leaf_example_multiplier = 10
shots = 100
lr = 0.001
bits = 29
alpha = 0.1 #0.3
passes = 1  #3 #5
use_oas = 0
dream_at_update = 0
learn_at_leaf = 1 #turn on leaf at leaf actually works better
loss = "squared"
dream_repeats = 20 #3
online = 1
#random_seed = 4000

tree_node = int(2*passes*(num_of_classes*shots/(np.log(num_of_classes*shots)/np.log(2)*leaf_example_multiplier)));

train_data = "aloi_train.vw"
test_data = "aloi_test.vw"
if os.path.exists(train_data) is not True:
        os.system("wget http://kalman.ml.cmu.edu/wen_datasets/{}".format(train_data))
if os.path.exists(test_data) is not True:
        os.system("wget http://kalman.ml.cmu.edu/wen_datasets/{}".format(test_data))


saved_model = "{}.vw".format(train_data)

print("## Training...")
start = time.time()
os.system("../../build/vowpalwabbit/vw {} --memory_tree {} --learn_at_leaf {} --max_number_of_labels {} --dream_at_update {}\
                   --dream_repeats {} --oas {} --online {}\
                --leaf_example_multiplier {} --Alpha {} -l {} -b {} -c --passes {} --loss_function {} --holdout_off -f {}".format(
                train_data, tree_node, learn_at_leaf, num_of_classes, dream_at_update,
                dream_repeats, use_oas, online, leaf_example_multiplier, alpha, lr, bits, passes, loss, saved_model))
train_time = time.time() - start

    #test:
#print "## Testing..."
#start = time.time();
#os.system(".././vw {} -i {}".format(test_data, saved_model))

#test_time = time.time() - start

print("## train time {}, and test time {}".format(train_time, test_time))





