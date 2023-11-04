import scipy as sp
import main_PnP_MASK_Synthetic
import KTCScoring
 
 

#The third parameter represents the difficulty group
main_PnP_MASK_Synthetic.main('TrainingData/','Output_PnP_MASK_Synthetic/',2)

score = 0
for ii in range(4):

    reco = sp.io.loadmat('Output_PnP_MASK_Synthetic/' + str(ii+1) + '.mat')
    reco = reco["reconstruction"]
    
    truth = sp.io.loadmat('GroundTruths/true' + str(ii+1) + '.mat')
    truth = truth["truth"]
    
    s = KTCScoring.scoringFunction(truth, reco)
    print('Score from target ' + str(ii+1) + ' = ' + str(s))
    score = score + s

print('Final score: ' + str(score) + ' / 4.00')
