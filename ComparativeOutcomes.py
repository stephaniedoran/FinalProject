import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov

# simulate warfarin
# create a cohort
cohort_warfarin = MarkovCls.Cohort(id=0, therapy=P.Therapies.WARFARIN)
# simulate cohort
simOutputs_warfarin = cohort_warfarin.simulate()

# simulate dabigatran_110
cohort_dabigatran_110 = MarkovCls.Cohort(id=1, therapy=P.Therapies.DABIGATRAN_110MG)
simOutputs_dabigatran_110 = cohort_dabigatran_110.simulate()

# simulate dabigatran_150
cohort_dabigatran_150 = MarkovCls.Cohort(id=1, therapy=P.Therapies.DABIGATRAN_150MG)
simOutputs_dabigatran_150 = cohort_dabigatran_150.simulate()

SupportMarkov.draw_survival_curves_and_histograms(simOutputs_warfarin=simOutputs_warfarin, simOutputs_dabigatran_110=simOutputs_dabigatran_110,
                                                  simOutputs_dabigatran_150=simOutputs_dabigatran_150)

SupportMarkov.print_outcomes(simOutputs_warfarin, "Warfarin")
SupportMarkov.print_outcomes(simOutputs_dabigatran_110, "Dabigatran 110mg")
SupportMarkov.print_outcomes(simOutputs_dabigatran_150, "Dabigatran 150mg")

print('Warfarin vs. Dabigatran 110mg')
SupportMarkov.print_comparative_outcomes(simOutputs_warfarin, simOutputs_dabigatran_110)

print('Warfarin vs. Dabigatran 150mg')
SupportMarkov.print_comparative_outcomes(simOutputs_warfarin, simOutputs_dabigatran_150)

print('Dabigatran 110mg vs. Dabigatran 150mg')
SupportMarkov.print_comparative_outcomes(simOutputs_dabigatran_110, simOutputs_dabigatran_150)

SupportMarkov.report_CEA_CBA(simOutputs_warfarin=simOutputs_warfarin, simOutputs_dabigatran_110=simOutputs_dabigatran_110,
                             simOutputs_dabigatran_150=simOutputs_dabigatran_150)
